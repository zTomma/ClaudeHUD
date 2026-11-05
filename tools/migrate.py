#!/usr/bin/env python3
"""
Migrate every HUD .res file to the ClaudeHUD design tokens.

For each file under resource/ and scripts/ (schemes excluded) the PRISTINE copy is read
from "#TF2 Files/<same path>" (never edited) and rewritten with:
  * every literal colour -> the role token of its mode (DESIGN.md §3, §9)
  * every legacy colour / BaseSettings name -> explicit Dk*/Lt* token
  * on light surfaces, legacy title fonts -> serif type tokens
  * panels that relied on a textured legacy border for their background get an explicit
    fill (the legacy borders are flattened in the scheme)
Keys that are not proven to accept scheme colour names (no occurrence with a name in
Valve's own files) receive the token's RGBA literal with a `// token: X` comment, so the
value is still generated from tools/tokens.py and traceable.

Files whose first line contains "ClaudeHUD: riscritto" are hand-written: never touched.

  python3 tools/migrate.py           migrate everything
  python3 tools/migrate.py --dry     report only
"""
import glob
import json
import os
import re
import sys
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import build_scheme as B  # noqa: E402
import modes  # noqa: E402
import tokens as T  # noqa: E402
import vdf  # noqa: E402

PRISTINE_ROOT = os.path.join(ROOT, "#TF2 Files")
REF_ROOTS = ["#TF2 Files", "#HL2 Files", "#Platform Files"]   # same priority as the game's search paths
# Panels the game loads from the hl2/platform VPKs (TF2 does not override them) that still carry
# default-HUD colours: copied into the HUD tree and migrated like every other file.
PROMOTE = [
    "resource/ui/replaybrowser/recordspanel.res", "resource/ui/replaybrowser/renderdialog.res",
    "resource/ui/replaybrowser/cutspanel.res", "resource/ui/replaybrowser/mainpanel.res",
    "resource/ui/replaybrowser/titleeditpanel.res", "resource/ui/replaybrowser/previewpanel.res",
    "resource/ui/replaybrowser/listthumbnail.res", "resource/ui/replaybrowser/thumbnailcollection.res",
    "resource/ui/replaybrowser/playbackpanelslideshow.res", "resource/ui/replaybrowser/confirmquitdlg.res",
    "resource/ui/replaybrowser/thumbnailrow.res",
    "resource/ui/replayperformanceeditor/settings_timescale.res", "resource/ui/replayperformanceeditor/savedlg.res",
    "resource/ui/replayperformanceeditor/reclight.res", "resource/ui/replayperformanceeditor/camsettings_free.res",
    "resource/ui/replayperformanceeditor/tip.res", "resource/ui/replayperformanceeditor/main.res",
    "resource/ui/replayinputpanel.res", "resource/ui/replaymessagedlg.res", "resource/ui/replaymessage.res",
    "resource/ui/replayrenderoverlay.res", "resource/ui/youtubeuploadwaitingdialog.res",
    "resource/ui/youtubelogindialog.res", "resource/ui/youtubeuploaddialog.res",
    "resource/ui/achievementgroup.res", "resource/ui/achievementitem.res", "resource/ui/statitem.res",
    "resource/ui/commentarymodelviewer.res",
    "resource/ui/econ/confirmdialog.res", "resource/ui/econ/confirmdialog_sc.res",
    "resource/ui/econ/messageboxdialog.res", "resource/ui/econ/messageboxdialog_sc.res",
    "resource/askconnectpanel.res", "servers/quicklistpanel.res",
]


def pristine_path(rel):
    for r in REF_ROOTS:
        p = os.path.join(ROOT, r, rel)
        if os.path.exists(p):
            return p
    return None
HAND_MARK = "ClaudeHUD: riscritto"
MIGRATED_MARK = "// ClaudeHUD: migrato ai token (layout originale) - generato da tools/migrate.py"
VARIANTS_FILE = os.path.join(HERE, "generated_variants.json")

