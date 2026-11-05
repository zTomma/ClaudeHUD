#!/usr/bin/env python3
"""
Schematic previews (NOT game renders): draws the main cards with the real fonts, the real tokens and
the geometry read from the .res files (via tools/layout_check.py), so reviewers can judge proportions
and hierarchy before testing in game. Writes:
  docs/preview_ingame.png   in-game HUD at 1920x1080 (16:9), sample values
  docs/preview_menu.png     main menu at 1920x1080 (light editorial)
  docs/colorblind.png       team colours under normal vision and simulated CVD
The engine's real corner radius, font hinting and antialiasing differ: this is a plan, not a screenshot.
"""
import os
import sys

from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import contrast as C  # noqa: E402
import layout_check as L  # noqa: E402
import tokens as T  # noqa: E402

OUT = os.path.join(ROOT, "docs")
S = 1080 / 480.0          # proportional unit -> pixels at 1080p
RADIUS = 7                # engine corner radius estimate (px)
FONTS = os.path.join(ROOT, "resource", "fonts")
FILE_OF = {f[1]: f[0] for f in T.FONT_FILES}
CELL = {"IBM Plex Sans": 1.300, "Source Serif 4": 1.371}


def font(token):
    (fam, _w), tall, _role = T.TYPE[token]
    cell = 1.371 if fam.startswith("Source") else 1.300
    return ImageFont.truetype(os.path.join(FONTS, FILE_OF[fam]), max(6, int(round(tall * S / cell))))


def col(role):
    return T.rgba(role)


def px(r):
    x, y, w, h = r
    return [x * S, y * S, (x + w) * S, (y + h) * S]


def card(d, r, role="DkCard", radius=RADIUS):
    d.rounded_rectangle(px(r), radius=radius, fill=col(role))


def text(d, xy_units, s, token, role, anchor="la"):
    d.text((xy_units[0] * S, xy_units[1] * S), s, font=font(token), fill=col(role), anchor=anchor)


