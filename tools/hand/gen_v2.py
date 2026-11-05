#!/usr/bin/env python3
"""
ClaudeHUD v2 - "taccuino vivace" (lively notebook). Applied on top of the v1 hand-written files, after
every other generator (build.py runs gen_* in alphabetical order). Idempotent: every element it owns is
named ClaudeV2* and is removed and re-added on each run.

Adds (DESIGN.md par. 11):
  * offset 'sticker' shadows behind every combat card (Moss; state colours come from the animations)
    and behind the cards of the light pages (ink / terracotta / sage / steel)
  * grid paper on the light pages (ref 2), brand stripes at the bottom of the menus (ref 4)
  * giant serif title with a blush highlighter, a kicker and a halftone of Plex bullets
  * the "Personalizza" menu: crosshair, hit sounds, damage numbers, HUD options - plain console
    variables verified in the TF2 client source, run through the main menu's "engine" command path
"""
import os
import re
import sys

from PIL import ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, os.path.dirname(HERE))
import migrate as M  # noqa: E402
import tokens as T  # noqa: E402
import vdf  # noqa: E402

P = "ClaudeV2"
FILE_OF = {f[1]: f[0] for f in T.FONT_FILES}


# ------------------------------------------------------------------------------------------ io
def load(rel):
    text = open(os.path.join(ROOT, rel), encoding="utf-8").read()
    lines = text.split("\n")
    head = []
    for l in lines:
        if l.startswith("//") or l.lower().startswith("#base") or not l.strip():
            head.append(l)
        else:
            break
    nodes = vdf.parse(text)
    return [l for l in head if l.startswith("//")], [l for l in head if l.lower().startswith("#base")], nodes


def save(rel, comments, bases, nodes):
    root = next(nd for nd in nodes if isinstance(nd[1], list))
    M.sanitize(nodes)
    note = "// ClaudeHUD v2 (taccuino vivace): elementi ClaudeV2* aggiunti da tools/hand/gen_v2.py"
    comments = [c for c in comments if "ClaudeHUD v2" not in c] + [note]
    out = "\n".join(comments) + "\n" + ("\n".join('#base "%s"' % b.split('"')[1] for b in bases) + "\n" if bases else "")
    out += vdf.dump([root]) + "\n"
    assert M.HAND_MARK in out[:400], rel
    vdf.parse(out)
    open(os.path.join(ROOT, rel), "w", encoding="utf-8", newline="\n").write(out)


def root_of(nodes):
    return next(nd[1] for nd in nodes if isinstance(nd[1], list))


def strip_v2(body):
    body[:] = [nd for nd in body if not (isinstance(nd[1], list) and nd[0].startswith(P))]
    for nd in body:
        if isinstance(nd[1], list):
            strip_v2(nd[1])


def find(body, name):
    for nd in body:
        if isinstance(nd[1], list) and nd[0].lower() == name.lower():
            return nd[1]
    raise KeyError(name)


def setkv(body, **kv):
    for k, v in kv.items():
        vdf.set_value(body, k, str(v))


def block(name, ctl, items):
    nodes = [["ControlName", ctl, None, None], ["fieldName", name, None, None]]
    nodes += [[k, str(v), None, None] for k, v in items]
    return [name, nodes, None, None]


def shadow(name, x, y, w, t, role, z):
    return block(name, "EditablePanel", [("xpos", x), ("ypos", y), ("zpos", z), ("wide", w), ("tall", t),
                                         ("visible", 1), ("enabled", 1), ("mouseinputenabled", 0),
                                         ("paintbackground", 1), ("paintbackgroundtype", 2), ("bgcolor_override", role)])


def line(name, x, y, w, t, role, z):
    return block(name, "ImagePanel", [("xpos", x), ("ypos", y), ("zpos", z), ("wide", w), ("tall", t),
                                      ("visible", 1), ("enabled", 1), ("mouseinputenabled", 0), ("fillcolor", role)])