FG = {"fgcolor", "fgcolor_override", "defaultfgcolor_override", "armedfgcolor_override", "depressedfgcolor_override",
      "selectedfgcolor_override", "disabledfgcolor_override", "disabledfgcolor1_override", "disabledfgcolor2_override",
      "textcolor", "noitem_textcolor", "selectiontextcolor_override", "titlebarfgcolor_override",
      "titlebardisabledfgcolor_override", "fgcolor_lodef", "headerfgcolor", "enabled_text_color_override",
      "disabled_text_color_override", "link_color", "bright_color", "standard_color", "positivecolor", "negativecolor",
      "itemset_color", "highlight_color", "color_red", "color_blue", "selectedcolor", "unselectedcolor", "linecolor",
      "color", "healthdeathwarningcolor", "keyboardfocuscolor_override", "blinkfgcolor_override", "color_outline",
      "teamblue", "teamred", "localplayercolor", "flashcolor", "button.armedtextcolor", "slidertickcolor",
      "selected_fgcolor_override", "color_ready", "color_notready", "titlecolor", "selectionnumberfg", "messagecolor",
      "itemcountcolor_noitems", "itemcountcolor", "fgcolor_other", "fgcolor_local", "chat_color_player_name", "progressbarcolor",
      "chat_color_default", "chat_color_chat_text", "buttontextcolor", "purpletext", "greentext", "eventcolor",
      "redrobotscorecolor", "bluerobotscorecolor"}
BG = {"bgcolor", "bgcolor_override", "defaultbgcolor_override", "armedbgcolor_override", "depressedbgcolor_override",
      "selectedbgcolor_override", "disabledbgcolor_override", "fillcolor", "panel_bgcolor", "panel_bgcolor_mouseover",
      "item_panel_bgcolor", "item_panel_bgcolor_mouseover", "item_panel_bgcolor_selected", "infocus_bgcolor_override",
      "outoffocus_bgcolor_override", "titlebarbgcolor_override", "selectioncolor_override",
      "defaultselectionbg2color_override", "armedbgcolor", "basebackgroundcolor", "localbackgroundcolor",
      "backgroundoverridecolor", "meterbg", "item_backdrop_color", "fillcolor_lodef", "thumbnail_bgcolor",
      "thumbnail_bgcolor_selected", "thumbnail_bgcolor_mouseover", "boxcolor", "selectedboxclor",
      "color_portrait_bg_red", "color_portrait_bg_red_dead", "color_portrait_bg_blue", "color_portrait_bg_blue_dead",
      "color_portrait_blend_dead_red", "color_portrait_blend_dead_blue", "killstreakbackgroundcolor"}
IMG = {"image_drawcolor", "image_armedcolor", "image_depressedcolor", "image_disabledcolor", "image_selectedcolor",
       "iconcolor", "drawcolor", "drawcolor_override", "meterfg", "inactivedrawcolor", "activedrawcolor",
       "color_bar_health_high", "color_bar_health_med", "color_bar_health_low"}
ALL_COLOR_KEYS = FG | BG | IMG

# reference colours of the default HUD -> semantic role
OLD_REFS = [
    ((46, 43, 42), "surface"), ((41, 37, 38), "surface"), ((52, 48, 45), "surface"), ((51, 47, 46), "surface"),
    ((60, 56, 53), "surface"), ((48, 43, 42), "surface"), ((32, 32, 32), "surface"), ((52, 48, 55), "surface2"),
    ((59, 54, 48), "surface2"), ((72, 71, 69), "surface2"), ((77, 72, 68), "surface2"), ((69, 64, 58), "surface2"),
    ((95, 92, 101), "surface2"), ((0, 0, 0), "black"),
    ((117, 107, 94), "muted"), ((118, 107, 94), "muted"), ((130, 120, 104), "muted"), ((128, 117, 104), "muted"),
    ((131, 121, 104), "muted"), ((156, 146, 128), "muted"), ((176, 166, 148), "muted"), ((173, 165, 146), "muted"),
    ((178, 178, 178), "muted"), ((124, 124, 124), "muted"), ((100, 100, 100), "muted"), ((139, 137, 137), "muted"),
    ((235, 226, 202), "text"), ((236, 227, 203), "text"), ((251, 235, 202), "text"), ((200, 187, 161), "text"),
    ((246, 247, 213), "text"), ((248, 231, 198), "text"), ((235, 235, 235), "text"), ((245, 229, 196), "text"),
    ((200, 184, 151), "text"), ((255, 255, 255), "white"),
    ((200, 80, 60), "accent"), ((178, 82, 22), "accent"), ((145, 73, 59), "accent"), ((250, 114, 45), "accent"),
    ((255, 133, 0), "accent"), ((220, 100, 80), "accent"), ((150, 71, 0), "accent"), ((239, 128, 73), "accent"),
    ((207, 106, 50), "accent"), ((188, 112, 0), "accent"),
    ((255, 0, 0), "danger"), ((240, 30, 30), "danger"), ((255, 64, 64), "danger"), ((192, 28, 0), "danger"),
    ((180, 92, 77), "red"), ((192, 56, 63), "red"), ((184, 56, 59), "red"), ((157, 49, 47), "red"),
    ((104, 124, 155), "blue"), ((92, 128, 166), "blue"), ((91, 122, 142), "blue"), ((153, 204, 255), "blue"),
    ((71, 98, 145), "blue"), ((88, 133, 162), "blue"), ((0, 28, 162), "blue"),
    ((0, 255, 0), "green"), ((112, 176, 74), "green"), ((76, 107, 34), "green"), ((94, 150, 49), "green"),
    ((0, 160, 0), "green"),
    ((255, 215, 0), "gold"), ((240, 207, 78), "gold"), ((212, 160, 23), "gold"), ((208, 147, 75), "gold"),
    ((251, 235, 0), "gold"), ((255, 167, 42), "gold"),
]

