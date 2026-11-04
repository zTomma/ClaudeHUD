"""
ClaudeHUD — design tokens: the single source of truth.

Everything stylistic (colours, type, borders) is defined here and *generated* into
resource/clientscheme.res by tools/build_scheme.py. Nothing in this file is typed from
memory: every base colour is a pixel value sampled from the reference screenshots
(see SAMPLED[*]["source"]); every other colour is derived from sampled colours with an
explicit formula (DERIVED), so it can be recomputed and audited.

Run `python3 tools/contrast.py` to verify every text/background pair declared below.
"""

# --------------------------------------------------------------------------------------
# 1. Sampled palette (pixel values measured with tools/sample_reference.py)
# --------------------------------------------------------------------------------------
SAMPLED = {
    "Ivory":      {"rgb": (250, 249, 245), "source": "ref 5 (anthropic.com), page background, 91.6% of pixels"},
    "Pampas":     {"rgb": (244, 243, 238), "source": "ref 3, swatch labelled #F4F3EE"},
    "White":      {"rgb": (255, 255, 255), "source": "ref 3, swatch labelled #FFFFFF"},
    "Cloud":      {"rgb": (177, 173, 161), "source": "ref 3, swatch labelled #B1ADA1"},
    "Ink":        {"rgb": (20, 20, 19),    "source": "ref 5, body text and 'Try Claude' button fill"},
    "Terracotta": {"rgb": (217, 119, 87),  "source": "ref 3, swatch labelled #D97757; ref 5 blob (identical pixel)"},
    "Coral":      {"rgb": (225, 129, 102), "source": "ref 4, pixel mascot body"},
    "Blush":      {"rgb": (243, 198, 181), "source": "ref 4, light stripe at bottom"},
    "Sage":       {"rgb": (188, 210, 203), "source": "ref 2, right panel background"},
    "Green":      {"rgb": (81, 155, 134),  "source": "ref 4, dark green bar at bottom"},
    "Moss":       {"rgb": (100, 115, 107), "source": "ref 2, halftone dots (bottom right), modal value"},
    "Steel":      {"rgb": (16, 88, 137),   "source": "ref 4, mascot headphones"},
}


def _clamp(v):
    return max(0, min(255, int(round(v))))


def mix(a, b, t):
    """Linear interpolation in sRGB (the same space the game alpha-blends in)."""
    return tuple(_clamp(x * (1 - t) + y * t) for x, y in zip(a, b))


def srgb_to_lin(c):
    c = c / 255.0
    return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4


def luminance(rgb):
    r, g, b = (srgb_to_lin(c) for c in rgb)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def contrast(a, b):
    la, lb = luminance(a), luminance(b)
    hi, lo = max(la, lb), min(la, lb)
    return (hi + 0.05) / (lo + 0.05)


def composite(fg_rgb, alpha, backdrop):
    """Colour seen on screen when fg is drawn with alpha (0..1) over backdrop."""
    return mix(backdrop, fg_rgb, alpha)


def solve_mix(a, b, against, target, step=0.01):
    """Smallest t in [0,1] such that contrast(mix(a,b,t), every bg in against) >= target."""
    t = 0.0
    while t <= 1.0 + 1e-9:
        c = mix(a, b, t)
        if all(contrast(c, bg) >= target for bg in against):
            return round(t, 2), c
        t += step
    raise ValueError("unreachable target")


S = {k: v["rgb"] for k, v in SAMPLED.items()}

# --------------------------------------------------------------------------------------
# 2. Derived colours (formula -> value). Order matters: later ones may use earlier ones.
# --------------------------------------------------------------------------------------
DERIVED = {}


def _derive(name, formula, rgb):
    DERIVED[name] = {"rgb": rgb, "formula": formula}
    S[name] = rgb


