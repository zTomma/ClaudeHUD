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
      "itemcountcolor_noitems", "itemcountcolor", "fgcolor_other", "fgcolor_local", "chat_color_player_name",
      "chat_color_default", "chat_color_chat_text", "buttontextcolor"}
BG = {"bgcolor", "bgcolor_override", "defaultbgcolor_override", "armedbgcolor_override", "depressedbgcolor_override",
      "selectedbgcolor_override", "disabledbgcolor_override", "fillcolor", "panel_bgcolor", "panel_bgcolor_mouseover",
      "item_panel_bgcolor", "item_panel_bgcolor_mouseover", "item_panel_bgcolor_selected", "infocus_bgcolor_override",
      "outoffocus_bgcolor_override", "titlebarbgcolor_override", "selectioncolor_override",
      "defaultselectionbg2color_override", "armedbgcolor", "basebackgroundcolor", "localbackgroundcolor",
      "backgroundoverridecolor", "meterbg", "item_backdrop_color", "fillcolor_lodef", "thumbnail_bgcolor",
      "thumbnail_bgcolor_selected", "thumbnail_bgcolor_mouseover", "boxcolor", "selectedboxclor",
      "color_portrait_bg_red", "color_portrait_bg_red_dead", "color_portrait_bg_blue", "color_portrait_bg_blue_dead",
      "color_portrait_blend_dead_red", "color_portrait_blend_dead_blue"}
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
BORDER_FILL = {
    "mainmenubgborder": ("DkCard", "LtCard"), "mainmenubgborderalpha": ("DkCardSoft", "LtCard"),
    "graydialogborder": ("DkCard", "LtCard"), "steamworkshopborder": ("DkCard", "LtCard"),
    "quickplayborder": ("DkCard", "LtCard"), "replaydefaultborder": ("DkCard", "LtCard"),
    "storepreviewtabselected": ("DkChip", "LtCardAlt"), "storepreviewtabunselected": ("DkCard", "LtCard"),
    "innershadowborder": ("DkChip", "LtCardAlt"), "innershadowborderthin": ("DkChip", "LtCardAlt"),
    "storeinnershadowborder": ("DkChip", "LtCardAlt"), "outershadowborder": ("DkCard", "LtCard"),
    "outershadowborderthin": ("DkCard", "LtCard"), "tffatlineborder": ("DkCard", "LtCard"),
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


def convert_color(key, value, mode, ctx):
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
        elif name in T.ROLES or re.match(r"^(Dk|Lt)\w+A\d0$", name):
            return None  # already a token
        else:
            return None  # unknown name (e.g. game-specific) - leave untouched, lint will report
        if mode == "light" and token.startswith("Dk"):
            fg_t, bg_t = DK_TO_LT.get(token, (token, token))
            token = bg_t if cat == "bg" else fg_t
        if T.ROLES[token][1] < 255:
            alpha = min(alpha, 255)
        ctx.stats["name"] += 1
    final = with_alpha(token, alpha, ctx)
    if k in ctx.name_ok:
        return final, None
    r, g, b, a = variant_rgba(final)
    return "%d %d %d %d" % (r, g, b, a), "token: %s" % final


def element_kv(body):
    return {k.lower(): v for k, v, c, cm in body if not isinstance(v, list)}


def migrate_nodes(nodes, mode, ctx):
    for path, nd in list(vdf.walk(nodes)):
        key, value = nd[0], nd[1]
        if isinstance(value, list):
            fix_element(value, mode, ctx)
            continue
        if key.lower() in ALL_COLOR_KEYS:
            res = convert_color(key, value, mode, ctx)
            if res:
                nd[1], cm = res
                nd[3] = cm
        elif key.lower() in ("font", "font_minmode", "font_lodef", "font_hidef") and mode == "light":
            new = LIGHT_TITLE_FONTS.get(value.lower())
            if new:
                nd[1] = new
                ctx.stats["font"] += 1


def fix_element(body, mode, ctx):
    kv = element_kv(body)
    border = (kv.get("border") or kv.get("border_default") or "").lower()
    if not border:
        return
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
        return
    fill = BORDER_FILL.get(border)
    if fill and "bgcolor_override" not in kv:
        token = fill[0] if mode == "dark" else fill[1]
        body.append(["bgcolor_override", token, None, "ClaudeHUD: riempimento al posto del bordo texture"])
        if kv.get("paintbackground") == "0":
            vdf.set_value(body, "paintbackground", "1")
        ctx.stats["panel_fill"] += 1


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
        src = os.path.join(PRISTINE_ROOT, rel)
        if not os.path.exists(src):
            continue
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