ROLE_MAP = {
    "dark": {
        "fg": {"text": "DkText", "white": "DkText", "muted": "DkTextMuted", "surface": "DkOnRed", "surface2": "DkTextMuted",
               "black": "DkOnRed", "accent": "DkAccent", "danger": "DkAccent", "red": "DkRedText", "blue": "DkBluText",
               "green": "DkPositive", "gold": "DkAccent"},
        "bg": {"text": "DkAccent", "white": "DkAccent", "muted": "DkChip", "surface": "DkCard", "surface2": "DkChip",
               "black": "DkCard", "accent": "DkAccent", "danger": "DkAccent", "red": "DkRedFill", "blue": "DkBluFill",
               "green": "DkPositiveFill", "gold": "DkAccent"},
        "img": {"text": "DkText", "white": "Untinted", "muted": "DkTextMuted", "surface": "DkCard", "surface2": "DkChip",
                "black": "DkOnRed", "accent": "DkAccent", "danger": "DkAccent", "red": "DkRedText", "blue": "DkBluText",
                "green": "DkPositive", "gold": "DkAccent"},
    },
    "light": {
        "fg": {"text": "LtText", "white": "LtText", "muted": "LtTextMuted", "surface": "LtText", "surface2": "LtTextMuted",
               "black": "LtText", "accent": "LtAccentText", "danger": "LtAccentText", "red": "LtRedText", "blue": "LtBluText",
               "green": "LtPositive", "gold": "LtAccentText"},
        "bg": {"text": "LtButtonHover", "white": "LtButtonHover", "muted": "LtCardAlt", "surface": "LtCard",
               "surface2": "LtCardAlt", "black": "LtCardAlt", "accent": "LtAccent", "danger": "LtAccent", "red": "LtRedFill",
               "blue": "LtBluFill", "green": "LtPositive", "gold": "LtAccent"},
        "img": {"text": "LtText", "white": "Untinted", "muted": "LtTextMuted", "surface": "LtText", "surface2": "LtTextMuted",
                "black": "LtText", "accent": "LtAccent", "danger": "LtAccent", "red": "LtRedText", "blue": "LtBluText",
                "green": "LtPositive", "gold": "LtAccent"},
    },
}

