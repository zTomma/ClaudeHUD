#!/usr/bin/env python3
"""
Verify the bundled fonts against the rules in CLAUDE.md:
  * static TTF (no 'fvar' table), TrueType outlines
  * internal legacy family name (name ID 1) == the name used in ClientScheme "Fonts"
  * requested weight == OS/2 usWeightClass
  * digits 0-9 have identical advance width (tabular) in every font used for numbers
  * the Italian accented letters and every literal character typed in the HUD's .res
    files are present in every bundled font
Usage: python3 tools/check_fonts.py   (exit code 1 on failure)
"""
import glob
import os
import re
import sys

from fontTools.ttLib import TTFont

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import tokens as T  # noqa: E402

REQUIRED = "àèéìòùÀÈÉÌÒÙ0123456789%+-–—×·•:/'’…«»"


def literal_hud_chars():
    """Characters typed directly in labelText of the HUD files (not #localized / %dialog vars%)."""
    chars = set()
    for p in glob.glob(os.path.join(ROOT, "resource", "**", "*.res"), recursive=True) + \
            glob.glob(os.path.join(ROOT, "scripts", "**", "*.res"), recursive=True):
        txt = open(p, encoding="utf-8", errors="replace").read()
        if "ClaudeHUD" not in txt:
            continue  # only files authored for this HUD
        for v in re.findall(r'"labeltext"\s+"([^"]*)"', txt, re.I):
            if v.startswith("#") or re.fullmatch(r"%[^%]*%", v):
                continue
            chars.update(v)
    return chars


def main():
    fails = 0
    used = literal_hud_chars()
    need = set(REQUIRED) | used
    numeric_families = {fam for (fam, _w), *_ in [v for k, v in T.TYPE.items() if k.startswith("Num")]}
    for fname, family, weight, role in T.FONT_FILES:
        path = os.path.join(ROOT, "resource", "fonts", fname)
        if not os.path.exists(path):
            print("FAIL %s missing" % fname)
            fails += 1
            continue
        f = TTFont(path)
        name = f["name"]
        fam = str(name.getName(1, 3, 1, 0x409))
        cmap = f.getBestCmap()
        hm = f["hmtx"]
        widths = {hm[cmap[ord(d)]][0] for d in "0123456789"}
        missing = sorted(c for c in need if c.strip() and ord(c) not in cmap)
        checks = [
            ("statico (niente fvar)", "fvar" not in f),
            ("contorni TrueType (glyf)", "glyf" in f),
            ("nome famiglia interno = %r" % family, fam == family),
            ("peso %d = usWeightClass %d" % (weight, f["OS/2"].usWeightClass), weight == f["OS/2"].usWeightClass),
            ("cifre tabulari", len(widths) == 1 or family not in numeric_families),
            ("glifi richiesti presenti", not missing),
        ]
        status = all(ok for _, ok in checks)
        fails += not status
        print("%s %-34s (%s)" % ("OK  " if status else "FAIL", fname, role))
        for label, ok in checks:
            if not ok:
                print("       x %s%s" % (label, ("  missing: " + "".join(missing)) if "glifi" in label else ""))
        print("       famiglia=%r versione=%r cifre=%s" % (fam, str(name.getName(5, 3, 1, 0x409)), sorted(widths)))
    print("caratteri letterali usati nei .res della HUD: %s" % ("".join(sorted(used)) or "(nessuno)"))
    print("%d failure(s)" % fails)
    return fails


if __name__ == "__main__":
    sys.exit(1 if main() else 0)