# Warm dark surfaces: Ink lifted toward the warm grey Cloud (no pure black anywhere).
_derive("Ink2", "mix(Ink, Cloud, 0.12)", mix(S["Ink"], S["Cloud"], 0.12))
_derive("Ink3", "mix(Ink, Cloud, 0.22)", mix(S["Ink"], S["Cloud"], 0.22))
_derive("InkLine", "mix(Ink, Cloud, 0.36)", mix(S["Ink"], S["Cloud"], 0.36))
# Local-player highlight surface: Ink warmed with a little Terracotta.
_derive("InkWarm", "mix(Ink, Terracotta, 0.16)", mix(S["Ink"], S["Terracotta"], 0.16))
# Muted text on light surfaces: Cloud darkened toward Ink until >= 4.5:1 on Pampas and Ivory.
_t, _c = solve_mix(S["Cloud"], S["Ink"], [S["Pampas"], S["Ivory"], S["White"]], 4.6)
_derive("CloudDeep", "mix(Cloud, Ink, %.2f)  [solved: >=4.6:1 on Pampas/Ivory/White]" % _t, _c)
# Accent / RED text on light surfaces: Terracotta darkened toward Ink until >= 4.5:1.
_t, _c = solve_mix(S["Terracotta"], S["Ink"], [S["Pampas"], S["Ivory"], S["White"]], 4.6)
_derive("TerracottaDeep", "mix(Terracotta, Ink, %.2f)  [solved: >=4.6:1 on Pampas/Ivory/White]" % _t, _c)
# BLU text on dark surfaces: Steel lightened toward Ivory until >= 4.6:1 on every dark surface.
_t, _c = solve_mix(S["Steel"], S["Ivory"], [S["Ink2"], S["Ink3"], S["InkWarm"]], 4.6)
_derive("SteelLight", "mix(Steel, Ivory, %.2f)  [solved: >=4.6:1 on Ink2/Ink3/InkWarm]" % _t, _c)
# Faint (disabled) text on dark: Cloud toward Ink2, kept >= 3:1 (non-essential text only).
_t, _c = solve_mix(S["Ink2"], S["Cloud"], [S["Ink2"]], 3.1)
_derive("CloudFaint", "mix(Ink2, Cloud, %.2f)  [solved: >=3.1:1 on Ink2, disabled text only]" % _t, _c)
# Faint (disabled) text on light.
_t, _c = solve_mix(S["Pampas"], S["Ink"], [S["Pampas"], S["Ivory"]], 3.1)
_derive("InkFaint", "mix(Pampas, Ink, %.2f)  [solved: >=3.1:1 on Pampas/Ivory, disabled text only]" % _t, _c)
# Hairlines on light surfaces (decorative, not text).
_derive("CloudLine", "mix(Ivory, Cloud, 0.55)", mix(S["Ivory"], S["Cloud"], 0.55))
# Pressed state on light buttons.
_derive("PampasDeep", "mix(Pampas, Cloud, 0.30)", mix(S["Pampas"], S["Cloud"], 0.30))

# --------------------------------------------------------------------------------------
# 3. Role tokens -> (palette colour, alpha 0..255). These names are what the .res files use.
#    Dk* = in-game (dark warm) mode, Lt* = menu (light editorial) mode.
# --------------------------------------------------------------------------------------
ROLES = {
    # ---- dark / in-game -------------------------------------------------------------
    "DkCard":          ("Ink2", 255),     # every combat card (opaque: contrast never depends on the map)
    "DkCardSoft":      ("Ink2", 232),     # chat and other non-combat overlays (91%: worst-case contrast >= 4.5)
    "DkCardGhost":     ("Ink2", 150),     # large dimming planes (spectator bars)
    "DkChip":          ("Ink3", 255),     # raised element inside a card, bar tracks
    "DkLine":          ("InkLine", 255),  # hairlines / dividers
    "DkCardLocal":     ("InkWarm", 255),  # local-player rows (killfeed)
    "DkText":          ("Ivory", 255),
    "DkTextMuted":     ("Cloud", 255),
    "DkTextFaint":     ("CloudFaint", 255),
    "DkAccent":        ("Terracotta", 255),
    "DkAccentSoft":    ("Terracotta", 96),
    "DkPositive":      ("Sage", 255),
    "DkPositiveFill":  ("Green", 255),
    "DkInfo":          ("SteelLight", 255),
    "DkRedText":       ("Terracotta", 255),
    "DkBluText":       ("SteelLight", 255),
    "DkRedFill":       ("Terracotta", 255),
    "DkBluFill":       ("Steel", 255),
    "DkOnRed":         ("Ink", 255),
    "DkOnBlu":         ("Ivory", 255),
    "DkScrim":         ("Ink", 160),
    # ---- light / menus --------------------------------------------------------------
    "LtCanvas":        ("Ivory", 255),
    "LtCanvasVeil":    ("Ivory", 236),    # canvas drawn over the 3D background
    "LtCard":          ("White", 255),
    "LtCardAlt":       ("Pampas", 255),
    "LtCardPressed":   ("PampasDeep", 255),
    "LtLine":          ("CloudLine", 255),
    "LtLineStrong":    ("Cloud", 255),
    "LtText":          ("Ink", 255),
    "LtTextMuted":     ("CloudDeep", 255),
    "LtTextFaint":     ("InkFaint", 255),
    "LtAccent":        ("Terracotta", 255),  # fills, markers, focus bars - never small text
    "LtAccentText":    ("TerracottaDeep", 255),
    "LtRedText":       ("TerracottaDeep", 255),
    "LtBluText":       ("Steel", 255),
    "LtRedFill":       ("Terracotta", 255),
    "LtBluFill":       ("Steel", 255),
    "LtOnRed":         ("Ink", 255),
    "LtOnBlu":         ("Ivory", 255),
    "LtButton":        ("Ink", 255),
    "LtOnButton":      ("Ivory", 255),
    "LtButtonHover":   ("Terracotta", 255),
    "LtOnButtonHover": ("Ink", 255),
    "LtPositive":      ("Green", 255),
    "LtScrim":         ("Ink", 110),
    # ---- shared ---------------------------------------------------------------------
    "Untinted":        ("White", 255),   # image tint that leaves game textures untouched
    "Clear":           ("Ink", 0),       # fully transparent
}