# dark token -> light token (fg / bg), used for legacy names on light surfaces
DK_TO_LT = {
    "DkCard": ("LtText", "LtCard"), "DkCardSoft": ("LtText", "LtCard"), "DkCardGhost": ("LtText", "LtCardAlt"),
    "DkChip": ("LtTextMuted", "LtCardAlt"), "DkLine": ("LtLine", "LtLine"), "DkCardLocal": ("LtText", "LtCardAlt"),
    "DkText": ("LtText", "LtButtonHover"), "DkTextMuted": ("LtTextMuted", "LtCardAlt"),
    "DkTextFaint": ("LtTextFaint", "LtCardPressed"), "DkAccent": ("LtAccentText", "LtAccent"),
    "DkAccentSoft": ("LtAccentText", "LtCardPressed"), "DkPositive": ("LtPositive", "LtPositive"),
    "DkPositiveFill": ("LtPositive", "LtPositive"), "DkInfo": ("LtBluText", "LtBluFill"),
    "DkRedText": ("LtRedText", "LtRedFill"), "DkBluText": ("LtBluText", "LtBluFill"),
    "DkRedFill": ("LtRedText", "LtRedFill"), "DkBluFill": ("LtBluText", "LtBluFill"),
    "DkOnRed": ("LtText", "LtText"), "DkOnBlu": ("LtOnBlu", "LtOnBlu"), "DkScrim": ("LtText", "LtScrim"),
    "LtText": ("LtText", "LtText"), "LtCard": ("LtText", "LtCard"), "LtAccent": ("LtAccentText", "LtAccent"),
    "LtTextMuted": ("LtTextMuted", "LtCardAlt"),
}

# flattened legacy borders -> (dark fill, light fill) for panels that had no bg of their own
# shadow borders are transparent overlays drawn ABOVE content (zpos): they must never get a fill
BORDER_FILL = {
    "mainmenubgborder": ("DkCard", "LtCard"), "mainmenubgborderalpha": ("DkCardSoft", "LtCard"),
    "graydialogborder": ("DkCard", "LtCard"), "steamworkshopborder": ("DkCard", "LtCard"),
    "quickplayborder": ("DkCard", "LtCard"), "replaydefaultborder": ("DkCard", "LtCard"),
    "storepreviewtabselected": ("DkChip", "LtCardAlt"), "storepreviewtabunselected": ("DkCard", "LtCard"),
    "innershadowborder": ("Clear", "Clear"), "innershadowborderthin": ("Clear", "Clear"),
    "storeinnershadowborder": ("Clear", "Clear"), "outershadowborder": ("Clear", "Clear"),
    "outershadowborderthin": ("Clear", "Clear"), "tffatlineborder": ("DkCard", "LtCard"),
    "tffatlineborderopaque": ("DkCard", "LtCard"), "tfthinlineborder": ("DkCard", "LtCard"),
    "tffatlineborderclearbg": ("Clear", "Clear"), "tffatlineborderredbg": ("DkRedFill", "LtRedFill"),
    "tffatlineborderredbgopaque": ("DkRedFill", "LtRedFill"), "tffatlineborderredbgmoreopaque": ("DkRedFill", "LtRedFill"),
    "tffatlineborderredbgopaque_store": ("DkRedFill", "LtRedFill"), "tffatlinebordervbluebg": ("DkBluFill", "LtBluFill"),
    "tffatlinebordervblueBGopaque": ("DkBluFill", "LtBluFill"), "tffatlineborderbluebg": ("DkBluFill", "LtBluFill"),
    "tffatlineborderbluebgopaque": ("DkBluFill", "LtBluFill"), "tffatlineborderbluebgmoreopaque": ("DkBluFill", "LtBluFill"),
    "mainmenuhighlightborder": ("DkCard", "DkCard"), "loadoutitempopupborder": ("DkCard", "DkCard"),
    "tooltipborder": ("DkCard", "DkCard"), "econitemborder": ("DkCard", "DkCard"), "cyoapopupborder": ("DkCard", "DkCard"),
    "cyoanodeviewborder": ("DkChip", "DkChip"), "queststatusborder": ("DkCard", "DkCard"),
    "notificationdefault": ("DkCard", "LtCard"), "notificationhighpriority": ("DkCard", "LtCard"),
    "outlinedgreybox": ("DkChip", "LtCardAlt"), "outlineddullgreybox": ("DkChip", "LtCardAlt"),
    "sortcategoryborder": ("DkChip", "LtCardAlt"), "trainingresultsbg": ("DkCard", "LtCard"),
    "storepreviewborder": ("DkChip", "LtCardAlt"), "storepromotion": ("DkChip", "LtCardAlt"),
    "storenewborder": ("DkChip", "LtCardAlt"), "storediscountborder": ("DkChip", "LtCardAlt"),
    "storeaddtocart": ("DkAccent", "LtAccent"), "storehighlightedborder": ("DkChip", "LtCardAlt"),
    "storefreetrialborder": ("DkChip", "LtCardAlt"), "salepriceborder": ("DkChip", "LtCardAlt"),
    "friendhighlightborder": ("DkChip", "LtCardAlt"), "friendhighlightborderthick": ("DkChip", "LtCardAlt"),
    "replayhighlightborder": ("DkChip", "LtCardAlt"), "darkcomboboxborder": ("DkChip", "LtCardAlt"),
}
BUTTON_BORDERS = {"mainmenubuttondefault", "mainmenuminibuttondefault", "mainmenusubbuttonborder", "mainmenubuttonglow",
                  "mainmenubuttondisabled", "econ.button.border.default", "buttonborder", "mainmenubuttonarmed",
                  "mainmenuminibuttonarmed", "econ.button.border.armed"}
