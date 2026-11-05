#!/usr/bin/env python3
"""
Schematic renderer for .res files (NOT the game): draws the simple elements of a panel straight from the
file - EditablePanel/Label backgrounds, ImagePanel fills, CExLabel/Label text, CExButton chips - with the
real fonts and the token colours, so layouts can be checked for overlaps without the game.
Game-driven content (models, avatars, item icons, code-filled text) is drawn as a dashed placeholder.

  python3 tools/render_res.py resource/ui/mainmenuoverride.res docs/render_menu.png [--width 1920 --height 1080]
"""
import os
import re
import sys

from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import tokens as T  # noqa: E402
import vdf  # noqa: E402

FILE_OF = {f[1]: f[0] for f in T.FONT_FILES}


def scheme_colors():
    s = vdf.parse(open(os.path.join(ROOT, "resource", "clientscheme.res"), encoding="utf-8").read())
    sc = next(nd[1] for nd in s if isinstance(nd[1], list))
    out = {}
    for k, v, c, cm in vdf.get(sc, "Colors"):
        if not isinstance(v, list):
            p = [int(float(x)) for x in v.split()]
            out[k.lower()] = tuple((p + [255])[:4])
    return out


COLORS = scheme_colors()


def color(v, default=None):
    if v is None:
        return default
    v = v.strip()
    if re.match(r"^\d+\s+\d+\s+\d+", v):
        p = [int(float(x)) for x in v.split()]
        return tuple((p + [255])[:4])
    return COLORS.get(v.lower(), default)


def font_for(name, scale):
    t = T.TYPE.get(name)
    if t:
        (fam, _w), tall, _r = t
    else:  # legacy font: look it up in the generated scheme
        fam, tall = "IBM Plex Sans", 9
    cell = 1.371 if fam.startswith("Source") else 1.300
    return ImageFont.truetype(os.path.join(ROOT, "resource", "fonts", FILE_OF.get(fam, "IBMPlexSans-Regular.ttf")),
                              max(6, int(round(tall * scale / cell))))


def num(expr, full, own=0.0, parent_full=None):
    e = str(expr).strip().replace(" ", "")
    m = re.fullmatch(r"cs(-?[\d.]+)([+-][\d.]+)?", e)
    if m:
        return full / 2 + float(m.group(1)) * own + float(m.group(2) or 0)
    m = re.fullmatch(r"rs(-?[\d.]+)([+-][\d.]+)?", e)
    if m:
        return full - float(m.group(1)) * own + float(m.group(2) or 0)
    m = re.fullmatch(r"c(-?[\d.]+)([+-][\d.]+)?", e)
    if m:
        return full / 2 + float(m.group(1)) + float(m.group(2) or 0)
    m = re.fullmatch(r"r(-?[\d.]+)([+-][\d.]+)?", e)
    if m:
        return full - float(m.group(1)) + float(m.group(2) or 0)
    m = re.fullmatch(r"f(-?[\d.]+)", e)
    if m:
        return full - float(m.group(1))
    m = re.fullmatch(r"p([\d.]+)", e)
    if m:
        return full * float(m.group(1))
    try:
        return float(e)
    except ValueError:
        return 0.0


def kv_of(body):
    d = {}
    for k, v, c, cm in body:
        if not isinstance(v, list) and not (c and ("X360" in c or "OSX" in c)) and k.lower() not in d:
            d[k.lower()] = v
    return d