def backdrop(w, h):
    """A neutral, busy 'game world' so the opaque cards can be judged against detail."""
    img = Image.new("RGBA", (w, h), (92, 98, 104, 255))
    d = ImageDraw.Draw(img)
    for i in range(0, w, 160):
        for j in range(0, h, 160):
            if (i // 160 + j // 160) % 2:
                d.rectangle([i, j, i + 159, j + 159], fill=(120, 116, 104, 255))
    d.rectangle([0, int(h * 0.62), w, h], fill=(70, 66, 58, 255))
    d.polygon([(0, int(h * 0.62)), (w * 0.45, int(h * 0.35)), (w, int(h * 0.62))], fill=(150, 160, 170, 255))
    return img


def ingame():
    W = 480 * 16 / 9
    els = L.elements(W)
    img = backdrop(1920, 1080)
    d = ImageDraw.Draw(img, "RGBA")
    # health
    hc = els["Salute (scheda)"]
    card(d, hc)
    text(d, (hc[0] + 58, hc[1] + 18), "125", "NumXL", "DkText", "rm")
    text(d, (hc[0] + 62, hc[1] + 26), "150", "NumXS", "DkTextMuted", "ls")
    # ammo
    am = els["Munizioni"]
    card(d, am)
    text(d, (am[0] + 54, am[1] + 18), "4", "NumXL", "DkAccent", "rm")
    text(d, (am[0] + 58, am[1] + 26), "20", "NumM", "DkTextMuted", "ls")
    d.rectangle(px([am[0], am[1] + 4, 2, 28]), fill=col("DkAccent"))
    # medic charge
    mc = els["Carica Medic"]
    card(d, mc)
    text(d, (mc[0] + 8, mc[1] + 5), "ÜBERCARICA", "TypeLabel", "DkTextMuted")
    d.rectangle(px([mc[0] + 8, mc[1] + 26, 42, 4]), fill=col("DkChip"))
    d.rectangle(px([mc[0] + 8, mc[1] + 26, 42 * 0.64, 4]), fill=col("DkText"))
    text(d, (mc[0] + 82, mc[1] + 25), "64", "NumM", "DkText", "rm")
    # item meter
    im = els["Metro oggetto"]
    card(d, im)
    text(d, (im[0] + 8, im[1] + 5), "PALLA", "TypeLabel", "DkTextMuted")
    d.rectangle(px([im[0] + 8, im[1] + 22, 64, 6]), fill=col("DkChip"))
    d.rectangle(px([im[0] + 8, im[1] + 22, 40, 6]), fill=col("DkText"))
    # timer
    tm = els["Timer di round"]
    card(d, [tm[0], tm[1], 80, 28])
    text(d, (tm[0] + 32, tm[1] + 14), "4:59", "NumL", "DkText", "mm")
    d.ellipse(px([tm[0] + 62, tm[1] + 7, 14, 14]), fill=col("DkChip"))
    d.pieslice(px([tm[0] + 62, tm[1] + 7, 14, 14]), -90, 130, fill=col("DkText"))
    # killfeed
    kf = els["Killfeed (area)"]
    rows = [("Pyro", "DkRedText", "Medic", "DkBluText", False), ("Tu", "DkBluText", "Heavy", "DkRedText", True),
            ("Scout", "DkRedText", "Sniper", "DkBluText", False)]
    for i, (a, ca, b, cb, local) in enumerate(rows):
        y = kf[1] + i * 20
        w_units = 150
        x = 480 * 16 / 9 - 12 - w_units
        card(d, [x, y, w_units, 16], "DkCardLocal" if local else "DkCard", radius=6)
        text(d, (x + 6, y + 8), a, "TypeBodyStrong", ca, "lm")
        d.rectangle(px([x + 62, y + 5, 24, 6]), fill=col("DkText"))
        text(d, (x + w_units - 6, y + 8), b, "TypeBodyStrong", cb, "rm")
    # target ID
    t = els["Target ID"]
    card(d, [t[0] + 70, t[1], 112, 30])
    card(d, [t[0] + 74, t[1] + 4, 22, 22], "DkChip", radius=6)
    text(d, (t[0] + 85, t[1] + 15), "175", "NumS", "DkText", "mm")
    text(d, (t[0] + 100, t[1] + 4), "Heavy", "TypeBodyStrong", "DkBluText")
    text(d, (t[0] + 100, t[1] + 16), "Salute 300 / 300", "TypeCaption", "DkTextMuted")
    # chat
    ch = els["Chat"]
    d.rounded_rectangle(px([ch[0], ch[1] + 76, 200, 40]), radius=RADIUS, fill=col("DkCardSoft"))
    text(d, (ch[0] + 6, ch[1] + 82), "Scout: spingiamo sul punto B", "TypeBody", "DkText")
    text(d, (ch[0] + 6, ch[1] + 96), "(Squadra) Medic: über tra 10 secondi", "TypeBody", "DkTextMuted")
    # crosshair (off by default) shown faint for reference
    d.rectangle(px([480 * 16 / 9 / 2 - 2, 238, 4, 4]), fill=col("DkCard"))
    d.rectangle(px([480 * 16 / 9 / 2 - 1, 239, 2, 2]), fill=col("DkText"))
    d.text((24, 300), "ClaudeHUD - anteprima schematica (tools/preview.py), non e' un render del gioco",
           font=ImageFont.truetype(os.path.join(FONTS, "IBMPlexSans-Medium.ttf"), 20), fill=(250, 249, 245, 230))
    img.convert("RGB").save(os.path.join(OUT, "preview_ingame.png"), optimize=True)


def menu():
    W = 480 * 16 / 9
    img = Image.new("RGBA", (1920, 1080), col("LtCanvas"))
    d = ImageDraw.Draw(img, "RGBA")
    cx = W / 2
    # top bar
    d.rectangle(px([0, 0, W, 30]), fill=col("LtCard"))
    d.rectangle(px([0, 30, W, 0.5]), fill=col("LtLine"))
    card(d, [W - 140, 4, 112, 22], "LtButton")
    text(d, (W - 84, 15), "Trova una partita", "TypeBodyStrong", "LtOnButton", "mm")
    # title + Segno
    d.rectangle(px([cx - 290, 52, 2, 36]), fill=col("LtAccent"))
    text(d, (cx - 282, 48), "Team Fortress 2", "TypeDisplay", "LtText")
    # left column cards
    card(d, [cx - 282, 100, 256, 56], "LtCard")
    text(d, (cx - 270, 108), "Grado competitivo", "TypeCaption", "LtTextMuted")
    text(d, (cx - 270, 120), "Livello 12", "TypeHeading", "LtText")
    card(d, [cx - 282, 164, 256, 96], "LtCard")
    text(d, (cx - 270, 172), "EVENTO", "TypeLabel", "LtAccentText")
    text(d, (cx - 270, 184), "Smissmas 2026", "TypeHeading", "LtText")
    card(d, [cx - 282, 268, 256, 148], "LtCard")
    text(d, (cx - 270, 274), "Amici", "TypeHeading", "LtText")
    for i, n in enumerate(("Daniele · in partita", "Marta · nel menu", "Luca · offline")):
        text(d, (cx - 270, 298 + i * 14), n, "TypeBody", "LtText" if i < 2 else "LtTextMuted")
    # bottom
    d.rectangle(px([0, 424, W, 0.5]), fill=col("LtLine"))
    card(d, [cx - 282, 480 - 44, 100, 26], "LtCardAlt")
    text(d, (cx - 232, 480 - 31), "Oggetti", "TypeBodyStrong", "LtText", "mm")
    card(d, [cx - 178, 480 - 44, 100, 26], "LtButtonHover")
    text(d, (cx - 128, 480 - 31), "Negozio", "TypeBodyStrong", "LtOnButtonHover", "mm")
    # font test card (right)
    import re as _re
    src = open(os.path.join(ROOT, "resource", "ui", "claudehud_fonttest.res"), encoding="utf-8").read()
    card_h = int(_re.search(r'"FontTestCard".*?"tall"\s+"(\d+)"', src, _re.S).group(1))
    card(d, [cx + 8, 64, 300, card_h], "LtCard")
    text(d, (cx + 16, 66), "CLAUDEHUD · PROVA FONT", "TypeLabel", "LtAccentText")
    y = 80
    for name, label in _re.findall(r'"FontTest_(\w+)".*?"labelText"\s+"([^"]*)"', src, _re.S):
        text(d, (cx + 16, y), label, name, "LtText")
        y += T.TYPE[name][1] + 3
    d.text((24, 20), "ClaudeHUD - anteprima schematica (tools/preview.py), non e' un render del gioco",
           font=ImageFont.truetype(os.path.join(FONTS, "IBMPlexSans-Medium.ttf"), 20), fill=col("LtTextMuted"))
    img.convert("RGB").save(os.path.join(OUT, "preview_menu.png"), optimize=True)


def colorblind():
    pairs = [("DkRedText", "DkBluText", "DkCard"), ("DkRedFill", "DkBluFill", "DkCard"), ("LtRedText", "LtBluText", "LtCard")]
    modes = [("normale", None), ("protanopia", "protanopia"), ("deuteranopia", "deuteranopia"), ("tritanopia", "tritanopia")]
    img = Image.new("RGB", (1200, 420), col("LtCanvas")[:3])
    d = ImageDraw.Draw(img)
    f = ImageFont.truetype(os.path.join(FONTS, "IBMPlexSans-Medium.ttf"), 22)
    fb = ImageFont.truetype(os.path.join(FONTS, "IBMPlexSans-SemiBold.ttf"), 30)
    for j, (label, kind) in enumerate(modes):
        d.text((300 * j + 20, 16), label, font=f, fill=col("LtText")[:3])
    for i, (a, b, bg) in enumerate(pairs):
        for j, (label, kind) in enumerate(modes):
            def sim(c):
                return C.simulate(c, kind) if kind else c
            x, y = 300 * j + 20, 60 + i * 120
            d.rounded_rectangle([x, y, x + 260, y + 100], radius=10, fill=sim(T.rgba(bg)[:3]))
            d.text((x + 16, y + 30), "RED", font=fb, fill=sim(T.rgba(a)[:3]))
            d.text((x + 140, y + 30), "BLU", font=fb, fill=sim(T.rgba(b)[:3]))
    img.save(os.path.join(OUT, "colorblind.png"), optimize=True)


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    ingame()
    menu()
    colorblind()
    print("wrote docs/preview_ingame.png, docs/preview_menu.png, docs/colorblind.png")