LIGHT_TITLE_FONTS = {}  # filled in main(): legacy display font -> serif type token on light surfaces


# ---------------------------------------------------------------------------------------------
# Which colour keys resolve SCHEME NAMES - verified in the TF2 client source (Source SDK 2013, 2025):
#   Panel/Button/Label/Frame/TextEntry  REGISTER_COLOR_AS_OVERRIDABLE  -> *_override keys below
#   ImagePanel::ApplySettings           fillcolor, drawcolor (sscanf, else scheme GetColor)
#   CExLabel/CExButton/CExRichText      fgcolor (SetColorStr -> scheme GetColor)
#   CPanelAnimationVar(Color)           HUD element vars (killfeed, damage numbers...) -> scheme GetColor
#   CExImageButton                      image_*color: sscanf ONLY -> a name is silently ignored
# Everything not listed gets the token's RGBA literal (+ "// token: X"), which every parser accepts.
VERIFIED_NAME_KEYS = {
    "fgcolor_override", "bgcolor_override", "defaultfgcolor_override", "defaultbgcolor_override",
    "armedfgcolor_override", "armedbgcolor_override", "depressedfgcolor_override", "depressedbgcolor_override",
    "selectedfgcolor_override", "selectedbgcolor_override", "keyboardfocuscolor_override", "blinkfgcolor_override",
    "disabledfgcolor2_override", "infocus_bgcolor_override", "outoffocus_bgcolor_override",
    "titlebarbgcolor_override", "titlebardisabledbgcolor_override", "titlebarfgcolor_override",
    "titlebardisabledfgcolor_override", "disabledfgcolor_override", "disabledbgcolor_override",
    "selectioncolor_override", "selectiontextcolor_override", "defaultselectionbg2color_override"}
IMAGEPANEL_CTLS = {"imagepanel", "ctfimagepanel"}
EXLABEL_CTLS = {"cexlabel", "cexbutton", "ceximagebutton", "cexrichtext"}
ANIMVAR_KEYS = {"teamblue", "teamred", "purpletext", "greentext", "localplayercolor", "iconcolor",
                "basebackgroundcolor", "localbackgroundcolor", "killstreakbackgroundcolor", "positivecolor",
                "negativecolor", "eventcolor", "redrobotscorecolor", "bluerobotscorecolor"}


def name_allowed(key, ctl):
    k, c = key.lower(), (ctl or "").lower()
    if k in VERIFIED_NAME_KEYS:
        return True
    if k in ("fillcolor", "drawcolor") and c in IMAGEPANEL_CTLS:
        return True
    if k == "fgcolor" and c in EXLABEL_CTLS:
        return True
    if k in ANIMVAR_KEYS and c == "":
        return True  # HUD element blocks in hudlayout.res (no ControlName): CPanelAnimationVar colours
    return False


def is_token_name(v):
    v = v.strip()
    return v in T.ROLES or bool(re.match(r"^((Dk|Lt)[A-Za-z]+|Untinted)A\d0$", v))


def nearest_role(rgb):
    best, role = 1e9, None
    for ref, r in OLD_REFS:
        d = sum((a - b) ** 2 for a, b in zip(rgb, ref)) ** 0.5
        if d < best:
            best, role = d, r
    if best <= 48:
        return role
    lum = T.luminance(rgb)
    if lum > 0.55:
        return "text"
    if lum > 0.12:
        return "muted"
    return "surface"


