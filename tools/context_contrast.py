#!/usr/bin/env python3
"""
Contrast IN CONTEXT. tools/contrast.py proves the token pairs that DESIGN.md declares; this tool checks
what the files actually do: every text colour of every .res element against the background it is drawn
on - its own painted background, else the topmost painted sibling underneath that covers it, else the
parent's, up to the page canvas (light pages: Ivory; in-game: the game world, unknown, not checked).

It catches what the contracts cannot see, e.g. a Valve text colour meant for a light tan popover that the
migration carried onto a popover ClaudeHUD made dark (text and card the same colour: invisible).

  python3 tools/context_contrast.py            report, exit 1 if any text is below 3:1
  python3 tools/context_contrast.py --list     also list every failure

fix_nodes(nodes, mode) is the same logic as a repair pass: tools/migrate.py and tools/hand/_patch.py run
it on Valve elements, so a migrated colour that lands on a same-colour surface becomes the readable text
token for that surface (the one that keeps the original's role: muted stays muted when it still passes).
"""
import glob
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import modes  # noqa: E402
import tokens as T  # noqa: E402
import vdf  # noqa: E402

ERROR_MIN = 3.0      # below this the text is not legible at any size (WCAG large-text floor)
GUESS_MIN = 2.0      # when the background is inferred from geometry, only near-identical colours are errors
FIX_TARGET = 4.5     # a repaired colour must reach body-text contrast

LABELS = {"label", "cexlabel", "cautofittinglabel", "cexrichtext", "richtext", "urllabel", "creplaytiplabel",
          "ceconitemdetailsrichtext", "ctftextwindow", "crichtextwithscrollbarborders", "checkbutton",
          "radiobutton", "cexcheckbutton", "cvartogglecheckbutton", "ccvartogglecheckbutton"}
BUTTONS = {"button", "cexbutton", "ceximagebutton", "ctfteambutton", "creplaybutton", "imagebutton",
           "cimagebutton", "cpreviewrotbutton"}
EX = {"cexlabel", "cexbutton", "ceximagebutton", "cexrichtext", "ctfteambutton", "creplaybutton"}
DEFAULT_FG = {"label": "Label.TextColor", "button": "Button.TextColor", "check": "CheckButton.TextColor",
              "rich": "RichText.TextColor"}
DEFAULT_BG = {"button": "Button.BgColor", "armed": "Button.ArmedBgColor", "depressed": "Button.DepressedBgColor"}
KNOWN_PAINT = {"editablepanel", "panel", "", "imagepanel", "ctfimagepanel"} | LABELS | BUTTONS
STATE_KEYS = (("default", "defaultfgcolor_override", "defaultbgcolor_override"),
              ("armed", "armedfgcolor_override", "armedbgcolor_override"),
              ("depressed", "depressedfgcolor_override", "depressedbgcolor_override"))
CANDIDATES = {"primary": ("DkText", "LtText", "DkOnRed", "LtOnBlu"),
              "muted": ("DkTextMuted", "LtTextMuted", "DkText", "LtText")}


# ------------------------------------------------------------------------------------- colours
def _scheme(name="clientscheme.res"):
    path = os.path.join(ROOT, "resource", name)
    colors, base = {}, {}
    if not os.path.exists(path):
        return colors, base
    s = vdf.parse(open(path, encoding="utf-8").read())
    sc = next(nd[1] for nd in s if isinstance(nd[1], list))
    for k, v, c, cm in vdf.get(sc, "Colors"):
        if not isinstance(v, list):
            try:
                p = [int(float(x)) for x in v.split()]
                colors[k.lower()] = tuple((p + [255])[:4])
            except ValueError:
                pass
    for k, v, c, cm in vdf.get(sc, "BaseSettings"):
        if not isinstance(v, list):
            base[k.lower()] = v
    return colors, base


COLORS, BASE = _scheme()
_SRC_COLORS, SOURCE_BASE = _scheme("sourcescheme.res")


def uses_sourcescheme(rel):
    """GameUI dialogs (resource/*.res, not resource/ui/) are drawn with SourceScheme's defaults."""
    return rel.count("/") == 1 and rel.startswith("resource/")


def resolve(v):
    """RGBA of a colour value: literal, token, <Token>A<pct> variant, or a scheme colour name."""
    if v is None:
        return None
    v = str(v).strip()
    if re.match(r"^-?[\d.]+\s+-?[\d.]+\s+-?[\d.]+", v):
        p = [max(0, min(255, int(float(x)))) for x in v.split()]
        return tuple((p + [255])[:4])
    if v in T.ROLES:
        return T.rgba(v)
    m = re.match(r"^(.*)A(\d0)$", v)
    if m and m.group(1) in T.ROLES:
        r, g, b, _ = T.rgba(m.group(1))
        return (r, g, b, int(round(int(m.group(2)) * 2.55)))
    if v.lower() in COLORS:
        return COLORS[v.lower()]
    b = BASE.get(v.lower())
    if b and b.lower() != v.lower():
        return resolve(b)
    return None