# --------------------------------------------------------------------------------------
# 4. Contrast contracts: every text/background pair the HUD uses, with its minimum ratio.
#    (fg_role, bg_role, min_ratio, note). bg alpha < 255 is checked against a worst-case
#    white AND black backdrop (the game world can be anything behind a translucent card).
# --------------------------------------------------------------------------------------
TEXT_MIN = 4.5          # body / UI text
LARGE_MIN = 3.0         # numbers >= 18 units tall and bold, icons
FAINT_MIN = 3.0         # disabled text only

CONTRACTS = [
    # dark mode
    ("DkText", "DkCard", 7.0, "numeri di combattimento, testo primario"),
    ("DkText", "DkChip", 7.0, "testo su chip"),
    ("DkText", "DkCardLocal", 7.0, "killfeed locale"),
    ("DkText", "DkCardSoft", TEXT_MIN, "chat (card traslucida, sfondo peggiore)"),
    ("DkTextMuted", "DkCard", TEXT_MIN, "etichette, riserva munizioni"),
    ("DkTextMuted", "DkChip", TEXT_MIN, "etichette su chip"),
    ("DkTextMuted", "DkCardSoft", TEXT_MIN, "testo secondario chat"),
    ("DkTextFaint", "DkCard", FAINT_MIN, "solo stati disabilitati"),
    ("DkAccent", "DkCard", TEXT_MIN, "pericolo: salute/munizioni basse"),
    ("DkAccent", "DkCardLocal", TEXT_MIN, "accento su riga locale"),
    ("DkPositive", "DkCard", TEXT_MIN, "overheal / buff"),
    ("DkInfo", "DkCard", TEXT_MIN, "informazioni neutre"),
    ("DkRedText", "DkCard", TEXT_MIN, "nome RED su card"),
    ("DkBluText", "DkCard", TEXT_MIN, "nome BLU su card"),
    ("DkRedText", "DkCardLocal", TEXT_MIN, "nome RED su riga locale"),
    ("DkBluText", "DkCardLocal", TEXT_MIN, "nome BLU su riga locale"),
    ("DkOnRed", "DkRedFill", TEXT_MIN, "testo su fascia RED"),
    ("DkOnBlu", "DkBluFill", TEXT_MIN, "testo su fascia BLU"),
    # light mode
    ("LtText", "LtCanvas", 7.0, "testo primario menu"),
    ("LtText", "LtCard", 7.0, "testo su card"),
    ("LtText", "LtCardAlt", 7.0, "testo su card secondaria"),
    ("LtText", "LtCardPressed", TEXT_MIN, "testo su bottone premuto"),
    ("LtTextMuted", "LtCanvas", TEXT_MIN, "testo secondario"),
    ("LtTextMuted", "LtCard", TEXT_MIN, "testo secondario su card"),
    ("LtTextMuted", "LtCardAlt", TEXT_MIN, "testo secondario su card secondaria"),
    ("LtTextFaint", "LtCardAlt", FAINT_MIN, "solo stati disabilitati"),
    ("LtAccentText", "LtCanvas", TEXT_MIN, "accento come testo"),
    ("LtAccentText", "LtCardAlt", TEXT_MIN, "accento come testo su card"),
    ("LtRedText", "LtCard", TEXT_MIN, "nome RED su scoreboard"),
    ("LtBluText", "LtCard", TEXT_MIN, "nome BLU su scoreboard"),
    ("LtRedText", "LtCardAlt", TEXT_MIN, "nome RED su riga alternata"),
    ("LtBluText", "LtCardAlt", TEXT_MIN, "nome BLU su riga alternata"),
    ("LtOnRed", "LtRedFill", TEXT_MIN, "testo su fascia RED"),
    ("LtOnBlu", "LtBluFill", TEXT_MIN, "testo su fascia BLU"),
    ("LtOnButton", "LtButton", 7.0, "bottone primario"),
    ("LtOnButtonHover", "LtButtonHover", TEXT_MIN, "bottone primario in hover"),
    ("LtPositive", "LtCard", LARGE_MIN, "icone/stati positivi"),
]