class Ctx:
    def __init__(self, scheme_colors, base_settings, name_ok):
        self.colors = scheme_colors      # legacy name(lower) -> (name, rgba)
        self.base = base_settings        # BaseSettings name(lower) -> value
        self.name_ok = name_ok
        self.variants = set()
        self.stats = Counter()


def parse_rgba(v):
    p = [int(float(x)) for x in v.split()]
    while len(p) < 4:
        p.append(255)
    return tuple(max(0, min(255, x)) for x in p[:4])


def is_literal(v):
    return bool(re.match(r"^\s*-?[\d.]+\s+-?[\d.]+\s+-?[\d.]+", v))


def with_alpha(token, alpha, ctx):
    """token name carrying the given alpha (0..255): base token, Clear, or <token>A<pct> variant."""
    if alpha <= 6:
        return "Clear"
    base_a = T.ROLES[token][1]
    if abs(alpha - base_a) <= 12 or token in ("Clear",):
        return token
    pct = int(round(alpha / 255 * 10)) * 10
    pct = max(10, min(90, pct))
    if abs(pct * 2.55 - base_a) <= 12:
        return token
    name = "%sA%d" % (token, pct)
    ctx.variants.add(name)
    return name


def variant_rgba(name):
    m = re.match(r"^(.*)A(\d0)$", name)
    if m and m.group(1) in T.ROLES:
        r, g, b, _ = T.rgba(m.group(1))
        return (r, g, b, int(round(int(m.group(2)) * 2.55)))
    return T.rgba(name)


def convert_color(key, value, mode, ctx, ctl=""):
    """Return (new_value, comment) or None to keep."""
    k = key.lower()
    cat = "fg" if k in FG else "bg" if k in BG else "img"
    if is_literal(value):
        rgba = parse_rgba(value)
        role = nearest_role(rgba[:3])
        token = ROLE_MAP[mode][cat][role]
        alpha = rgba[3]
        ctx.stats["literal"] += 1
    else:
        name = value.strip()
        lname = name.lower()
        if lname in ctx.colors:
            legacy, rgba = ctx.colors[lname]
            target = B.LEGACY_COLORS.get(legacy, "keep" if legacy.startswith(B.KEEP_PREFIXES) else None)
            if target in (None, "keep"):
                return None
            token, alpha = target, rgba[3]
        elif lname in ctx.base and ctx.base[lname] in T.ROLES:
            token, alpha = ctx.base[lname], T.ROLES[ctx.base[lname]][1]
        elif is_token_name(name):
            if name_allowed(key, ctl):
                return None  # already a token, and this key resolves names
            r, g, b, a = variant_rgba(name)
            return "%d %d %d %d" % (r, g, b, a), "token: %s" % name
        else:
            return None  # unknown name (e.g. game-specific) - leave untouched, lint will report
        if mode == "light" and token.startswith("Dk"):
            fg_t, bg_t = DK_TO_LT.get(token, (token, token))
            token = bg_t if cat == "bg" else fg_t
        if T.ROLES[token][1] < 255:
            alpha = min(alpha, 255)
        ctx.stats["name"] += 1
    final = with_alpha(token, alpha, ctx)
    if name_allowed(key, ctl):
        return final, None
    r, g, b, a = variant_rgba(final)
    return "%d %d %d %d" % (r, g, b, a), "token: %s" % final


def element_kv(body):
    return {k.lower(): v for k, v, c, cm in body if not isinstance(v, list)}


def block_ctl(body):
    for k, v, c, cm in body:
        if not isinstance(v, list) and k.lower() == "controlname":
            return v
    return ""


def migrate_nodes(nodes, mode, ctx, ctl=""):
    """Recursive: an element that becomes a dark popover (tooltip border) inside a light file switches
    its whole subtree to dark mode, so its labels get dark-mode tokens. ctl = ControlName of the block
    the leaves belong to (decides whether a colour key may hold a scheme name)."""
    for nd in nodes:
        key, value = nd[0], nd[1]
        if isinstance(value, list):
            sub_mode = fix_element(value, mode, ctx)
            migrate_nodes(value, sub_mode, ctx, block_ctl(value))
            continue
        if key.lower() in ALL_COLOR_KEYS:
            res = convert_color(key, value, mode, ctx, ctl)
            if res:
                nd[1], cm = res
                nd[3] = cm
        elif key.lower() in ("font", "font_minmode", "font_lodef", "font_hidef") and mode == "light":
            new = LIGHT_TITLE_FONTS.get(value.lower())
            if new:
                nd[1] = new
                ctx.stats["font"] += 1