def over(top, below):
    a = top[3] / 255.0
    return tuple(int(round(top[i] * a + below[i] * (1 - a))) for i in range(3)) + (255,)


def ratio(fg, bg):
    l1, l2 = T.luminance(fg[:3]), T.luminance(bg[:3])
    hi, lo = max(l1, l2), min(l1, l2)
    return (hi + 0.05) / (lo + 0.05)


# ------------------------------------------------------------------------------------- geometry
def num(expr, full, own=0.0):
    e = str(expr).strip().replace(" ", "")
    for pat, fn in ((r"cs(-?[\d.]+)([+-][\d.]+)?", lambda a, b: full / 2 + a * own + b),
                    (r"rs(-?[\d.]+)([+-][\d.]+)?", lambda a, b: full - a * own + b),
                    (r"c(-?[\d.]+)([+-][\d.]+)?", lambda a, b: full / 2 + a + b),
                    (r"r(-?[\d.]+)([+-][\d.]+)?", lambda a, b: full - a + b)):
        m = re.fullmatch(pat, e)
        if m:
            return fn(float(m.group(1)), float(m.group(2) or 0))
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


class El:
    __slots__ = ("name", "body", "kv", "ctl", "rect", "z", "order", "children", "parent", "path")

    def __init__(self, name, body, parent, pw, ph, order):
        self.name, self.body, self.parent, self.order = name, body, parent, order
        self.kv = kv_of(body)
        self.ctl = self.kv.get("controlname", "").lower()
        w = num(self.kv.get("wide", "0"), pw)
        h = num(self.kv.get("tall", "0"), ph)
        self.rect = (num(self.kv.get("xpos", "0"), pw, w), num(self.kv.get("ypos", "0"), ph, h), w, h)
        zm = re.match(r"-?[\d.]+", self.kv.get("zpos", "0") or "0")
        self.z = float(zm.group()) if zm else 0.0
        self.children = []
        self.path = (parent.path + "/" if parent and parent.path else "") + name


def build_tree(nodes, width=853.0):
    root_nd = next(nd for nd in nodes if isinstance(nd[1], list))
    top = El("", [], None, width, 480, 0)
    top.rect = (0, 0, width, 480)

    def walk(parent, body):
        for i, nd in enumerate(body):
            if not isinstance(nd[1], list) or nd[0].lower().startswith("if_"):
                continue
            kv = kv_of(nd[1])
            if "controlname" not in kv and "fieldname" not in kv:
                continue
            el = El(nd[0], nd[1], parent, parent.rect[2], parent.rect[3], i)
            parent.children.append(el)
            walk(el, nd[1])

    walk(top, root_nd[1])
    return top


# ------------------------------------------------------------------------------------- backgrounds
def own_bg(el, state="default", base=None):
    """The background an element paints itself, or None."""
    kv = el.kv
    if el.ctl in BUTTONS:
        if kv.get("paintbackground", "1") == "0":
            return None
        key = {"default": "defaultbgcolor_override", "armed": "armedbgcolor_override",
               "depressed": "depressedbgcolor_override"}[state]
        v = kv.get(key) or (kv.get("defaultbgcolor_override") if state != "default" else None)
        if v is None:
            v = (base or BASE).get(DEFAULT_BG["button" if state == "default" else state].lower())
        c = resolve(v)
        return c if c and c[3] > 0 else None
    if el.ctl in ("imagepanel", "ctfimagepanel"):
        c = resolve(kv.get("fillcolor"))
        return c if c and c[3] > 0 else None
    paints = kv.get("paintbackground")
    v = kv.get("bgcolor_override")
    if el.ctl in ("editablepanel", "panel", "") and paints != "0" and v:
        c = resolve(v)
    elif paints == "1" and v:
        c = resolve(v)
    elif el.ctl.startswith("c") and ("infocus_bgcolor_override" in kv) and el.parent and el.parent.parent is None:
        c = resolve(kv.get("infocus_bgcolor_override"))   # the dialog's own frame
    else:
        return None
    return c if c and c[3] > 0 else None


