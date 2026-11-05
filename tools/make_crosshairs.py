#!/usr/bin/env python3
"""
ClaudeHUD crosshairs: five original geometric shapes, written straight to Valve's texture format.

How the game uses them (verified in the TF2 client source, tf_hud_crosshair.cpp): `cl_crosshair_file X`
loads the material "vgui/crosshairs/X", draws it tinted with cl_crosshair_red/green/blue, 64x64 px at
cl_crosshair_scale 32 (size = 2 x scale). So every texture is WHITE with the shape in the alpha channel,
64x64, drawn 1:1 at the default scale; strokes of 2 px centred on the texture centre stay sharp.

Output (DESIGN.md par. 8 and 11):
  materials/vgui/crosshairs/claudehud_<name>.vtf   VTF 7.2, BGRA8888, 1 mip, no thumbnail,
                                                   flags NoMip | NoLOD | ClampS | ClampT | EightBitAlpha
  materials/vgui/crosshairs/claudehud_<name>.vmt   UnlitGeneric, $translucent $vertexcolor $vertexalpha $ignorez
  tools/crosshairs/claudehud_<name>.png            the same image as PNG (fallback: convert with VTFEdit,
                                                   RGBA8888/BGRA8888, same flags, if the .vtf is not read)
  docs/crosshairs.png                              preview, tinted with the six colours of Personalizza

Header layout from public/vtf/vtf.h (Source SDK 2013): VTFFileHeaderV7_2_t, packed, 80-byte header.
"""
import os
import struct
import sys

from PIL import Image, ImageDraw

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import tokens as T  # noqa: E402

SIZE = 64
SS = 8                      # supersampling for anti-aliased edges
IMAGE_FORMAT_BGRA8888 = 12  # public/bitmap/imageformat.h
IMAGE_FORMAT_UNKNOWN = -1
FLAGS = 0x4 | 0x8 | 0x100 | 0x200 | 0x2000   # CLAMPS CLAMPT NOMIP NOLOD EIGHTBITALPHA (public/vtf/vtf.h)
MAT_DIR = os.path.join(ROOT, "materials", "vgui", "crosshairs")
PNG_DIR = os.path.join(HERE, "crosshairs")


# ------------------------------------------------------------------------------------------ shapes
def canvas():
    im = Image.new("L", (SIZE * SS, SIZE * SS), 0)
    return im, ImageDraw.Draw(im)


def px(v):
    """texture coordinate (centre of the texture = 32.0, a pixel corner) -> supersampled pixels"""
    return int(round(v * SS))


def rect(d, x0, y0, x1, y1):
    d.rectangle([px(x0), px(y0), px(x1) - 1, px(y1) - 1], fill=255)


def disc(d, cx, cy, r):
    d.ellipse([px(cx - r), px(cy - r), px(cx + r) - 1, px(cy + r) - 1], fill=255)


def ring(d, cx, cy, r_out, r_in):
    disc(d, cx, cy, r_out)
    d.ellipse([px(cx - r_in), px(cy - r_in), px(cx + r_in) - 1, px(cy + r_in) - 1], fill=0)


C = SIZE / 2  # 32.0


def punto(d):          # a dot, 4 px
    disc(d, C, C, 2.2)


def anello(d):         # ring 18 px, stroke 2, centre dot 2 px
    ring(d, C, C, 9, 7)
    disc(d, C, C, 1.2)


def croce(d):          # plus with an open centre: arms 6 px, stroke 2, gap 4
    for a, b in ((C - 10, C - 4), (C + 4, C + 10)):
        rect(d, a, C - 1, b, C + 1)
        rect(d, C - 1, a, C + 1, b)


def angoli(d):         # notebook photo corners around a 20 px square + centre dot
    lo, hi, arm = C - 10, C + 10, 5
    for x, sx in ((lo, 1), (hi, -1)):
        for y, sy in ((lo, 1), (hi, -1)):
            xa, xb = sorted((x, x + sx * arm))
            ya, yb = sorted((y, y + sy * arm))
            rect(d, xa, (y if sy > 0 else y - 2), xb, (y + 2 if sy > 0 else y))
            rect(d, (x if sx > 0 else x - 2), ya, (x + 2 if sx > 0 else x), yb)
    disc(d, C, C, 1.2)


def tacche(d):         # ruler ticks left, right and below + centre dot (a "T" without the top)
    rect(d, C - 12, C - 1, C - 5, C + 1)
    rect(d, C + 5, C - 1, C + 12, C + 1)
    rect(d, C - 1, C + 5, C + 1, C + 12)
    disc(d, C, C, 1.2)