def render(rel, out, width=1920, height=1080, background=None):
    scale = height / 480.0
    W = 480 * width / height
    nodes = vdf.parse(open(os.path.join(ROOT, rel), encoding="utf-8").read())
    rootnd = next(nd for nd in nodes if isinstance(nd[1], list))
    root = rootnd[1]
    self_name = os.path.splitext(os.path.basename(rootnd[0].replace("\\", "/")))[0].lower()
    items = []

    first = [True]

    def collect(body, ox, oy, pw, ph, depth):
        for name, val, cond, cm in body:
            if not isinstance(val, list) or name.lower().startswith("if_"):
                continue
            kv = kv_of(val)
            if "fieldname" not in kv and "controlname" not in kv:
                continue
            if kv.get("visible", "1") == "0":
                continue
            w = num(kv.get("wide", "0"), pw)
            h = num(kv.get("tall", "0"), ph)
            x = ox + num(kv.get("xpos", "0"), pw, w)
            y = oy + num(kv.get("ypos", "0"), ph, h)
            zm = re.match(r"-?[\d.]+", kv.get("zpos", "0") or "0")
            z = float(zm.group()) if zm else 0.0
            basic = kv.get("controlname", "").lower() in ("editablepanel", "imagepanel", "ctfimagepanel", "label",
                                                          "cexlabel", "button", "cexbutton", "ceximagebutton")
            whole = kv.get("wide", "") in ("f0", "f1") or kv.get("tall", "") == "480"
            if depth == 0 and (name.lower() == self_name or (first[0] and (whole or not basic))):
                z = -1e9  # the panel's own settings block (first block): its background is under every child
                if "bgcolor_override" not in kv and kv.get("infocus_bgcolor_override"):
                    kv = dict(kv, bgcolor_override=kv["infocus_bgcolor_override"], controlname="editablepanel")
            if depth == 0:
                first[0] = False
            items.append((z, depth, len(items), name, kv, (x, y, w, h)))
            if kv.get("controlname", "").lower() in ("editablepanel", ""):
                collect(val, x, y, w, h, depth + 1)

    collect(root, 0, 0, W, 480, 0)
    img = Image.new("RGBA", (width, height), background or (80, 84, 88, 255))
    d = ImageDraw.Draw(img, "RGBA")
    for z, depth, idx, name, kv, (x, y, w, h) in sorted(items, key=lambda t: (t[0], t[1], t[2])):
        if w <= 0 or h <= 0:
            continue
        box = [x * scale, y * scale, (x + w) * scale - 1, (y + h) * scale - 1]
        ctl = kv.get("controlname", "").lower()
        radius = 9 if kv.get("paintbackgroundtype") == "2" else 0
        if ctl in ("imagepanel", "ctfimagepanel"):
            fc = color(kv.get("fillcolor"))
            if fc and fc[3] > 0:
                d.rectangle(box, fill=fc)
            elif kv.get("image"):
                d.rectangle(box, outline=(150, 150, 150, 120))
            continue
        if ctl in ("cexbutton", "ceximagebutton", "button", "ctfteambutton", "creplaybutton"):
            bg = color(kv.get("defaultbgcolor_override"), (0, 0, 0, 0))
            if kv.get("paintbackground", "1") != "0" and bg[3] > 0:
                d.rounded_rectangle(box, radius=radius, fill=bg) if radius else d.rectangle(box, fill=bg)
            if kv.get("border_default", "").lower() == "clinputlt":
                d.rounded_rectangle(box, radius=radius, outline=color("LtLineStrong"))
            fg = color(kv.get("defaultfgcolor_override"), color("LtText"))
            text = kv.get("labeltext", "")
            if text and not text.startswith("#"):
                f = font_for(kv.get("font", "TypeBody"), scale)
                d.text(((x + w / 2) * scale, (y + h / 2) * scale), text, font=f, fill=fg, anchor="mm")
            elif text:
                f = font_for("TypeCaption", scale)
                d.text(((x + w / 2) * scale, (y + h / 2) * scale), text[1:][:18], font=f, fill=fg, anchor="mm")
            continue
        if ctl in ("cexlabel", "label", "cautofittinglabel"):
            bg = color(kv.get("bgcolor_override"))
            if kv.get("paintbackground") == "1" and bg and bg[3] > 0:
                d.rounded_rectangle(box, radius=radius, fill=bg) if radius else d.rectangle(box, fill=bg)
            text = kv.get("labeltext", "")
            if not text:
                continue
            fg = color(kv.get("fgcolor"), None) or color(kv.get("fgcolor_override"), color("LtText"))
            f = font_for(kv.get("font", "TypeBody"), scale)
            if kv.get("allcaps") == "1":
                text = text.upper()
            if text.startswith("#") or text.startswith("%"):
                text = "‹" + text.strip("#%")[:24] + "›"
            a = kv.get("textalignment", "west").lower()
            ax = {"west": "l", "north-west": "l", "left": "l", "center": "m", "north": "m", "south": "m",
                  "east": "r", "south-east": "r", "north-east": "r", "south-west": "l"}.get(a, "l")
            tx = {"l": x, "m": x + w / 2, "r": x + w}[ax] * scale
            if kv.get("wrap") == "1":
                words, linebuf, ty = text.split(" "), "", y * scale
                for wd in words:
                    trial = (linebuf + " " + wd).strip()
                    if f.getlength(trial) > w * scale and linebuf:
                        d.text((x * scale, ty), linebuf, font=f, fill=fg)
                        ty += f.size * 1.25
                        linebuf = wd
                        if ty > (y + h) * scale:
                            break
                    else:
                        linebuf = trial
                if ty <= (y + h) * scale:
                    d.text((x * scale, ty), linebuf, font=f, fill=fg)
            else:
                d.text((tx, (y + h / 2) * scale), text, font=f, fill=fg, anchor=ax + "m")
            continue
        if ctl in ("editablepanel", "panel", ""):
            bg = color(kv.get("bgcolor_override"))
            if bg and bg[3] > 0 and kv.get("paintbackground", "1") != "0":
                d.rounded_rectangle(box, radius=radius, fill=bg) if radius else d.rectangle(box, fill=bg)
            continue
        # game-driven content
        d.rectangle(box, outline=(160, 160, 160, 90))
    img.convert("RGB").save(os.path.join(ROOT, out), optimize=True)
    return out


DOCS = (("resource/ui/mainmenuoverride.res", "docs/render_menu.png"),
        ("resource/ui/teammenu.res", "docs/render_team.png"),
        ("resource/ui/classselection.res", "docs/render_class.png"),
        ("resource/ui/scoreboard.res", "docs/render_scoreboard.png"))

if __name__ == "__main__":
    a = sys.argv[1:]
    w = int(a[a.index("--width") + 1]) if "--width" in a else 1920
    h = int(a[a.index("--height") + 1]) if "--height" in a else 1080
    if not a or a[0].startswith("--"):  # build step: the standard set of schematic renders in docs/
        for rel, out in DOCS:
            render(rel, out, w, h)
        print("wrote %d schematic renders in docs/" % len(DOCS))
    else:
        print(render(a[0], a[1], w, h))