def contains(outer, inner):
    ox, oy, ow, oh = outer
    ix, iy, iw, ih = inner
    cx, cy = ix + iw / 2, iy + ih / 2
    return ox <= cx <= ox + ow and oy <= cy <= oy + oh


def inside(outer, inner, tol=1.0):
    ox, oy, ow, oh = outer
    ix, iy, iw, ih = inner
    return ix >= ox - tol and iy >= oy - tol and ix + iw <= ox + ow + tol and iy + ih <= oy + oh + tol


def backdrop(el, canvas, base=None):
    """(colour under `el` not counting el itself, source). colour None = the unknown game world.
    source: "parent" when it comes from the painted ancestors / page canvas (reliable: el lies inside its
    parent by construction), "sibling" when a painted sibling underneath decides it (a geometric guess)."""
    parent = el.parent
    if parent is None:
        return canvas, "parent"
    # painted siblings drawn before el (lower z, or same z earlier in the file) that cover its centre
    below = [s for s in parent.children if s is not el and s.kv.get("visible", "1") != "0"
             and (s.z < el.z or (s.z == el.z and s.order < el.order)) and s.rect[2] > 0 and s.rect[3] > 0
             and contains(s.rect, el.rect)]
    below.sort(key=lambda s: (s.z, s.order))
    # a code-drawn control underneath (progress bar, model, item panel, HTML...) paints colours this tool
    # cannot know: from it upwards the backdrop is unknown
    for i in range(len(below) - 1, -1, -1):
        if below[i].ctl not in KNOWN_PAINT:
            return None, "sibling"
    layers = [own_bg(s, base=base) for s in below]
    if parent.parent is None:
        col, src = canvas, "parent"
    else:
        pb = own_bg(parent, base=base)
        under, src = backdrop(parent, canvas, base)
        if pb is None:
            col = under
        elif pb[3] >= 250:
            col, src = pb, "parent"
        elif under is not None:
            col = over(pb, under)
        elif pb[3] >= 200:
            col, src = pb, "parent"
        else:
            col = None
    for s_el, c in zip(below, layers):
        if c is None:
            continue
        # a painted sibling that wholly contains the element is as reliable as a parent
        kind = "parent" if inside(s_el.rect, el.rect) and src == "parent" else "sibling"
        if c[3] >= 250:
            col, src = c, kind
        elif col is not None:
            col, src = over(c, col), kind
        elif c[3] >= 200:
            col, src = c, kind
    return col, src


def text_colors(el, base=None):
    """[(state, key, value, rgba)] for the text an element draws."""
    kv, ctl, out = el.kv, el.ctl, []
    base = base or BASE
    if ctl in ("ceximagebutton", "imagebutton", "cimagebutton") and not kv.get("labeltext"):
        return out  # icon-only button: its text colour is never drawn
    if ctl in BUTTONS and "labeltext" in kv and not kv["labeltext"].strip():
        return out  # explicitly empty label (colour swatches...)
    if ctl in BUTTONS:
        for state, fk, bk in STATE_KEYS:
            v = kv.get(fk) or (kv.get("fgcolor_override") if state == "default" else None)
            if v is None and state == "default" and ctl in EX:
                v = kv.get("fgcolor")
            if v is None:
                if state != "default":
                    continue
                v = base.get("button.textcolor")
            out.append((state, fk if kv.get(fk) else ("fgcolor" if v == kv.get("fgcolor") else "default"), v, resolve(v)))
        return out
    if ctl in LABELS:
        v = None
        key = None
        if ctl in EX and kv.get("fgcolor"):
            v, key = kv["fgcolor"], "fgcolor"
        elif kv.get("fgcolor_override"):
            v, key = kv["fgcolor_override"], "fgcolor_override"
        else:
            fam = "check" if "check" in ctl or "radio" in ctl else "rich" if "rich" in ctl else "label"
            v, key = base.get(DEFAULT_FG[fam].lower()), "default"
        out.append(("default", key, v, resolve(v)))
    return out


def iter_elements(top):
    stack = list(top.children)
    while stack:
        el = stack.pop(0)
        yield el
        stack[0:0] = el.children


def canvas_of(rel):
    return T.rgba("LtCanvas") if modes.mode_of(rel) == "light" else None


