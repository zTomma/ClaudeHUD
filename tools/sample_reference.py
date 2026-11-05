#!/usr/bin/env python3
"""
Re-sample the base palette from the reference screenshots.

The screenshots are not committed (they contain the Claude/Anthropic logos, see LICENSES.md):
put them in reference/ (git-ignored) with these names and run
    python3 tools/sample_reference.py reference
  1.png  hand + paper illustration on terracotta (1200x630)
  2.webp terracotta / sage / halftone illustration (1920x1080)
  3.png  logo + palette swatches with hex labels (800x600)
  4.webp "Less hype. More humanity." branding board (1694x1167)
  5.png  anthropic.com hero (1886x919)
Prints the median colour of every sampled region next to the value stored in tokens.py.
"""
import os
import statistics
import sys
from collections import Counter

from PIL import Image

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tokens as T  # noqa: E402

REGIONS = [
    # token, image, box (x0, y0, x1, y1)
    ("Ivory", "5.png", (900, 200, 1000, 300)),
    ("Pampas", "3.png", (170, 450, 380, 480)),
    ("Cloud", "3.png", (410, 450, 630, 480)),
    ("Ink", "5.png", (100, 750, 120, 760)),
    ("Terracotta", "5.png", (1330, 360, 1380, 400)),
    ("Terracotta", "3.png", (20, 450, 120, 480)),
    ("Coral", "4.webp", (640, 330, 740, 380)),
    ("Blush", "4.webp", (700, 1070, 1600, 1105)),
    ("Sage", "2.webp", (1000, 50, 1100, 150)),
    ("Green", "4.webp", (50, 960, 550, 972)),
]


def median(im, box):
    x0, y0, x1, y1 = box
    px = [im.getpixel((x, y)) for x in range(x0, x1) for y in range(y0, y1)]
    return tuple(int(statistics.median(p[i] for p in px)) for i in range(3))


def dominant(im, box, pred):
    x0, y0, x1, y1 = box
    c = Counter(p for p in (im.getpixel((x, y)) for x in range(x0, x1) for y in range(y0, y1)) if pred(p))
    return c.most_common(1)[0][0] if c else None


def main(folder):
    for token, name, box in REGIONS:
        im = Image.open(os.path.join(folder, name)).convert("RGB")
        got = median(im, box)
        print("%-11s %-7s median %s   tokens.py %s   %s" % (token, name, T.hexs(got), T.hexs(T.S[token]), "=" if got == T.S[token] else "DIFF"))
    im = Image.open(os.path.join(folder, "4.webp")).convert("RGB")
    steel = dominant(im, (560, 200, 830, 360), lambda p: p[2] > p[0] + 40 and p[2] > p[1] + 10)
    print("%-11s %-7s mode   %s   tokens.py %s" % ("Steel", "4.webp", T.hexs(steel), T.hexs(T.S["Steel"])))
    im = Image.open(os.path.join(folder, "2.webp")).convert("RGB")
    moss = dominant(im, (980, 560, 1900, 1070), lambda p: 60 < sum(p) < 330)
    print("%-11s %-7s mode   %s   tokens.py %s" % ("Moss", "2.webp", T.hexs(moss), T.hexs(T.S["Moss"])))


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "reference")