def label(name, text, x, y, w, t, font, color, z, align="west", **extra):
    items = [("xpos", x), ("ypos", y), ("zpos", z), ("wide", w), ("tall", t), ("visible", 1), ("enabled", 1),
             ("mouseinputenabled", 0), ("labelText", text), ("textAlignment", align), ("font", font), ("fgcolor", color)]
    items += list(extra.items())
    return block(name, "CExLabel", items)


def chip(name, text, x, y, w, t, command, z, swatch=None):
    items = [("xpos", x), ("ypos", y), ("zpos", z), ("wide", w), ("tall", t), ("visible", 1), ("enabled", 1),
             ("labelText", text), ("textAlignment", "center"), ("font", "TypeCaption"), ("command", command),
             ("sound_depressed", "UI/buttonclick.wav"), ("paintbackground", 1), ("paintbackgroundtype", 2)]
    if swatch:
        items += [("defaultBgColor_override", swatch), ("armedBgColor_override", swatch),
                  ("depressedBgColor_override", swatch), ("border_default", "ClInputLt"), ("border_armed", "ClInputFocus")]
    else:
        items += [("defaultBgColor_override", "LtCardAlt"), ("defaultFgColor_override", "LtText"),
                  ("armedBgColor_override", "LtButtonHover"), ("armedFgColor_override", "LtOnButtonHover"),
                  ("depressedBgColor_override", "LtButton"), ("depressedFgColor_override", "LtOnButton")]
    return block(name, "CExButton", items)


def offset(v, d):
    v = str(v)
    if re.fullmatch(r"-?\d+", v):
        return str(int(v) + d)
    m = re.fullmatch(r"r(-?\d+)", v)
    if m:
        return "r%d" % (int(m.group(1)) - d)
    m = re.fullmatch(r"c(-?\d+)", v)
    if m:
        return "c%d" % (int(m.group(1)) + d)
    return "%s+%d" % (v, d)


def text_width_units(s, token):
    (fam, _w), tall, _r = T.TYPE[token]
    cell = 1.371 if fam.startswith("Source") else 1.300
    f = ImageFont.truetype(os.path.join(ROOT, "resource", "fonts", FILE_OF[fam]), 1000)
    return f.getlength(s) / 1000 * (tall / cell)


def edit(rel, fn):
    comments, bases, nodes = load(rel)
    body = root_of(nodes)
    strip_v2(body)
    fn(body)
    save(rel, comments, bases, nodes)


# ------------------------------------------------------------------------------------------ combat cards
SH = 3  # shadow offset (units)

edit("resource/ui/hudplayerhealth.res", lambda b: b.append(shadow(P + "HealthShadow", SH, 28 + SH, 88, 36, "DkShadow", 0)))
edit("resource/ui/hudammoweapons.res", lambda b: b.append(shadow(P + "AmmoShadow", SH, SH, 88, 36, "DkShadow", -1)))
edit("resource/ui/hudmediccharge.res", lambda b: b.append(shadow(P + "MedicShadow", SH, SH, 88, 36, "DkShadow", -2)))
edit("resource/ui/huddemomanpipes.res", lambda b: b.append(shadow(P + "PipesShadow", SH, SH, 80, 36, "DkShadow", -2)))
edit("resource/ui/hudaccountpanel.res", lambda b: b.append(shadow(P + "MetalShadow", 5 + SH, 103 + SH, 88, 36, "DkShadow", -2)))
edit("resource/ui/hudobjectivetimepanel.res", lambda b: b.append(shadow(P + "TimeShadow", SH, SH, 80, 28, "DkShadow", 0)))
edit("resource/ui/disguisestatuspanel.res", lambda b: b.append(shadow(P + "DisguiseShadow", SH, SH, 176, 30, "DkShadow", -2)))
edit("resource/ui/hudobjectiveflagpanel.res",
     lambda b: b.append(shadow(P + "FlagShadow", "c%d" % (-112 + SH), "r%d" % (56 - SH), 224, 44, "DkShadow", -2)))