def check_nodes(nodes, rel, warnings=False):
    """Failing text colours: (el, state, key, value, fg, bg, ratio, certain). certain = the background is
    the element's own painted background or comes from its painted ancestors (no sibling guess; the bare
    page canvas of a light file counts as a guess, since an image may sit there). Errors: certain and below 3:1, or
    guessed and below 2:1 (same colour family). With warnings=True also guessed 2-3:1 cases."""
    if not any(isinstance(nd[1], list) for nd in nodes):
        return []
    top = build_tree(nodes)
    canvas = canvas_of(rel)
    base = SOURCE_BASE if uses_sourcescheme(rel) and SOURCE_BASE else BASE
    problems = []
    for el in iter_elements(top):
        if el.rect[2] <= 0 or el.rect[3] <= 0:
            continue
        cols = text_colors(el, base)
        if not cols:
            continue
        under = src = None
        for state, key, value, fg in cols:
            if fg is None or fg[3] < 40:
                continue
            bg = own_bg(el, state, base)
            certain = bg is not None and bg[3] >= 250
            if not certain:
                if under is None:
                    under, src = backdrop(el, canvas, base)
                if under is None:
                    continue
                bg = over(bg, under) if bg else under
                certain = src == "parent" and not (el.parent and el.parent.parent is None and canvas is not None
                                                   and own_bg(el.parent, base=base) is None)
            f = over(fg, bg) if fg[3] < 255 else fg
            r = ratio(f, bg)
            if r < ERROR_MIN and (certain or r < GUESS_MIN or warnings):
                problems.append((el, state, key, value, fg, bg, r, certain))
    return problems


# ------------------------------------------------------------------------------------- repair
def best_token(original, bg):
    muted = bool(re.search(r"Muted|Faint|muted", str(original)))
    for group in (("muted",) if muted else ()) + ("primary",):
        best, best_r = None, 0
        for t in CANDIDATES[group]:
            r = ratio(T.rgba(t), bg)
            if r >= FIX_TARGET and (best is None or (group == "muted" and r > best_r) or group == "primary" and r > best_r):
                best, best_r = t, r
        if best:
            return best
    return max(CANDIDATES["primary"], key=lambda t: ratio(T.rgba(t), bg))


def fix_nodes(nodes, rel, name_allowed, note="ClaudeHUD: contrasto nel contesto"):
    """Repair every failing text colour in place; returns the number of fixes."""
    fixed = 0
    for el, state, key, value, fg, bg, r, certain in check_nodes(nodes, rel):
        token = best_token(value, bg)
        real_key = key if key not in ("default",) else {"default": "fgcolor_override"}.get(state, key)
        if el.ctl in BUTTONS and key in ("default", "fgcolor"):
            real_key = "defaultFgColor_override"
        allowed = name_allowed(real_key, el.ctl)
        val = token if allowed else T.rgba_str(token)
        cm = note if allowed else "token: %s - %s" % (token, note)
        hit = False
        for nd in el.body:
            if not isinstance(nd[1], list) and nd[0].lower() == real_key.lower():
                nd[1], nd[3], hit = val, cm, True
        if not hit:
            el.body.append([real_key, val, None, cm])
        fixed += 1
    return fixed


# ------------------------------------------------------------------------------------- main
def files():
    out = []
    for pat in ("resource/**/*.res", "scripts/**/*.res"):
        for p in sorted(glob.glob(os.path.join(ROOT, pat), recursive=True)):
            rel = os.path.relpath(p, ROOT).replace("\\", "/")
            if rel in ("resource/clientscheme.res", "resource/sourcescheme.res", "resource/chatscheme.res"):
                continue
            out.append(rel)
    return out


def main():
    show = "--list" in sys.argv
    errors, warns, checked = [], [], 0
    for rel in files():
        try:
            nodes = vdf.parse(open(os.path.join(ROOT, rel), encoding="utf-8", errors="replace").read())
        except Exception:
            continue
        if not any(isinstance(nd[1], list) for nd in nodes):
            continue
        checked += 1
        for p in check_nodes(nodes, rel, warnings=True):
            (errors if (p[7] or p[6] < GUESS_MIN) else warns).append((rel,) + p)
    for tag, rows in (("ERR ", errors), ("warn", warns)):
        for rel, el, state, key, value, fg, bg, r, certain in rows if show else rows[:25]:
            print("  %s %-44s %-40s %-9s %s=%s on #%02X%02X%02X %.2f:1%s" % (
                tag, rel, el.path[:40], state, key, value, bg[0], bg[1], bg[2], r, "" if certain else " (sfondo dedotto)"))
        if not show and len(rows) > 25:
            print("  ... %d more %s (use --list)" % (len(rows) - 25, tag.strip()))
    print("context contrast: %d files; %d errors (text below %.1f:1 on its own background, or below %.1f:1 on an "
          "inferred one); %d warnings (inferred background, %.1f-%.1f:1)"
          % (checked, len(errors), ERROR_MIN, GUESS_MIN, len(warns), GUESS_MIN, ERROR_MIN))
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
