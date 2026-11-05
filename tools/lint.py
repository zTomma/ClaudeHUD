#!/usr/bin/env python3
"""
ClaudeHUD linter. Run before declaring any phase ready:  python3 tools/lint.py

Errors (exit code 1)
  * VDF syntax: balanced braces, terminated quotes, keys with values           (all files)
  * duplicate keys with the same condition in the same block                  (hand-written files)
  * colour names, fonts and borders referenced but not defined in the scheme  (all files)
  * colour literals that do not come from a token (no `// token:` comment)    (all files)
  * keys / ControlName values never used in Valve's own files                 (hand-written files)
  * element names of the original file missing from the rewrite               (hand-written files)
  * hudanimations: unbalanced braces, unknown commands, unknown colour names
Warnings
  * duplicate keys inherited from Valve's originals (migrated files)
"""
import glob
import os
import re
import sys
from collections import Counter, defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import migrate as M  # noqa: E402
import vdf  # noqa: E402

PRISTINE = os.path.join(ROOT, "#TF2 Files")
SCHEMES = ("resource/clientscheme.res", "resource/sourcescheme.res", "resource/chatscheme.res",
           "resource/pdacontrolpanelscheme.res")
ANIM_COMMANDS = {"animate", "runevent", "stopevent", "setvisible", "firecommand", "setfont", "settexture", "setstring",
                 "stopanimation", "stoppanelanimations", "runeventchild", "setinputenabled", "playsound", "setalpha"}
COLOR_VARS = {"fgcolor", "bgcolor", "iconcolor", "fillcolor", "drawcolor", "color", "itemcolor", "menucolor", "textcolor",
              "hintcolor", "ammo2color", "flashcolor", "teamcolor", "image_drawcolor", "bgcolor_override", "fgcolor_override"}


def scheme_names():
    s = vdf.parse(open(os.path.join(ROOT, "resource", "clientscheme.res"), encoding="utf-8").read())
    sc = vdf.get(s, "Scheme")
    colors = {k.lower() for k, v, c, cm in vdf.get(sc, "Colors") if not isinstance(v, list)}
    base = {k.lower() for k, v, c, cm in vdf.get(sc, "BaseSettings") if not isinstance(v, list)}
    fonts = {k.lower() for k, v, c, cm in vdf.get(sc, "Fonts") if isinstance(v, list)}
    borders = {k.lower() for k, v, c, cm in vdf.get(sc, "Borders") if isinstance(v, list)}
    return colors, base, fonts, borders


# Keys not used in any Valve .res but verified in the TF2 client source (Source SDK 2013, 2025 release):
SOURCE_VERIFIED_KEYS = {
    "killstreakbackgroundcolor",   # hud_basedeathnotice.h: CPanelAnimationVar(Color, m_clrKillStreakBg, ...)
}


def corpus():
    """Keys, ControlNames and pristine element names from Valve's original files."""
    keys, controls = set(SOURCE_VERIFIED_KEYS), set()
    for root in ("#TF2 Files", "#HL2 Files", "#Platform Files"):
        for p in glob.glob(os.path.join(ROOT, root, "**", "*.res"), recursive=True):
            try:
                nodes = vdf.parse(open(p, encoding="utf-8", errors="replace").read())
            except vdf.VDFError:
                continue
            for path, nd in vdf.walk(nodes):
                if not isinstance(nd[1], list):
                    keys.add(nd[0].lower())
                    if nd[0].lower() == "controlname":
                        controls.add(nd[1].lower())
    return keys, controls


def element_names(nodes):
    names = set()
    for path, nd in vdf.walk(nodes):
        if isinstance(nd[1], list) and len(path) == 1:
            names.add(nd[0].lower())
    return names


def dup_keys(nodes, rel, report):
    for path, nd in [((), ["<root>", nodes, None, None])] + list(vdf.walk(nodes)):
        if not isinstance(nd[1], list):
            continue
        # repeated *blocks* are a Valve list idiom (e.g. several "animation" blocks); only leaf keys count
        seen = Counter((k.lower(), c or "") for k, v, c, cm in nd[1] if k != "#base" and not isinstance(v, list))
        for (k, c), n in seen.items():
            if n > 1:
                report.append((rel, "chiave duplicata %r%s x%d in %s" % (k, (" " + c) if c else "", n, "/".join(path + (nd[0],)))))


def pristine_refs(rel):
    """Values referenced in Valve's original copy of the file (to tell inherited problems apart)."""
    src = M.pristine_path(rel)
    if not src:
        return set()
    try:
        nodes = vdf.parse(open(src, encoding="utf-8", errors="replace").read())
    except vdf.VDFError:
        return set()
    return {(nd[0].lower(), nd[1].lower()) for path, nd in vdf.walk(nodes) if not isinstance(nd[1], list)}


