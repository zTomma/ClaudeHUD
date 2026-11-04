#!/usr/bin/env python3
"""
Verify every contrast contract declared in tools/tokens.py.

* Text/background pairs: WCAG 2.x contrast ratio. A background with alpha < 255 is
  composited over the worst case (pure white and pure black game world) and the lowest
  ratio is reported.
* Team pairs: luminance ratio between the two team colours plus CIEDE2000 distance under
  normal vision and simulated protanopia / deuteranopia / tritanopia
  (Machado, Oliveira & Fernandes 2009, severity 1.0, applied in linear RGB).

Usage: python3 tools/contrast.py [--markdown]
Exit code 1 if any contract fails.
"""
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tokens as T  # noqa: E402

MACHADO = {
    "protanopia": ((0.152286, 1.052583, -0.204868), (0.114503, 0.786281, 0.099216), (-0.003882, -0.048116, 1.051998)),
    "deuteranopia": ((0.367322, 0.860646, -0.227968), (0.280085, 0.672501, 0.047413), (-0.011820, 0.042940, 0.968881)),
    "tritanopia": ((1.255528, -0.076749, -0.178779), (-0.078411, 0.930809, 0.147602), (0.004733, 0.691367, 0.303900)),
}


def lin_to_srgb(v):
    v = max(0.0, min(1.0, v))
    return 255 * (12.92 * v if v <= 0.0031308 else 1.055 * v ** (1 / 2.4) - 0.055)


def simulate(rgb, kind):
    lin = [T.srgb_to_lin(c) for c in rgb]
    m = MACHADO[kind]
    out = [sum(m[i][j] * lin[j] for j in range(3)) for i in range(3)]
    return tuple(int(round(lin_to_srgb(v))) for v in out)


def to_lab(rgb):
    r, g, b = (T.srgb_to_lin(c) for c in rgb)
    x = (0.4124 * r + 0.3576 * g + 0.1805 * b) / 0.95047
    y = (0.2126 * r + 0.7152 * g + 0.0722 * b) / 1.0
    z = (0.0193 * r + 0.1192 * g + 0.9505 * b) / 1.08883

    def f(t):
        return t ** (1 / 3) if t > 216 / 24389 else (24389 / 27 * t + 16) / 116

    fx, fy, fz = f(x), f(y), f(z)
    return 116 * fy - 16, 500 * (fx - fy), 200 * (fy - fz)


def ciede2000(c1, c2):
    L1, a1, b1 = to_lab(c1)
    L2, a2, b2 = to_lab(c2)
    C1, C2 = math.hypot(a1, b1), math.hypot(a2, b2)
    Cm = (C1 + C2) / 2
    G = 0.5 * (1 - math.sqrt(Cm ** 7 / (Cm ** 7 + 25 ** 7)))
    a1p, a2p = (1 + G) * a1, (1 + G) * a2
    C1p, C2p = math.hypot(a1p, b1), math.hypot(a2p, b2)
    h1p = math.degrees(math.atan2(b1, a1p)) % 360
    h2p = math.degrees(math.atan2(b2, a2p)) % 360
    dLp, dCp = L2 - L1, C2p - C1p
    dhp = 0 if C1p * C2p == 0 else (h2p - h1p if abs(h2p - h1p) <= 180 else (h2p - h1p - 360 if h2p > h1p else h2p - h1p + 360))
    dHp = 2 * math.sqrt(C1p * C2p) * math.sin(math.radians(dhp / 2))
    Lpm, Cpm = (L1 + L2) / 2, (C1p + C2p) / 2
    if C1p * C2p == 0:
        hpm = h1p + h2p
    elif abs(h1p - h2p) <= 180:
        hpm = (h1p + h2p) / 2
    else:
        hpm = (h1p + h2p + 360) / 2 if h1p + h2p < 360 else (h1p + h2p - 360) / 2
    Tt = (1 - 0.17 * math.cos(math.radians(hpm - 30)) + 0.24 * math.cos(math.radians(2 * hpm))
          + 0.32 * math.cos(math.radians(3 * hpm + 6)) - 0.20 * math.cos(math.radians(4 * hpm - 63)))
    dtheta = 30 * math.exp(-(((hpm - 275) / 25) ** 2))
    Rc = 2 * math.sqrt(Cpm ** 7 / (Cpm ** 7 + 25 ** 7))
    Sl = 1 + 0.015 * (Lpm - 50) ** 2 / math.sqrt(20 + (Lpm - 50) ** 2)
    Sc, Sh = 1 + 0.045 * Cpm, 1 + 0.015 * Cpm * Tt
    Rt = -math.sin(math.radians(2 * dtheta)) * Rc
    return math.sqrt((dLp / Sl) ** 2 + (dCp / Sc) ** 2 + (dHp / Sh) ** 2 + Rt * (dCp / Sc) * (dHp / Sh))