SHAPES = (("punto", "Punto", punto), ("anello", "Anello", anello), ("croce", "Croce", croce),
          ("angoli", "Angoli", angoli), ("tacche", "Tacche", tacche))


def render(fn):
    im, d = canvas()
    fn(d)
    alpha = im.resize((SIZE, SIZE), Image.LANCZOS)
    rgba = Image.new("RGBA", (SIZE, SIZE), (255, 255, 255, 0))
    rgba.putalpha(alpha)
    return rgba


# ------------------------------------------------------------------------------------------ VTF / VMT
def vtf_bytes(rgba):
    w, h = rgba.size
    header = struct.pack(
        "<4s2iiHHIHH4x3f4xfiBiBBH",
        b"VTF\0", 7, 2, 80,                 # signature, version 7.2, headerSize
        w, h, FLAGS, 1, 0,                  # width, height, flags, numFrames, startFrame
        1.0, 1.0, 1.0,                      # reflectivity (between the two 4-byte pads)
        1.0,                                # bumpScale
        IMAGE_FORMAT_BGRA8888, 1,           # imageFormat, numMipLevels
        IMAGE_FORMAT_UNKNOWN, 0, 0,         # no low-res thumbnail
        1)                                  # depth
    assert len(header) == 65, len(header)
    header += b"\0" * (80 - len(header))
    r, g, b, a = rgba.split()
    data = Image.merge("RGBA", (b, g, r, a)).tobytes()   # BGRA, rows top to bottom
    return header + data


def read_vtf(blob):
    """Parse our own output back (self-test)."""
    f = struct.unpack("<4s2iiHHIHH4x3f4xfiBiBBH", blob[:65])
    sig, major, minor, hsize, w, h, flags, frames, start, _r1, _r2, _r3, bump, fmt, mips, lfmt, lw, lh, depth = f
    assert sig == b"VTF\0" and (major, minor) == (7, 2) and hsize == 80
    assert fmt == IMAGE_FORMAT_BGRA8888 and mips == 1 and lfmt == IMAGE_FORMAT_UNKNOWN and depth == 1
    assert len(blob) == hsize + w * h * 4, (len(blob), hsize + w * h * 4)
    return w, h, flags


VMT = """"UnlitGeneric"
{
	"$basetexture"	"vgui/crosshairs/claudehud_%s"
	"$translucent"	"1"
	"$vertexcolor"	"1"
	"$vertexalpha"	"1"
	"$ignorez"	"1"
	"$no_fullbright"	"1"
}
"""


def preview(images):
    """docs/crosshairs.png: each crosshair at the default scale, tinted with the Personalizza colours,
    on a dark and on a light strip (the game world can be either)."""
    names = [("Ivory", "Avorio"), ("Terracotta", "Terracotta"), ("Sage", "Salvia"), ("SteelLight", "Acciaio"),
             ("Blush", "Blush"), ("Green", "Verde")]
    cell = 72
    out = Image.new("RGB", (cell * len(names), cell * len(images) * 2), (0, 0, 0))
    for i, (key, im) in enumerate(images):
        for j, (col, _label) in enumerate(names):
            for k, bg in enumerate(((52, 50, 46), (176, 186, 190))):
                tile = Image.new("RGB", (cell, cell), bg)
                tint = Image.new("RGBA", im.size, tuple(T.S[col]) + (255,))
                tint.putalpha(im.split()[3])
                tile.paste(tint, ((cell - SIZE) // 2, (cell - SIZE) // 2), tint)
                out.paste(tile, (j * cell, (i * 2 + k) * cell))
    out = out.resize((out.width * 2, out.height * 2), Image.NEAREST)
    out.save(os.path.join(ROOT, "docs", "crosshairs.png"), optimize=True)


def main():
    os.makedirs(MAT_DIR, exist_ok=True)
    os.makedirs(PNG_DIR, exist_ok=True)
    images = []
    for key, _label, fn in SHAPES:
        im = render(fn)
        blob = vtf_bytes(im)
        read_vtf(blob)
        open(os.path.join(MAT_DIR, "claudehud_%s.vtf" % key), "wb").write(blob)
        open(os.path.join(MAT_DIR, "claudehud_%s.vmt" % key), "w", encoding="utf-8", newline="\n").write(VMT % key)
        im.save(os.path.join(PNG_DIR, "claudehud_%s.png" % key))
        images.append((key, im))
    preview(images)
    print("wrote %d crosshairs (VTF 7.2 BGRA8888 + VMT) in materials/vgui/crosshairs/" % len(images))


if __name__ == "__main__":
    main()