def lint_res(rel, text, names, known, hand, errors, warnings):
    colors, base, fonts, borders = names
    try:
        nodes = vdf.parse(text)
    except vdf.VDFError as e:
        errors.append((rel, "sintassi: %s" % e))
        return
    inherited = pristine_refs(rel)
    real_errors = errors

    class _Sink(list):
        pass
    errors = _Sink()
    (dup_keys(nodes, rel, errors if hand else warnings))
    keys, controls = known
    ctl_of = {}
    def _walk(ns, ctl=""):
        for nd in ns:
            if isinstance(nd[1], list):
                yield from _walk(nd[1], M.block_ctl(nd[1]))
            else:
                yield ctl, nd
    for ctl, nd in _walk(nodes):
        key, val, cond, cm = nd
        if M.is_token_name(val) and not M.name_allowed(key, ctl) and (key.lower() in M.ALL_COLOR_KEYS or key.lower().endswith("color")):
            errors.append((rel, "nome di colore in una chiave che accetta solo RGBA (verificato nel sorgente): %s %r in %s" % (key, val, ctl or "elemento HUD")))
        k = key.lower()
        colorish = k in M.ALL_COLOR_KEYS or (re.search(r"colou?r|clor", k) and not k.startswith("standard_text"))
        if colorish and (M.is_literal(val) or k in M.ALL_COLOR_KEYS):
            if M.is_literal(val):
                if not (cm and cm.startswith("token:")):
                    errors.append((rel, "colore letterale non generato da token: %s %r" % (key, val)))
            elif val.lower() not in colors and val.lower() not in base:
                errors.append((rel, "colore non definito nello scheme: %s %r" % (key, val)))
        elif k in ("font", "font_minmode", "font_lodef", "font_hidef", "textfont", "itemfont", "itemfontpulsing",
                   "numberfont", "textfontsmall"):
            if val and val.lower() not in fonts:
                errors.append((rel, "font non definito: %s %r" % (key, val)))
        elif k in ("border", "border_default", "border_armed", "border_disabled", "border_override",
                   "activeborder_override", "normalborder_override"):
            if val and val.lower() not in borders:
                errors.append((rel, "bordo non definito: %s %r" % (key, val)))
        if hand:
            if k not in keys:
                errors.append((rel, "proprieta' mai usata nei file Valve: %r" % key))
            if k == "controlname" and val.lower() not in controls:
                errors.append((rel, "ControlName mai usato nei file Valve: %r" % val))
    for item in errors:
        msg = item[1]
        m = re.search(r": (\S+) '([^']*)'$", msg)
        if m and (m.group(1).lower(), m.group(2).lower()) in inherited and "non definito" in msg:
            warnings.append((rel, msg + " (ereditato dall'originale Valve)"))
        else:
            real_errors.append(item)
    errors = real_errors
    if hand:
        src = os.path.join(PRISTINE, rel)
        if os.path.exists(src):
            orig = element_names(vdf.parse(open(src, encoding="utf-8", errors="replace").read()))
            mine = element_names(nodes)
            lost = sorted(orig - mine)
            if lost:
                errors.append((rel, "elementi originali rimossi: %s" % ", ".join(lost[:12])))


def lint_animations(rel, text, names, errors):
    colors, base, fonts, borders = names
    depth = 0
    for i, line in enumerate(text.split("\n"), 1):
        s = re.sub(r"//.*", "", line).strip()
        if not s:
            continue
        depth += s.count("{") - s.count("}")
        if depth < 0:
            errors.append((rel, "riga %d: '}' senza apertura" % i))
            depth = 0
        toks = re.findall(r'"[^"]*"|\S+', s)
        if not toks or toks[0] in ("{", "}") or toks[0].lower() == "event":
            continue
        cmd = toks[0].lower()
        if cmd not in ANIM_COMMANDS:
            errors.append((rel, "riga %d: comando sconosciuto %r" % (i, toks[0])))
            continue
        if cmd == "animate" and len(toks) >= 4 and toks[2].lower().strip('"') in COLOR_VARS:
            v = toks[3].strip('"')
            if not re.match(r"^[\d. ]+$", v) and v.lower() not in colors and v.lower() not in base:
                errors.append((rel, "riga %d: colore non definito %r" % (i, v)))
            elif re.match(r"^[\d.]+ [\d. ]+$", v):
                errors.append((rel, "riga %d: colore letterale (usa un token) %r" % (i, v)))
        if cmd == "setfont" and len(toks) >= 3 and toks[2].strip('"').lower() not in fonts:
            errors.append((rel, "riga %d: font non definito %r" % (i, toks[2])))
    if depth:
        errors.append((rel, "parentesi graffe non bilanciate (%+d)" % depth))


def main():
    names = scheme_names()
    known = corpus()
    errors, warnings = [], []
    files = sorted(glob.glob(os.path.join(ROOT, "resource", "**", "*.res"), recursive=True) +
                   glob.glob(os.path.join(ROOT, "scripts", "**", "*.res"), recursive=True) +
                   glob.glob(os.path.join(ROOT, "servers", "**", "*.res"), recursive=True))
    hand_count = 0
    for p in files:
        rel = os.path.relpath(p, ROOT).replace("\\", "/")
        text = open(p, encoding="utf-8", errors="replace").read()
        if rel in SCHEMES:
            try:
                vdf.parse(text)
            except vdf.VDFError as e:
                errors.append((rel, "sintassi: %s" % e))
            continue
        hand = M.HAND_MARK in text[:400]
        hand_count += hand
        lint_res(rel, text, names, known, hand, errors, warnings)
    for p in glob.glob(os.path.join(ROOT, "scripts", "hudanimations_tf.txt")):
        rel = os.path.relpath(p, ROOT)
        lint_animations(rel, open(p, encoding="utf-8", errors="replace").read(), names, errors)
    by = defaultdict(list)
    for rel, msg in errors:
        by[rel].append(msg)
    for rel in sorted(by):
        print("ERRORE %s" % rel)
        for m in by[rel][:20]:
            print("   - %s" % m)
        if len(by[rel]) > 20:
            print("   ... +%d" % (len(by[rel]) - 20))
    if "-v" in sys.argv:
        for rel, msg in warnings:
            print("avviso %s: %s" % (rel, msg))
    print("\n%d file (.res) controllati, %d scritti a mano; %d errori, %d avvisi (eredita' Valve, -v per vederli)"
          % (len(files), hand_count, len(errors), len(warnings)))
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