LIGHT_TEXT_CONTROLS = {"label", "cexlabel", "cautofittinglabel", "cexrichtext", "richtext", "checkbutton",
                       "radiobutton"}
LIGHT_BUTTON_CONTROLS = {"cexbutton", "button", "cexImagebutton".lower(), "imagebutton", "ctfteambutton"}


def light_defaults(body, kv, ctx):
    """On light surfaces, controls without explicit colours would inherit the scheme default (dark
    semantics: ivory text) and vanish on white cards. Give them explicit light tokens."""
    ctl = kv.get("controlname", "").lower()
    note = "ClaudeHUD: colore esplicito in modalita' chiara"
    if ctl in LIGHT_TEXT_CONTROLS and "fgcolor" not in kv and "fgcolor_override" not in kv:
        body.append(["fgcolor_override", "LtText", None, note])
        ctx.stats["light_text"] += 1
    elif ctl in LIGHT_BUTTON_CONTROLS:
        if "defaultfgcolor_override" not in kv and "fgcolor_override" not in kv:
            body.append(["defaultFgColor_override", "LtText", None, note])
            body.append(["armedFgColor_override", "LtOnButtonHover", None, note])
            body.append(["depressedFgColor_override", "LtOnButtonHover", None, note])
            ctx.stats["light_button_fg"] += 1
        if "defaultbgcolor_override" not in kv and kv.get("paintbackground", "1") != "0":
            body.append(["defaultBgColor_override", "LtCardAlt", None, note])
            body.append(["armedBgColor_override", "LtButtonHover", None, note])
            body.append(["depressedBgColor_override", "LtButtonHover", None, note])
            ctx.stats["light_button_bg"] += 1


def fix_element(body, mode, ctx):
    """Fix one element in place and return the mode its subtree must use."""
    kv = element_kv(body)
    border = (kv.get("border") or kv.get("border_default") or "").lower()
    if mode == "light" and BORDER_FILL.get(border, ("", ""))[1].startswith("Dk"):
        mode = "dark"  # tooltip / popover: always dark (DESIGN.md par. 9)
        ctx.stats["dark_popover"] += 1
    if mode == "light" and "controlname" in kv:
        light_defaults(body, kv, ctx)
        kv = element_kv(body)
    if not border:
        return mode
    ctl = kv.get("controlname", "").lower()
    if "button" in ctl:
        if border in BUTTON_BORDERS or border in BORDER_FILL:
            if "defaultbgcolor_override" not in kv and kv.get("paintbackground", "1") != "0":
                d = "DkChip" if mode == "dark" else "LtCardAlt"
                a = "DkAccent" if mode == "dark" else "LtButtonHover"
                add = [("defaultBgColor_override", d), ("armedBgColor_override", a), ("depressedBgColor_override", a)]
                if "defaultfgcolor_override" not in kv:
                    add += [("defaultFgColor_override", "DkText" if mode == "dark" else "LtText"),
                            ("armedFgColor_override", "DkOnRed" if mode == "dark" else "LtOnButtonHover"),
                            ("depressedFgColor_override", "DkOnRed" if mode == "dark" else "LtOnButtonHover")]
                for k, v in add:
                    body.append([k, v, None, "ClaudeHUD: riempimento al posto del bordo texture"])
                ctx.stats["button_fill"] += 1
        return mode
    fill = BORDER_FILL.get(border)
    if fill and "bgcolor_override" not in kv:
        token = fill[0] if mode == "dark" else fill[1]
        body.append(["bgcolor_override", token, None, "ClaudeHUD: riempimento al posto del bordo texture"])
        if kv.get("paintbackground") == "0":
            vdf.set_value(body, "paintbackground", "1")
        ctx.stats["panel_fill"] += 1
    return mode


