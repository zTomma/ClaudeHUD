#!/usr/bin/env python3
"""
Generate resource/clientscheme.res from tools/tokens.py.

Source of the legacy structure: the pristine copy kept in "#TF2 Files/resource/clientscheme.res"
(never edited), so this script is idempotent: run it again after changing tokens.py.

  python3 tools/build_scheme.py            -> writes resource/clientscheme.res
  python3 tools/build_scheme.py --report   -> also prints the legacy font/border mapping

Sections produced:
  Colors          ClaudeHUD role tokens + every legacy colour name (remapped or kept)
  BaseSettings    every legacy key, re-pointed to tokens
  Fonts           ClaudeHUD type scale + every legacy font name (remapped or kept)
  Borders         ClaudeHUD borders + every legacy border name (flattened or kept)
  CustomFontFiles bundled static TTFs + the game icon fonts
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import tokens as T  # noqa: E402
import vdf  # noqa: E402

PRISTINE = os.path.join(ROOT, "#TF2 Files", "resource", "clientscheme.res")
OUT = os.path.join(ROOT, "resource", "clientscheme.res")

# ----------------------------------------------------------------------------------------
# Legacy colour names -> token ("keep" = game semantics, value untouched).
# Legacy names are what the game's C++ code asks for, so they all stay defined.
# They follow the DARK semantics (in-game + item surfaces); light files are migrated to
# explicit Lt* tokens by tools/migrate.py.
# ----------------------------------------------------------------------------------------
LEGACY_COLORS = {
    "Orange": "DkAccent", "OrangeDim": "DkAccentSoft", "LightOrange": "DkAccentSoft",
    "GoalOrange": "DkAccent", "TFOrange": "DkAccent", "Purple": "keep",
    "QuestGold": "keep", "HalloweenThemeColor2015_Light": "keep", "HalloweenThemeColor2015": "keep",
    "HalloweenThemeColor2015_Dark": "keep", "QuestUncommitted": "keep",
    "QuestMap_Bonus": "keep", "QuestMap_ActiveOrange": "DkAccent", "QuestMap_InactiveGrey": "DkTextFaint",
    "QuestMap_BGImages": "DkChip",
    "White": "DkText", "Red": "DkAccentSoft", "RedSolid": "DkRedFill", "Blue": "DkBluFill",
    "Yellow": "DkText", "TransparentYellow": "DkTextMuted", "BrightYellow": "DkAccent",
    "GreenSolid": "DkPositiveFill", "Black": "DkCard", "TransparentBlack": "DkCardSoft",
    "TransparentLightBlack": "DkCardGhost", "FooterBGBlack": "DkChip",
    "HUDBlueTeam": "DkBluFill", "HUDRedTeam": "DkRedFill", "HUDSpectator": "DkTextMuted",
    "HUDBlueTeamSolid": "DkBluFill", "HUDRedTeamSolid": "DkRedFill", "HUDDeathWarning": "DkAccent",
    "HudWhite": "DkText", "HudOffWhite": "DkText", "HudBlack": "LtText", "ProgressBarBlue": "DkInfo",
    "CreditsGreen": "DkPositive", "Gray": "DkTextMuted", "Blank": "Clear",
    "ForTesting": "keep", "ForTesting_Magenta": "keep", "ForTesting_MagentaDim": "keep",
    "HudPanelForeground": "DkCard", "HudPanelBackground": "DkCard", "HudPanelBorder": "DkLine",
    "HudProgressBarActive": "DkText", "HudProgressBarInActive": "DkChip",
    "HudProgressBarActiveLow": "DkAccent", "HudProgressBarInActiveLow": "DkAccentSoft",
    "HudTimerProgressActive": "DkText", "HudTimerProgressInActive": "DkChip", "HudTimerProgressWarning": "DkAccent",
    "HudTrainingHint": "DkAccent",
    "TanDark": "DkTextMuted", "TanLight": "DkText", "TanDarker": "DkCard",
    "StoreDarkTan": "DkTextMuted", "StoreGreen": "keep", "LowHealthRed": "DkAccent",
    "ProgressOffWhite": "DkText", "ProgressBackground": "DkChip", "HealthBgGrey": "DkChip",
    "ProgressOffWhiteTransparent": "DkTextMuted", "LabelDark": "DkCard", "LabelTransparent": "DkChip",
    "BuildMenuActive": "DkText", "DisguiseMenuIconRed": "DkRedText", "DisguiseMenuIconBlue": "DkBluText",
    "MatchmakingDialogTitleColor": "LtText", "MatchmakingMenuItemBackground": "LtCard",
    "MatchmakingMenuItemBackgroundActive": "LtAccent", "MatchmakingMenuItemTitleColor": "LtText",
    "MatchmakingMenuItemDescriptionColor": "LtTextMuted", "HTMLBackground": "LtCard",
    "ItemAttribLevel": "DkTextMuted", "ItemAttribNeutral": "DkText", "ItemAttribPositive": "keep",
    "ItemAttribNegative": "keep", "ItemSetName": "keep", "ItemSetItemEquipped": "keep",
    "ItemSetItemMissing": "keep", "ItemIsotope": "keep", "ItemBundleItem": "keep",
    "ItemLimitedUse": "keep", "ItemFlags": "DkTextMuted", "ItemLimitedQuantity": "keep",
    "SaleGreen": "keep", "LightRed": "DkAccent", "LighterRed": "DkAccent",
    "LighterDarkBrown": "DkChip", "DarkBrown": "DkCard",
    "UpgradeDefaultFg": "DkTextMuted", "UpgradeDefaultBg": "DkChip", "UpgradeArmedFg": "DkAccent",
    "UpgradeArmedBg": "DkAccent", "UpgradeDepressedFg": "DkAccent", "UpgradeDepressedBg": "DkAccent",
    "UpgradeSelectedFg": "DkAccent", "UpgradeSelectedBg": "DkAccent", "UpgradeDisabledFg": "DkTextFaint",
    "UpgradeDisabledBg": "DkCard",
}
KEEP_PREFIXES = ("QualityColor", "ItemRarity", "PartyMember")

# ----------------------------------------------------------------------------------------
# BaseSettings: explicit token for every colour key (dark semantics). Keys not listed keep
# their legacy value (which now resolves through the remapped legacy colours above).
# ----------------------------------------------------------------------------------------
BASE = {
    "ReplayBrowser.BgColor": "DkCard", "ReplayBrowser.Details.TitleEdit.Carat.FgColor": "DkAccent",
    "ReplayBrowser.Button.ArmedBgColor": "DkAccent", "ReplayBrowser.Button.DepressedBgColor": "DkAccent",
    "ReplayBrowser.CollectionTitle.FgColor": "DkAccent", "ReplayBrowser.Warning.FgColor": "DkText",
    "ReplayBrowser.ScrollBar.SliderButton.FgColor": "DkLine", "ReplayBrowser.Search.BgColor": "DkChip",
    "ReplayBrowser.Search.FgColor": "DkText", "Replay.RenderDialog.BgColor": "DkCard",
    "Econ.Dialog.BgColor": "Clear", "Econ.Button.BgColor": "DkChip", "Econ.Button.FgColor": "DkText",
    "Econ.Button.ArmedBgColor": "DkAccent", "Econ.Button.ArmedFgColor": "DkOnRed",
    "Econ.Button.DepressedBgColor": "DkAccent", "Econ.Button.DepressedFgColor": "DkOnRed",
    "Econ.Button.PresetDefaultColorFg": "DkText", "Econ.Button.PresetArmedColorFg": "DkOnRed",
    "Econ.Button.PresetDepressedColorFg": "DkOnRed", "Econ.Button.PresetDefaultColorBg": "DkChip",
    "Econ.Button.PresetArmedColorBg": "DkAccent", "Econ.Button.PresetDepressedColorBg": "DkAccent",
    "Border.Bright": "Clear", "Border.Dark": "DkLine", "Border.Selection": "DkAccent",
    "Button.TextColor": "DkText", "Button.BgColor": "DkChip", "Button.ArmedTextColor": "DkOnRed",
    "Button.ArmedBgColor": "DkAccent", "Button.SelectedTextColor": "DkOnRed", "Button.SelectedBgColor": "DkAccent",
    "Button.DepressedTextColor": "DkOnRed", "Button.DepressedBgColor": "DkAccent",
    "CheckButton.TextColor": "DkText", "CheckButton.SelectedTextColor": "DkText", "CheckButton.BgColor": "DkChip",
    "CheckButton.Border1": "DkLine", "CheckButton.Border2": "DkLine", "CheckButton.Check": "DkAccent",
    "CheckButton.HighlightFgColor": "DkText",
    "ComboBoxButton.ArrowColor": "DkTextMuted", "ComboBoxButton.ArmedArrowColor": "DkText",
    "ComboBoxButton.BgColor": "Clear", "ComboBoxButton.DisabledBgColor": "Clear",
    "Frame.BgColor": "DkCardSoft", "Frame.OutOfFocusBgColor": "DkCardSoft",
    "FrameGrip.Color1": "Clear", "FrameGrip.Color2": "Clear", "FrameTitleButton.FgColor": "Clear",
    "FrameTitleButton.BgColor": "Clear", "FrameTitleButton.DisabledFgColor": "Clear",
    "FrameTitleButton.DisabledBgColor": "Clear", "FrameSystemButton.FgColor": "Clear",
    "FrameSystemButton.BgColor": "Clear", "FrameTitleBar.TextColor": "DkText", "FrameTitleBar.BgColor": "Clear",
    "FrameTitleBar.DisabledTextColor": "DkTextMuted", "FrameTitleBar.DisabledBgColor": "Clear",
    "GraphPanel.FgColor": "DkAccent", "GraphPanel.BgColor": "DkCardSoft",
    "Label.TextDullColor": "DkTextMuted", "Label.TextColor": "DkText", "Label.TextBrightColor": "DkText",
    "Label.SelectedTextColor": "DkText", "Label.BgColor": "Clear", "Label.DisabledFgColor1": "Clear",
    "Label.DisabledFgColor2": "DkTextFaint",
    "ListPanel.TextColor": "DkText", "ListPanel.BgColor": "DkCardSoft", "ListPanel.SelectedTextColor": "DkOnRed",
    "ListPanel.SelectedBgColor": "DkAccent", "ListPanel.SelectedOutOfFocusBgColor": "DkChip",
    "ListPanel.EmptyListInfoTextColor": "DkTextMuted",
    "Menu.TextColor": "DkText", "Menu.BgColor": "DkCard", "Menu.ArmedTextColor": "DkOnRed", "Menu.ArmedBgColor": "DkAccent",
    "Chat.TypingText": "DkText", "Panel.FgColor": "DkTextMuted", "Panel.BgColor": "Clear", "HTML.BgColor": "Clear",
    "ProgressBar.FgColor": "DkText", "ProgressBar.BgColor": "DkChip",
    "CircularProgressBar.FgColor": "DkText", "CircularProgressBar.BgColor": "DkChip",
    "BuildingHealthBar.BgColor": "DkChip", "BuildingHealthBar.Health": "DkText", "BuildingHealthBar.LowHealth": "DkAccent",
    "PropertySheet.TextColor": "DkTextMuted", "PropertySheet.SelectedTextColor": "DkText",
    "RadioButton.TextColor": "DkText", "RadioButton.SelectedTextColor": "DkText",
    "RichText.TextColor": "DkText", "RichText.BgColor": "Clear", "RichText.SelectedTextColor": "DkOnRed",
    "RichText.SelectedBgColor": "DkAccent",
    "ScrollBarButton.FgColor": "DkTextMuted", "ScrollBarButton.BgColor": "Clear", "ScrollBarButton.ArmedFgColor": "DkText",
    "ScrollBarButton.ArmedBgColor": "Clear", "ScrollBarButton.DepressedFgColor": "DkText",
    "ScrollBarButton.DepressedBgColor": "Clear", "ScrollBarSlider.FgColor": "DkLine", "ScrollBarSlider.BgColor": "Clear",
    "SectionedListPanel.HeaderTextColor": "DkTextMuted", "SectionedListPanel.HeaderBgColor": "Clear",
    "SectionedListPanel.DividerColor": "DkLine", "SectionedListPanel.TextColor": "DkText",
    "SectionedListPanel.BrightTextColor": "DkText", "SectionedListPanel.BgColor": "DkCardGhost",
    "SectionedListPanel.SelectedTextColor": "DkOnRed", "SectionedListPanel.SelectedBgColor": "DkAccent",
    "SectionedListPanel.OutOfFocusSelectedTextColor": "DkText", "SectionedListPanel.OutOfFocusSelectedBgColor": "DkChip",
    "Slider.NobColor": "DkText", "Slider.TextColor": "DkTextMuted", "Slider.TrackColor": "DkChip",
    "Slider.DisabledTextColor1": "DkTextFaint", "Slider.DisabledTextColor2": "Clear",
    "TextEntry.TextColor": "DkText", "TextEntry.BgColor": "DkChip", "TextEntry.CursorColor": "DkAccent",
    "TextEntry.DisabledTextColor": "DkTextFaint", "TextEntry.DisabledBgColor": "DkCard",
    "TextEntry.SelectedTextColor": "DkOnRed", "TextEntry.SelectedBgColor": "DkAccent",
    "TextEntry.OutOfFocusSelectedBgColor": "DkChip", "TextEntry.FocusEdgeColor": "Clear",
    "ToggleButton.SelectedTextColor": "DkText", "Tooltip.TextColor": "DkText", "Tooltip.BgColor": "DkCard",
    "TreeView.BgColor": "DkCardSoft", "WizardSubPanel.BgColor": "Clear",
    "TimerProgress.Active": "DkText", "TimerProgress.InActive": "DkChip", "TimerProgress.Warning": "DkAccent",
    "HudObjectives.FgColor": "DkText", "HudObjectives.BgColor": "DkCard", "HudObjectives.BorderColor": "DkLine",
    "HudProgressBar.Active": "DkText", "HudProgressBar.InActive": "DkChip",
    "HudCaptureIcon.Active": "DkText", "HudCaptureIcon.InActive": "DkChip",
    "HudCaptureProgressBar.Active": "DkText", "HudCaptureProgressBar.InActive": "DkChip",
    "FgColor": "DkText", "BgColor": "DkCardSoft", "ViewportBG": "Clear",
    "TeamSpec": "DkTextMuted", "TeamRed": "DkRedText", "TeamBlue": "DkBluText",
    "MapDescriptionText": "DkText", "HudIcon_Green": "DkPositive", "HudIcon_Red": "DkAccent",
    "ItemColor": "DkText", "MenuColor": "DkTextMuted", "MenuBoxBg": "DkCard",
    "SelectionNumberFg": "DkTextMuted", "SelectionTextFg": "DkText", "SelectionEmptyBoxBg": "DkCardGhost",
    "SelectionBoxBg": "DkCard", "SelectionSelectedBoxBg": "DkChip",
    "HintMessageFg": "DkText", "HintMessageBg": "DkCard", "ProgressBarFg": "DkAccent", "VguiScreenCursor": "DkAccent",
}

# ----------------------------------------------------------------------------------------
# Fonts
# ----------------------------------------------------------------------------------------
KEEP_FONT_FAMILIES = {"marlett", "buttons", "buttonssc", "tfd", "team fortress", "courier new"}
FAMILY_FACTOR = {"tf2 build": 0.86, "tf2": 0.86, "tf2 secondary": 0.95, "verdana": 1.0, "tahoma": 1.0,
                 "arial": 1.0, "arial black": 0.95, "trebuchet ms": 1.0, "ocr a extended": 0.95, "ocra": 0.95,
                 "tf2 professor": 0.95, "helvetica": 1.0}
# legacy fonts that only live on light menu surfaces and act as titles -> serif
SERIF_TITLES = {"menumaintitle", "matchmakingdialogtitle", "matchmakingdialogsessionoptionstitle", "teammenubold",
                "scoreboardteamscorenew", "scoreboardteamnamelarge", "chalkboardtitle", "chalkboardtitlebig",
                "chalkboardtitlemedium", "queststickytext"}
SERIF_TEXT = {"chalkboardtext"}
FLAG_KEYS = ("dropshadow", "outline", "blur", "additive", "italic", "underline", "scanlines", "rotary", "symbol")


def legacy_font_entry(name, entries):
    """entries: list of child nodes ("1", "2", ...). Returns (family, weight, tall, flags) or None (keep)."""
    first = None
    chosen = None
    for e in entries:
        if not isinstance(e[1], list) or (e[2] and "X360" in e[2]):
            continue
        kv = {k.lower(): v for k, v, c, cm in e[1] if not isinstance(v, list) and not (c and "X360" in c)}
        if first is None:
            first = kv
        yres = kv.get("yres")
        if yres:
            lo, hi = (int(x) for x in yres.split()[:2])
            if lo <= 1080 <= hi:
                chosen = dict(kv)
                chosen["tall"] = str(float(kv.get("tall", "10")) * 480 / 1080)
        elif chosen is None or "yres" in chosen:
            if "yres" not in kv:
                chosen = kv if chosen is None or chosen.get("yres") else chosen
    kv = chosen or first
    if kv is None:
        return None
    fam = kv.get("name", "").lower()
    if fam in KEEP_FONT_FAMILIES or not fam:
        return None
    try:
        tall = float(kv.get("tall", "10"))
    except ValueError:
        tall = 10.0
    weight = int(kv.get("weight", "400") or 400)
    lname = name.lower()
    if lname in SERIF_TITLES:
        fam_w = T.SERIF_DISPLAY if tall >= 20 else T.SERIF_SEMI
    elif lname in SERIF_TEXT or fam == "tf2 professor":
        fam_w = T.SERIF
    elif fam in ("tf2 build", "tf2"):
        fam_w = T.SANS_SEMI
    elif weight >= 600 or "bold" in lname:
        fam_w = T.SANS_MED
    else:
        fam_w = T.SANS
    new_tall = max(5, int(round(tall * FAMILY_FACTOR.get(fam, 1.0))))
    flags = {k: kv[k] for k in FLAG_KEYS if k in kv and kv[k] not in ("0", "")}
    return fam_w[0], fam_w[1], new_tall, flags


def font_block(family, weight, tall, flags=None, comment=None):
    entry = [["name", family, None, None], ["tall", str(tall), None, None],
             ["weight", str(weight), None, None], ["antialias", "1", None, None]]
    for k, v in (flags or {}).items():
        entry.append([k, v, None, None])
    if comment:
        entry[0][3] = comment
    return [["1", entry, None, None]]


# ----------------------------------------------------------------------------------------
# Borders
# ----------------------------------------------------------------------------------------
QUALITY_IMAGES = {"backpack_rect_color", "backpack_rect_mouseover_color", "backpack_rect_selected",
                  "backpack_rect", "backpack_rect_mouseover"}


def line_border(sides, color, thickness=1, inset="0 0 0 0", backgroundtype=None):
    nodes = [["inset", inset, None, None]]
    if backgroundtype is not None:
        nodes.append(["backgroundtype", str(backgroundtype), None, None])
    for side in ("Left", "Right", "Top", "Bottom"):
        lines = []
        for i in range(thickness if side in sides else 1):
            lines.append([str(i + 1), [["color", color if side in sides else "Clear", None, None],
                                       ["offset", "0 0", None, None]], None, None])
        nodes.append([side, lines, None, None])
    return nodes


FLAT_ROUND = [["inset", "0 0 0 0", None, None], ["backgroundtype", "2", None, None]]
FLAT_SQUARE = [["inset", "0 0 0 0", None, None], ["backgroundtype", "0", None, None]]

NEW_BORDERS = [
    ("ClCard", FLAT_ROUND, "superficie piena arrotondata: il colore viene dal bgcolor del pannello"),
    ("ClSquare", FLAT_SQUARE, "superficie piena squadrata (barre, filetti, pannelli < 12 unita')"),
    ("ClInputDk", line_border(("Left", "Right", "Top", "Bottom"), "DkLine"), "campo di input su scuro (unico contorno ammesso)"),
    ("ClInputLt", line_border(("Left", "Right", "Top", "Bottom"), "LtLineStrong"), "campo di input su chiaro (unico contorno ammesso)"),
    ("ClInputFocus", line_border(("Left", "Right", "Top", "Bottom"), "DkAccent"), "campo di input con focus"),
    ("ClMarkDk", line_border(("Left",), "DkAccent", thickness=3), "il Segno: barra terracotta a sinistra (scuro)"),
    ("ClMarkLt", line_border(("Left",), "LtAccent", thickness=3), "il Segno: barra terracotta a sinistra (chiaro)"),
    ("ClRuleDk", line_border(("Bottom",), "DkLine"), "filetto inferiore su scuro"),
    ("ClRuleLt", line_border(("Bottom",), "LtLine"), "filetto inferiore su chiaro"),
    ("ClUnderlineLt", line_border(("Bottom",), "LtAccent", thickness=2), "sottolineatura accento (voce attiva nei menu)"),
]
# legacy line borders that framed cards -> flat cards (no outlines around surfaces)
FLATTEN_LINE_BORDERS = {"quickplayborder", "tooltipborder", "replayhighlightborder"}
# legacy borders used as hover/armed state on buttons -> the Segno
ARMED_BORDERS = {"mainmenubuttonarmed", "mainmenuminibuttonarmed", "econ.button.border.armed"}


def build_borders(legacy_nodes, report):
    out = []
    for name, nodes, note in NEW_BORDERS:
        n = [x[:] for x in nodes]
        out.append([name, n, None, None])
        if note:
            out[-1].append(None)
            out[-1] = out[-1][:4]
    out.append(["__comment__", "legacy", None, None])
    for name, body, cond, _ in legacy_nodes:
        if not isinstance(body, list):
            continue
        kv = {k.lower(): v for k, v, c, cm in body if not isinstance(v, list)}
        image = kv.get("image", "").lower()
        lname = name.lower()
        if image in QUALITY_IMAGES or lname.startswith("backpackitem"):
            out.append([name, body, cond, None])
            report.append(("border", name, "kept (cornice di qualita' oggetto)"))
        elif lname in ARMED_BORDERS:
            out.append([name, [x[:] for x in line_border(("Left",), "DkAccent", thickness=3, backgroundtype=2)], cond, None])
            report.append(("border", name, "-> Segno (hover)"))
        elif kv.get("bordertype") == "scalable_image" or lname in FLATTEN_LINE_BORDERS:
            out.append([name, [x[:] for x in FLAT_ROUND], cond, None])
            report.append(("border", name, "-> ClCard (piatto arrotondato)"))
        else:
            out.append([name, body, cond, None])  # line border: colours resolve through remapped legacy names
            report.append(("border", name, "kept (linee, colori rimappati)"))
    return out


# ----------------------------------------------------------------------------------------
def color_line(name, rgba, comment):
    return [name, "%d %d %d %d" % rgba, None, comment]


def parse_rgba(s):
    p = [int(float(x)) for x in s.split()]
    while len(p) < 4:
        p.append(255)
    return tuple(p[:4])


def build(report=None):
    report = [] if report is None else report
    src = vdf.parse(open(PRISTINE, encoding="utf-8", errors="replace").read())
    scheme = vdf.get(src, "Scheme")
    sections = {nd[0]: nd for nd in scheme if isinstance(nd[1], list)}

    # ---------------- Colors
    colors = []
    for role in T.ROLES:
        pal, a = T.ROLES[role]
        colors.append(color_line(role, T.rgba(role), "%s %s%s" % (pal, T.hexs(T.S[pal]), "" if a == 255 else " @%d%%" % round(a / 2.55))))
    # alpha variants requested by tools/migrate.py (<Token>A<percent>)
    import glob as _glob
    found = set()
    for pth in _glob.glob(os.path.join(ROOT, "resource", "**", "*.res"), recursive=True) + \
            _glob.glob(os.path.join(ROOT, "scripts", "**", "*.*"), recursive=True):
        if os.path.basename(pth) in ("clientscheme.res", "sourcescheme.res", "chatscheme.res"):
            continue
        found |= set(m.group(0) for m in re.finditer(r"\b(?:Dk|Lt)[A-Za-z]+A\d0\b|\bUntintedA\d0\b",
                                                         open(pth, encoding="utf-8", errors="replace").read()))
    if True:
        for vname in sorted(found):
            m = re.match(r"^(.*)A(\d0)$", vname)
            if not m or m.group(1) not in T.ROLES:
                continue
            r, g, b, _ = T.rgba(m.group(1))
            colors.append(color_line(vname, (r, g, b, int(round(int(m.group(2)) * 2.55))),
                                     "%s @%s%% (variante generata)" % (m.group(1), m.group(2))))
    legacy = []
    for name, val, cond, cm in sections["Colors"][1]:
        if isinstance(val, list):
            continue
        orig = parse_rgba(val)
        target = LEGACY_COLORS.get(name)
        if target is None:
            target = "keep" if name.startswith(KEEP_PREFIXES) else None
        if target is None:
            raise SystemExit("legacy colour %r has no mapping" % name)
        if target == "keep":
            legacy.append(color_line(name, orig, "semantica di gioco, invariato"))
        else:
            r, g, b, a = T.rgba(target)
            alpha = orig[3] if orig[3] < 255 else a
            legacy.append(color_line(name, (r, g, b, alpha), "legacy -> %s" % target))
    colors_node = ["Colors", colors + [["//", "", None, None]] + legacy, None, None]

    # ---------------- BaseSettings
    base = []
    seen = set()
    for key, val, cond, cm in sections["BaseSettings"][1]:
        if isinstance(val, list):
            continue
        if key in BASE:
            if key in seen and cond:
                continue
            base.append([key, BASE[key], None, None])
            seen.add(key)
        else:
            base.append([key, val, cond, cm])
    for key in BASE:
        if key not in seen and not any(b[0] == key for b in base):
            base.append([key, BASE[key], None, "ClaudeHUD"])

    # ---------------- Fonts
    fonts = []
    for name, (fw, tall, role) in T.TYPE.items():
        fonts.append([name, font_block(fw[0], fw[1], tall, getattr(T, "TYPE_FLAGS", {}).get(name), comment="ClaudeHUD: " + role), None, None])
    for name, body, cond, _ in sections["Fonts"][1]:
        if not isinstance(body, list):
            continue
        m = legacy_font_entry(name, body)
        if m is None:
            fonts.append([name, body, cond, None])
            report.append(("font", name, "kept (font di icone/sistema)"))
        else:
            fam, w, tall, flags = m
            fonts.append([name, font_block(fam, w, tall, flags, comment="legacy -> %s %d" % (fam, tall)), cond, None])
            report.append(("font", name, "-> %s %d" % (fam, tall)))

    # ---------------- Borders
    borders = build_borders(sections["Borders"][1], report)

    # ---------------- CustomFontFiles
    cff = [["1", "resource/tf.ttf", None, "icone di gioco (Team Fortress)"],
           ["2", "resource/tfd.ttf", None, "icone killfeed (tfd)"]]
    for i, (fname, family, weight, role) in enumerate(T.FONT_FILES):
        cff.append([str(3 + i), [["font", "resource/fonts/" + fname, None, None],
                                 ["name", family, None, "nome famiglia interno (name ID 1), non il nome file"]], None, None])
    for nd in sections["CustomFontFiles"][1]:
        if nd[0] in ("10", "11", "12", "13", "14", "15", "16", "17"):
            cff.append(nd)

    return [colors_node, ["BaseSettings", base, None, None],
            ["BitmapFontFiles", sections["BitmapFontFiles"][1], None, None],
            ["Fonts", fonts, None, None], ["Borders", borders, None, None],
            ["CustomFontFiles", cff, None, None]], report


HEADER = """//
// ClaudeHUD - ClientScheme
// GENERATED by tools/build_scheme.py from tools/tokens.py. Do not edit by hand:
// change the tokens and run `python3 tools/build_scheme.py`.
//
// Colors       Dk* = in-game (dark warm), Lt* = menus (light editorial). Legacy names keep
//              the game's C++ working and are remapped to the same tokens.
// Fonts        IBM Plex Sans (UI, combat numbers - tabular digits) / Source Serif 4 (menu titles)
// Borders      Cl* = ClaudeHUD primitives; legacy texture borders are flattened.
//
"""


def render(sections):
    lines = [HEADER.rstrip("\n"), "Scheme", "{"]
    for name, body, cond, cm in sections:
        lines.append("\t%s" % name)
        lines.append("\t{")
        chunk = []
        for nd in body:
            if nd[0] == "__comment__":
                chunk.append("\t\t// ---- legacy ----")
            elif nd[0] == "//":
                chunk.append("\t\t// ---- legacy names (used by the game's code) ----")
            else:
                chunk.append(vdf.dump([nd], 2, align=False))
        lines.append("\n".join(chunk))
        lines.append("\t}")
    lines.append("}")
    return "\n".join(lines) + "\n"


def main():
    sections, report = build()
    text = render(sections)
    vdf.parse(text)  # must round-trip
    with open(OUT, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    print("wrote %s (%d lines)" % (os.path.relpath(OUT, ROOT), text.count("\n")))
    if "--report" in sys.argv:
        for kind, name, what in report:
            print("%-6s %-40s %s" % (kind, name, what))


if __name__ == "__main__":
    main()


def swap_family(body, fw):
    """Deep copy of a font definition with every 'name' set to fw[0] and 'weight' to fw[1]."""
    import copy
    out = copy.deepcopy(body)
    for path, nd in vdf.walk(out):
        if isinstance(nd[1], list):
            continue
        if nd[0].lower() == "name":
            nd[1] = fw[0]
            nd[3] = "ClaudeHUD (struttura Valve invariata)"
        elif nd[0].lower() == "weight":
            nd[1] = str(fw[1])
    return out


# ========================================================================================
# Auxiliary schemes: SourceScheme (GameUI: options, server browser -> LIGHT) and
# ChatScheme (chat window -> DARK). Same tokens, same rules.
# ========================================================================================
AUX = {
    "resource/sourcescheme.res": "light",
    "resource/chatscheme.res": "dark",
}
AUX_EXPLICIT = {
    "dark": {"TFColors.ChatTextYellow": "DkText", "TFColors.ChatTextTeamBlue": "DkBluText",
             "TFColors.ChatTextTeamRed": "DkRedText", "Chat.TypingText": "DkText", "Console.TextColor": "DkText",
             "Console.DevTextColor": "DkTextMuted", "Tooltip.TextColor": "DkText", "Tooltip.BgColor": "DkCard",
             "ListPanel.SelectedTextColor": "DkOnRed", "Menu.ArmedTextColor": "DkOnRed",
             "RichText.SelectedTextColor": "DkOnRed", "TextEntry.SelectedTextColor": "DkOnRed",
             "SectionedListPanel.SelectedTextColor": "DkOnRed", "SectionedListPanel.OutOfFocusSelectedTextColor": "DkText",
             "Frame.BgColor": "DkCardSoft", "Frame.OutOfFocusBgColor": "DkCardGhost", "Label.BgColor": "Clear",
             "RichText.BgColor": "Clear", "TextEntry.BgColor": "DkChip", "TextEntry.CursorColor": "DkAccent"},
    "light": {"Button.TextColor": "LtText", "Button.BgColor": "LtCardAlt", "Button.ArmedTextColor": "LtOnButtonHover",
              "Button.ArmedBgColor": "LtButtonHover", "Button.DepressedTextColor": "LtOnButton",
              "Button.DepressedBgColor": "LtButton", "Button.FocusBorderColor": "LtAccent",
              "Frame.BgColor": "LtCanvas", "Frame.OutOfFocusBgColor": "LtCanvas", "FrameTitleBar.TextColor": "LtText",
              "FrameTitleBar.DisabledTextColor": "LtTextMuted", "FrameTitleButton.FgColor": "LtTextMuted",
              "Label.TextColor": "LtText", "Label.TextBrightColor": "LtText", "Label.TextDullColor": "LtTextMuted",
              "Label.SelectedTextColor": "LtText", "Label.DisabledFgColor1": "LtTextFaint", "Label.DisabledFgColor2": "Clear",
              "ListPanel.TextColor": "LtText", "ListPanel.BgColor": "LtCard", "ListPanel.SelectedBgColor": "LtButtonHover",
              "ListPanel.SelectedOutOfFocusBgColor": "LtCardPressed", "ListPanel.SelectedTextColor": "LtOnButtonHover",
              "Menu.FgColor": "LtText", "Menu.BgColor": "LtCard", "Menu.ArmedFgColor": "LtOnButtonHover",
              "Menu.ArmedBgColor": "LtButtonHover", "Menu.DividerColor": "LtLine", "MainMenu.TextColor": "LtText",
              "MainMenu.ArmedTextColor": "LtAccentText", "CheckButton.TextColor": "LtText",
              "CheckButton.SelectedTextColor": "LtText", "CheckButton.BgColor": "LtCard", "CheckButton.Check": "LtAccent",
              "CheckButton.HighlightFgColor": "LtTextMuted", "CheckButton.DisabledBgColor": "LtCardAlt",
              "ToggleButton.SelectedTextColor": "LtText", "ComboBoxButton.ArrowColor": "LtTextMuted",
              "ComboBoxButton.ArmedArrowColor": "LtText", "RadioButton.TextColor": "LtText",
              "RadioButton.SelectedTextColor": "LtText", "RadioButton.ArmedTextColor": "LtAccentText",
              "ScrollBarButton.FgColor": "LtTextMuted", "ScrollBarButton.BgColor": "LtCardAlt",
              "ScrollBarButton.ArmedFgColor": "LtText", "ScrollBarButton.ArmedBgColor": "LtCardPressed",
              "ScrollBarButton.DepressedFgColor": "LtText", "ScrollBarButton.DepressedBgColor": "LtCardPressed",
              "ScrollBarSlider.BgColor": "LtCardAlt", "ScrollBarSlider.FgColor": "LtLineStrong",
              "Slider.NobColor": "LtText", "Slider.TextColor": "LtText", "Slider.TrackColor": "LtLine",
              "Slider.DisabledTextColor1": "LtTextFaint", "Slider.DisabledTextColor2": "Clear",
              "TextEntry.TextColor": "LtText", "TextEntry.DisabledTextColor": "LtTextFaint",
              "TextEntry.SelectedBgColor": "LtButtonHover", "Border.Bright": "LtLine", "Border.Dark": "LtLineStrong",
              "Border.Selection": "LtAccent"},
}


def _aux_role(key, value, colors_lit, mode):
    """Map a colour value of an auxiliary scheme to a token name, or None (not a colour)."""
    k = key.lower()
    if re.match(r"^\s*\d+\s+\d+\s+\d+", value):
        rgba = parse_rgba(value)
    elif value.lower() in colors_lit:
        rgba = colors_lit[value.lower()]
    else:
        return None
    import migrate as Mg
    cat = "bg" if any(x in k for x in ("bgcolor", "fill", "backdrop", "track", "border")) else "fg"
    role = Mg.nearest_role(rgba[:3])
    token = Mg.ROLE_MAP[mode][cat][role]
    if rgba[3] <= 6:
        return "Clear"
    if rgba[3] < 200 and cat == "bg":
        token = {"dark": "DkCardSoft", "light": "LtCardAlt"}[mode]
    return token


def build_aux(rel, mode):
    pristine = os.path.join(ROOT, "#TF2 Files", rel)
    src = vdf.parse(open(pristine, encoding="utf-8", errors="replace").read())
    head = [nd for nd in src if nd[0] == "#base"]
    scheme = vdf.get(src, "Scheme")
    secs = {nd[0]: nd for nd in scheme if isinstance(nd[1], list)}
    prefix = "Dk" if mode == "dark" else "Lt"
    colors = [color_line(r, T.rgba(r), "token") for r in T.ROLES if r.startswith(prefix) or r in ("Clear", "Untinted")]
    colors_lit = {}
    for k, v, c, cm in (secs.get("Colors", [None, []])[1]):
        if not isinstance(v, list):
            colors_lit[k.lower()] = parse_rgba(v)
    legacy = []
    for k, v, c, cm in (secs.get("Colors", [None, []])[1]):
        if isinstance(v, list):
            continue
        tok = _aux_role(k, v, colors_lit, mode) or "Clear"
        legacy.append(color_line(k, T.rgba(tok)[:3] + (min(T.rgba(tok)[3], colors_lit[k.lower()][3]) if tok != "Clear" else 0,), "legacy -> " + tok))
    base = []
    explicit = AUX_EXPLICIT[mode]
    seen = set()
    for k, v, c, cm in (secs.get("BaseSettings", [None, []])[1]):
        if isinstance(v, list):
            continue
        if k in explicit:
            if k in seen:
                continue
            seen.add(k)
            base.append([k, explicit[k], None, None])
            continue
        if any(b[0] == k and b[2] == c for b in base):
            continue  # Valve's original repeats a few keys with the same condition: keep the first
        tok = _aux_role(k, v, colors_lit, mode)
        base.append([k, tok if tok else v, c, cm])
    for k, tok in explicit.items():
        if k not in seen and not any(b[0] == k for b in base):
            base.append([k, tok, None, "ClaudeHUD"])
    fonts = []
    if mode == "light":
        # GameUI fonts: same structure as Valve's definition (yres variants in pixels), new family
        base_src = vdf.parse(open(os.path.join(ROOT, "#Platform Files", "resource", "sourceschemebase.res"),
                                  encoding="utf-8", errors="replace").read())
        base_fonts = {k: (v, c) for k, v, c, cm in vdf.get(vdf.get(base_src, "Scheme"), "Fonts") if isinstance(v, list)}
        for k, v, c, cm in secs.get("Fonts", [None, []])[1]:
            if isinstance(v, list):
                base_fonts[k] = (v, c)  # TF2 overrides win
        gameui = {"Default": T.SANS, "DefaultBold": T.SANS_MED, "DefaultUnderline": T.SANS, "DefaultSmall": T.SANS,
                  "DefaultSmallDropShadow": T.SANS, "DefaultVerySmall": T.SANS, "DefaultLarge": T.SANS_MED,
                  "UiBold": T.SANS_MED, "MenuLarge": T.SANS_MED, "ChapterTitle": T.SERIF_DISPLAY,
                  "Trebuchet24": T.SERIF_SEMI, "Trebuchet20": T.SERIF_SEMI, "Trebuchet18": T.SANS_MED,
                  "TitleFont": T.SERIF_DISPLAY, "TitleFont2": T.SERIF_DISPLAY, "StatsTitle": T.SERIF_SEMI,
                  "StatsText": T.SANS, "StatsPageText": T.SANS, "AchievementTitleFont": T.SERIF_SEMI,
                  "AchievementTitleFontSmaller": T.SERIF_SEMI, "AchievementDescriptionFont": T.SANS,
                  "AchievementItemTitle": T.SANS_MED, "AchievementItemTitleLarge": T.SANS_MED,
                  "AchievementItemDescription": T.SANS, "AchievementItemDate": T.SANS, "MainMenuFont": T.SANS_MED,
                  "ServerBrowserTitle": T.SERIF_DISPLAY, "ServerBrowserSmall": T.SANS}
        for name, fw in gameui.items():
            if name not in base_fonts:
                continue
            body, cond = base_fonts[name]
            fonts.append([name, swap_family(body, fw), cond, None])
    else:
        for name, body, cond, _ in secs.get("Fonts", [None, []])[1]:
            if not isinstance(body, list):
                continue
            fam = ""
            for path, nd in vdf.walk(body):
                if nd[0].lower() == "name" and not isinstance(nd[1], list):
                    fam = nd[1].lower()
                    break
            if fam in KEEP_FONT_FAMILIES:
                fonts.append([name, body, cond, None])
            else:
                fonts.append([name, swap_family(body, T.SANS_MED if name == "ChatFont" else T.SANS), cond, None])
    borders = secs.get("Borders", [None, []])[1]
    cff = []
    for i, (fname, family, weight, role) in enumerate(T.FONT_FILES):
        cff.append([str(1 + i), [["font", "resource/fonts/" + fname, None, None], ["name", family, None, None]], None, None])
    for nd in secs.get("CustomFontFiles", [None, []])[1]:
        if nd[0] in ("10", "11", "12", "13", "14", "15", "16", "17"):
            cff.append(nd)
    sections = [["Colors", colors + [["//", "", None, None]] + legacy, None, None], ["BaseSettings", base, None, None],
                ["Fonts", fonts, None, None]]
    if borders:
        sections.append(["Borders", borders, None, None])
    sections.append(["CustomFontFiles", cff, None, None])
    text = render(sections).replace("ClaudeHUD - ClientScheme", "ClaudeHUD - %s (%s)" % (os.path.basename(rel), mode))
    if head:
        text = "\n".join('#base "%s"' % nd[1] for nd in head) + "\n" + text
    vdf.parse(text)
    with open(os.path.join(ROOT, rel), "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    print("wrote %s (%s, %d lines)" % (rel, mode, text.count("\n")))


if __name__ == "__main__" and "--aux" in sys.argv:
    for rel, mode in AUX.items():
        build_aux(rel, mode)