def seen(role):
    """All colours a role can produce on screen (alpha composited over white/black)."""
    r, g, b, a = T.rgba(role)
    if a >= 255:
        return [(r, g, b)]
    return [T.composite((r, g, b), a / 255, (255, 255, 255)), T.composite((r, g, b), a / 255, (0, 0, 0))]


def run(markdown=False):
    fails = 0
    rows = []
    for fg, bg, minimum, note in T.CONTRACTS:
        fg_rgb = T.rgba(fg)[:3]
        ratio = min(T.contrast(fg_rgb, b) for b in seen(bg))
        ok = ratio >= minimum
        fails += not ok
        rows.append((fg, bg, ratio, minimum, ok, note))
    team = []
    for a, b, note in T.TEAM_PAIRS:
        ca, cb = T.rgba(a)[:3], T.rgba(b)[:3]
        lum = T.contrast(ca, cb)
        d = {"normale": ciede2000(ca, cb)}
        for kind in MACHADO:
            d[kind] = ciede2000(simulate(ca, kind), simulate(cb, kind))
        worst = min(d.values())
        ok = worst >= 20
        fails += not ok
        team.append((a, b, lum, d, ok, note))
    if markdown:
        out = ["| Testo | Sfondo | Rapporto | Minimo | Esito | Uso |", "|---|---|---:|---:|:-:|---|"]
        for fg, bg, ratio, minimum, ok, note in rows:
            out.append("| `%s` %s | `%s` %s | %.2f:1 | %.1f:1 | %s | %s |" % (
                fg, T.hexs(T.rgba(fg)), bg, T.hexs(T.rgba(bg)) + ("" if T.rgba(bg)[3] == 255 else " @%d%%" % round(T.rgba(bg)[3] / 2.55)),
                ratio, minimum, "OK" if ok else "**NO**", note))
        out += ["", "| Coppia squadre | Luminanza | ΔE2000 normale | protanopia | deuteranopia | tritanopia | Esito |",
                "|---|---:|---:|---:|---:|---:|:-:|"]
        for a, b, lum, d, ok, note in team:
            out.append("| `%s` %s / `%s` %s (%s) | %.2f:1 | %.1f | %.1f | %.1f | %.1f | %s |" % (
                a, T.hexs(T.rgba(a)), b, T.hexs(T.rgba(b)), note, lum, d["normale"], d["protanopia"],
                d["deuteranopia"], d["tritanopia"], "OK" if ok else "**NO**"))
        print("\n".join(out))
    else:
        for fg, bg, ratio, minimum, ok, note in rows:
            print("%-4s %-16s on %-14s %6.2f:1 (min %.1f)  %s" % ("OK" if ok else "FAIL", fg, bg, ratio, minimum, note))
        for a, b, lum, d, ok, note in team:
            print("%-4s %s vs %s  lum %.2f:1  dE2000 %s  (%s)" % ("OK" if ok else "FAIL", a, b, lum,
                  " ".join("%s=%.1f" % kv for kv in d.items()), note))
        print("\nderived colours:")
        for k, v in T.DERIVED.items():
            print("  %-15s %s  = %s" % (k, T.hexs(v["rgb"]), v["formula"]))
        print("\n%d failure(s)" % fails)
    return fails


if __name__ == "__main__":
    sys.exit(1 if run("--markdown" in sys.argv) else 0)