for f in sorted(os.listdir(os.path.join(ROOT, "resource", "ui"))):
    if f.startswith("huditemeffectmeter") and f.endswith(".res"):
        src = open(os.path.join(ROOT, "resource", "ui", f), encoding="utf-8").read()
        if "#base" not in src[:600]:
            edit("resource/ui/" + f, lambda b: b.append(shadow(P + "MeterShadow", SH, SH, 80, 36, "DkShadow", -2)))


def freeze(b):
    base = find(b, "FreezePanelBase")
    base.append(shadow(P + "KillerShadow", 8 + SH, 158 + SH, 256, 36, "DkShadow", -2))


edit("resource/ui/freezepanel_basic.res", freeze)


def win(b):
    bg = {k.lower(): v for k, v, c, cm in find(b, "WinPanelBGBorder") if not isinstance(v, list)}
    b.append(shadow(P + "WinShadow", offset(bg.get("xpos", "0"), SH), offset(bg.get("ypos", "0"), SH),
                    bg.get("wide", "300"), bg.get("tall", "185"), "DkShadow", -1))


edit("resource/ui/winpanel.res", win)


# ------------------------------------------------------------------------------------------ light pages
def grid(prefix, x0, y0, w, h, step, z):
    out = []
    i = 0
    x = x0
    while x <= x0 + w:
        out.append(line("%sGridV%02d" % (prefix, i), x, y0, 1, h, "LtGrid", z))
        x += step
        i += 1
    i = 0
    y = y0
    while y <= y0 + h:
        out.append(line("%sGridH%02d" % (prefix, i), x0, y, w if isinstance(w, int) else w, 1, "LtGrid", z))
        y += step
        i += 1
    return out


def fullscreen_grid(prefix, y0, y1, z):
    out = []
    for i, x in enumerate(range(0, 1137, 16)):
        out.append(line("%sGridV%02d" % (prefix, i), x, y0, 1, y1 - y0, "LtGrid", z))
    for i, y in enumerate(range(y0, y1 + 1, 16)):
        out.append(line("%sGridH%02d" % (prefix, i), 0, y, "f0", 1, "LtGrid", z))
    return out


def stripes(prefix, z):
    """The bottom stripes of the branding board (ref 4): mint band + green bar, terracotta band + blush bar."""
    return [line(prefix + "StripeMint", 0, 466, "f0", 4, "LtSage", z),
            line(prefix + "StripeGreen", 0, 467, 280, 2, "LtPositive", z),
            line(prefix + "StripeTerracotta", 0, 470, "f0", 10, "LtAccent", z),
            line(prefix + "StripeBlush", 280, 473, "f280", 4, "LtBlush", z)]


# ---- main menu ------------------------------------------------------------------------------------
RGB = {k: T.S[v] for k, v in (("Avorio", "Ivory"), ("Terracotta", "Terracotta"), ("Salvia", "Sage"),
                                ("Acciaio", "SteelLight"), ("Blush", "Blush"), ("Verde", "Green"))}
SWATCH_ROLE = {"Avorio": "LtCanvas", "Terracotta": "LtAccent", "Salvia": "LtSage", "Acciaio": "DkInfo",
               "Blush": "LtBlush", "Verde": "LtPositive"}