# Team pairs that must stay distinguishable (also under colour-vision deficiency).
TEAM_PAIRS = [
    ("DkRedText", "DkBluText", "nomi su card scura"),
    ("DkRedFill", "DkBluFill", "fasce/riempimenti"),
    ("LtRedText", "LtBluText", "nomi su card chiara"),
]

# --------------------------------------------------------------------------------------
# 5. Typography
# --------------------------------------------------------------------------------------
# Family names are the *internal* legacy family names (OpenType name ID 1) read from the
# files with fontTools - NOT the file names. tools/check_fonts.py re-verifies them.
FONT_FILES = [
    # (file in resource/fonts, internal family (nameID 1), weight to request, role)
    ("IBMPlexSans-Regular.ttf",  "IBM Plex Sans",       400, "UI testo"),
    ("IBMPlexSans-Medium.ttf",   "IBM Plex Sans Medm",  500, "UI enfasi, etichette"),
    ("IBMPlexSans-SemiBold.ttf", "IBM Plex Sans SmBld", 600, "numeri di combattimento"),
    ("SourceSerif4-Regular.ttf", "Source Serif 4",      400, "serif testo lungo"),
    ("SourceSerif4-Semibold.ttf", "Source Serif 4 Semibold", 600, "titoli, numeri grandi nei menu"),
    ("SourceSerif4Display-Semibold.ttf", "Source Serif 4 Display Semibold", 600, "titoli display (>= 20)"),
]

SANS = ("IBM Plex Sans", 400)
SANS_MED = ("IBM Plex Sans Medm", 500)
SANS_SEMI = ("IBM Plex Sans SmBld", 600)
SERIF = ("Source Serif 4", 400)
SERIF_SEMI = ("Source Serif 4 Semibold", 600)
SERIF_DISPLAY = ("Source Serif 4 Display Semibold", 600)

# Type scale (tall in 480-line proportional units; the engine scales by screen height).
TYPE = {
    # name           (family, weight), tall, role
    "TypeDisplay":   (SERIF_DISPLAY, 34, "titolo menu principale"),
    "TypeTitle":     (SERIF_DISPLAY, 24, "titoli di schermata (classe, team, scoreboard)"),
    "TypeHeading":   (SERIF_SEMI, 16, "titoli di sezione"),
    "TypeSerifNum":  (SERIF_SEMI, 20, "numeri grandi nei menu (punteggi)"),
    "TypeSerifBody": (SERIF, 11, "testo editoriale"),
    "TypeBodyL":     (SANS, 11, "testo UI grande"),
    "TypeBody":      (SANS, 9, "testo UI"),
    "TypeBodyStrong": (SANS_MED, 9, "testo UI in evidenza, bottoni"),
    "TypeCaption":   (SANS, 8, "didascalie"),
    "TypeLabel":     (SANS_MED, 7, "micro-etichette maiuscole"),
    "NumXL":         (SANS_SEMI, 26, "salute, caricatore"),
    "NumL":          (SANS_SEMI, 18, "timer di round, carica"),
    "NumM":          (SANS_SEMI, 13, "riserva, metallo, contatori"),
    "NumS":          (SANS_SEMI, 10, "numeri piccoli in card"),
    "NumXS":         (SANS_MED, 8, "micro-numeri"),
}

# --------------------------------------------------------------------------------------
# 6. Grid
# --------------------------------------------------------------------------------------
UNIT = 4                      # every position/size is a multiple of 4 (half-unit 2 only for insets)
SPACING = [2, 4, 8, 12, 16, 24, 32, 48]
EDGE = 12                     # distance of combat cards from the screen edge
CARD_PAD = 4                  # inner padding of a combat card
MENU_PAD = 16                 # inner padding of a menu card


def rgba(role):
    pal, a = ROLES[role]
    r, g, b = S[pal]
    return (r, g, b, a)


def rgba_str(role):
    return "%d %d %d %d" % rgba(role)


def hexs(rgb):
    return "#%02X%02X%02X" % tuple(rgb[:3])