def load_ctx():
    src = vdf.parse(open(B.PRISTINE, encoding="utf-8", errors="replace").read())
    scheme = vdf.get(src, "Scheme")
    colors = {}
    for k, v, c, cm in vdf.get(scheme, "Colors"):
        if not isinstance(v, list):
            colors[k.lower()] = (k, B.parse_rgba(v))
    base = {}
    for k, v, c, cm in vdf.get(scheme, "BaseSettings"):
        if not isinstance(v, list):
            base[k.lower()] = B.BASE.get(k, v)
    # evidence: keys that Valve's own files use with a scheme colour NAME
    name_ok = set()
    known = set(colors) | set(base)
    for p in glob.glob(os.path.join(PRISTINE_ROOT, "resource", "**", "*.res"), recursive=True) + \
            [os.path.join(PRISTINE_ROOT, "scripts", "hudlayout.res")]:
        for k, v in re.findall(r'^\s*"?([A-Za-z0-9_.]+)"?\s+"([A-Za-z][A-Za-z0-9_.]*)"', open(p, encoding="utf-8", errors="replace").read(), re.M):
            if k.lower() in ALL_COLOR_KEYS and v.lower() in known:
                name_ok.add(k.lower())
    # legacy fonts that become serif titles on light surfaces
    for name, body, cond, _ in vdf.get(scheme, "Fonts"):
        if not isinstance(body, list):
            continue
        m = B.legacy_font_entry(name, body)
        if not m:
            continue
        fam, w, tall, flags = m
        if fam == T.SANS_SEMI[0] and tall >= 15:
            LIGHT_TITLE_FONTS[name.lower()] = "TypeTitle" if tall >= 24 else "TypeHeading"
    return Ctx(colors, base, name_ok)


def targets():
    out = []
    for p in sorted(glob.glob(os.path.join(ROOT, "resource", "**", "*.res"), recursive=True)):
        rel = os.path.relpath(p, ROOT).replace("\\", "/")
        if rel in ("resource/clientscheme.res", "resource/sourcescheme.res", "resource/chatscheme.res"):
            continue
        out.append(rel)
    for p in sorted(glob.glob(os.path.join(ROOT, "scripts", "**", "*.res"), recursive=True)):
        out.append(os.path.relpath(p, ROOT).replace("\\", "/"))
    for rel in PROMOTE:
        if rel not in out:
            out.append(rel)
    return out


def is_hand_written(path):
    try:
        with open(path, encoding="utf-8", errors="replace") as f:
            return HAND_MARK in f.read(400)
    except FileNotFoundError:
        return False


def main(dry=False):
    ctx = load_ctx()
    done = skipped = 0
    for rel in targets():
        dst = os.path.join(ROOT, rel)
        if is_hand_written(dst):
            skipped += 1
            continue
        src = pristine_path(rel)
        if not src:
            continue
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        text = open(src, encoding="utf-8", errors="replace").read()
        nodes = vdf.parse(text)
        migrate_nodes(nodes, modes.mode_of(rel), ctx)
        out = MIGRATED_MARK + "\n// modalita': %s (DESIGN.md par. 9)\n" % modes.mode_of(rel) + vdf.dump(nodes) + "\n"
        vdf.parse(out)
        if not dry:
            with open(dst, "w", encoding="utf-8", newline="\n") as f:
                f.write(out)
        done += 1
    if False:  # variants are discovered by build_scheme.py scanning the files
        json.dump(sorted(ctx.variants), f, indent=1)
    print("migrated %d files, skipped %d hand-written; %s; alpha variants: %d; name-ok keys: %d"
          % (done, skipped, dict(ctx.stats), len(ctx.variants), len(ctx.name_ok)))


if __name__ == "__main__":
    main("--dry" in sys.argv)


def sanitize(nodes, ctx=None, ctl=""):
    """Post-pass for hand edits: any token NAME in a key that does not resolve names -> RGBA literal."""
    for nd in nodes:
        if isinstance(nd[1], list):
            sanitize(nd[1], ctx, block_ctl(nd[1]))
        elif (nd[0].lower() in ALL_COLOR_KEYS or nd[0].lower().endswith("color")) and is_token_name(nd[1]) \
                and not name_allowed(nd[0], ctl):
            r, g, b, a = variant_rgba(nd[1].strip())
            nd[3] = "token: %s" % nd[1].strip()
            nd[1] = "%d %d %d %d" % (r, g, b, a)