def custom_menu(b):
    X, Y, W, H = 8, 60, 300, 356           # card (centre-relative x)
    # below every popup of the main menu (MOTD_Panel z1, Notifications_Panel z10, item tooltip z100) and
    # above the canvas/grid/stripes (z -200 and lower) and the left column (z -50 and lower)
    z = -44
    b.append(shadow(P + "CustomShadow", "c%d" % (X + 4), Y + 4, W, H, "LtSage", z - 1))
    b.append(shadow(P + "CustomCard", "c%d" % X, Y, W, H, "LtCard", z))
    b.append(label(P + "CustomKicker", "ClaudeHUD", "c%d" % (X + 12), Y + 8, 120, 8, "TypeLabel", "LtAccentText", z + 1,
                   allcaps=1))
    b.append(label(P + "CustomTitle", "Personalizza", "c%d" % (X + 12), Y + 16, 200, 22, "TypeHeading", "LtText", z + 1))
    b.append(label(P + "CustomHalftone", "• " * 60, "c%d" % (X + W - 108), Y + 8, 96, 30, "TypeCaption", "DkShadow",
                   z + 1, wrap=1))
    b.append(line(P + "CustomRule", "c%d" % (X + 12), Y + 42, W - 24, 1, "LtLine", z + 1))
    cx0, lx = X + 68, X + 12              # chips start / row labels
    cw = W - 12 - 68                      # chips area width
    y = Y + 48
    rows = []

    def section(title):
        nonlocal y
        b.append(label(P + "Sec" + re.sub(r"\W", "", title), title, "c%d" % lx, y, 200, 10, "TypeLabel", "LtAccentText",
                       z + 1, allcaps=1))
        y += 12

    def row(key, title, chips, gap=3, swatch=False):
        nonlocal y
        if title:
            b.append(label(P + "Row" + key, title, "c%d" % lx, y, 54, 16, "TypeCaption", "LtTextMuted", z + 1))
        n = len(chips)
        w = int((cw - gap * (n - 1)) / n)
        for i, (text, cmd) in enumerate(chips):
            b.append(chip("%sChip%s%d" % (P, key, i), "" if swatch else text, "c%d" % (cx0 + i * (w + gap)), y, w, 16,
                          "engine " + cmd, z + 2, swatch=SWATCH_ROLE[text] if swatch else None))
        y += 20

    section("Mirino")
    row("XStyle", "Stile", [(str(i), "cl_crosshair_file crosshair%d" % i) for i in range(1, 8)] + [("Off", "crosshair 0")])
    row("XColor", "Colore", [(n, "crosshair 1; cl_crosshair_red %d; cl_crosshair_green %d; cl_crosshair_blue %d" % RGB[n])
                             for n in RGB], gap=4, swatch=True)
    row("XSize", "Taglia", [("S", "cl_crosshair_scale 24"), ("M", "cl_crosshair_scale 32"),
                            ("L", "cl_crosshair_scale 40"), ("XL", "cl_crosshair_scale 48")])
    y += 2
    section("Indicatori di danno")
    sounds = ["Ding", "Elettro", "Note", "Percuss.", "Retro", "Spazio", "Beepo", "Vortice", "Squash"]
    row("Hit1", "Suono colpo", [("Off", "tf_dingalingaling 0")] +
        [(s, "tf_dingalingaling 1; tf_dingalingaling_effect %d" % i) for i, s in enumerate(sounds[:4])])
    row("Hit2", "", [(s, "tf_dingalingaling 1; tf_dingalingaling_effect %d" % (i + 4)) for i, s in enumerate(sounds[4:])])
    row("Kill", "Uccisione", [("Off", "tf_dingalingaling_lasthit 0"), ("On", "tf_dingalingaling_lasthit 1")])
    row("Num", "Numeri", [("Off", "hud_combattext 0"), ("On", "hud_combattext 1"),
                          ("Gruppi", "hud_combattext 1; hud_combattext_batching 1"),
                          ("Singoli", "hud_combattext 1; hud_combattext_batching 0")])
    row("Heal", "Cure", [("Off", "hud_combattext_healing 0"), ("On", "hud_combattext_healing 1")])
    row("NColor", "Colore", [(n, "hud_combattext_red %d; hud_combattext_green %d; hud_combattext_blue %d" % RGB[n])
                             for n in RGB], gap=4, swatch=True)
    y += 2
    section("Hud")
    row("Ping", "Ping", [("Numero", "tf_scoreboard_ping_as_text 1"), ("Icona", "tf_scoreboard_ping_as_text 0")])
    row("Switch", "Armi", [("Rapido", "hud_fastswitch 1"), ("Menu", "hud_fastswitch 0")])
    row("Fov", "FOV arma", [("54", "viewmodel_fov 54"), ("70", "viewmodel_fov 70"), ("80", "viewmodel_fov 80"),
                            ("90", "viewmodel_fov 90")])
    row("Reload", "", [("Ricarica HUD", "hud_reloadscheme")])
    assert y <= Y + H, ("custom menu overflows the card", y, Y + H)


def mainmenu(b):
    b.extend(fullscreen_grid(P + "Menu", 30, 466, "-205"))
    b.extend(stripes(P + "Menu", "-200"))
    title = find(b, "ClaudeTitle")
    tw = text_width_units("Team Fortress 2", "TypeHero")
    setkv(title, font="TypeHero", ypos=44, tall=56, wide=int(tw) + 12, zpos=3)
    setkv(find(b, "ClaudeTitleSegno"), ypos=50, tall=44)
    b.append(shadow(P + "TitleMark", "c-287", 76, int(tw) + 14, 18, "LtBlush", 1))
    b.append(label(P + "TitleKicker", "ClaudeHUD · edizione taccuino", "c-282", 36, 240, 8, "TypeLabel", "LtAccentText", 3,
                   allcaps=1))
    for name, y in (("RankBorder", 112), ("NoGCMessage", 112), ("NoGCImage", 125), ("RankTooltipPanel", 117),
                    ("EventPromo", 176), ("SafeMode", 226)):
        setkv(find(b, name), ypos=y)
    setkv(find(b, "RankPanel"), ypos=90)
    # the promo-codes button (shown by the game only when there are codes) sat where the Personalizza card
    # is now: move it to the free strip under the top bar, left of the notification icons
    setkv(find(b, "ShowPromoCodesButton"), xpos="c-28", ypos=30, wide=168, tall=22, zpos=5)
    fr = find(b, "FriendsContainer")
    setkv(fr, ypos=276, tall=140)
    b.append(shadow(P + "FriendsShadow", "c-278", 280, 256, 140, "LtAccent", 4))
    custom_menu(b)


edit("resource/ui/mainmenuoverride.res", mainmenu)


# ---- class / team menus -------------------------------------------------------------------------
def classmenu(b):
    b.extend(fullscreen_grid(P + "Class", 0, 466, "-5"))
    b.extend(stripes(P + "Class", "-4"))


edit("resource/ui/classselection.res", classmenu)


def teammenu(b):
    b.extend(fullscreen_grid(P + "Team", 0, 466, "-5"))
    b.extend(stripes(P + "Team", "-4"))
    for i, btn in enumerate(("teambutton2", "teambutton0", "teambutton1", "teambutton3")):
        kv = {k.lower(): v for k, v, c, cm in find(b, btn) if not isinstance(v, list)}
        b.append(shadow("%sTeamShadow%d" % (P, i), offset(kv["xpos"], 4), offset(kv["ypos"], 4), kv["wide"], kv["tall"],
                        "LtText", 2))


edit("resource/ui/teammenu.res", teammenu)


# ---- scoreboard -----------------------------------------------------------------------------------
def scoreboard(b):
    b.extend(grid(P + "Score", 0, 40, 640, 408, 16, "-1"))
    for name in ("BlueBand", "RedBand", "BlueTable", "RedTable", "PlayerNameBG"):
        setkv(find(b, name), zpos=1)
    for name, role in (("BlueBand", "LtText"), ("RedBand", "LtText"), ("BlueTable", "LtAccent"),
                       ("RedTable", "LtAccent"), ("PlayerNameBG", "LtSage")):
        kv = {k.lower(): v for k, v, c, cm in find(b, name) if not isinstance(v, list)}
        b.append(shadow(P + name + "Shadow", offset(kv["xpos"], SH), offset(kv["ypos"], SH), kv["wide"], kv["tall"], role, 0))


edit("resource/ui/scoreboard.res", scoreboard)
print("ok v2")
