#!/usr/bin/env python3
"""resource/ui/claudehud_fonttest.res - font test card shown in the main menu (phase 2 checkpoint).
Every type token with its size, digits 0-9, Italian accents and the symbols the HUD uses.
Disable it by removing the '#base "claudehud_fonttest.res"' line at the top of mainmenuoverride.res."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, os.path.dirname(HERE)); import tokens as T

from PIL import ImageFont
FILE_OF = {f[1]: f[0] for f in T.FONT_FILES}
MAX_W = 284  # units: the card is 300 wide (fits 4:3, see tools/layout_check.py)

def width_units(s, fam, tall):
    cell = 1.371 if fam.startswith("Source") else 1.300
    f = ImageFont.truetype(os.path.join(ROOT, "resource", "fonts", FILE_OF[fam]), 1000)
    return f.getlength(s) / 1000 * (tall / cell)

CANDIDATES = ["Àà èéìòù 0123456789 • × – — ← → %", "Àà èéìòù 0123456789 • × –", "Àè 0123456789", "Àè 0123", "Àè 01"]
x0, y, w = "c16", 52, "284"
items = []
for name, (fw, tall, role) in T.TYPE.items():
    text = None
    for sample in CANDIDATES:
        t = "%s %d  %s" % (name, tall, sample)
        if width_units(t, fw[0], tall) <= MAX_W:
            text = t
            break
    text = text or "%s %d" % (name, tall)
    items.append((name, text, tall))

out = ['''// ClaudeHUD: riscritto a mano (fase 2) - pannello di test dei font (mostrato nel menu principale).
// Ogni passo della scala tipografica con cifre, accenti e simboli usati dalla HUD.
// Per spegnerlo: togliere la riga #base "claudehud_fonttest.res" in cima a mainmenuoverride.res.
"Resource/UI/MainMenuOverride.res"
{
	"FontTestCard"
	{
		"ControlName"			"EditablePanel"
		"fieldName"				"FontTestCard"
		"xpos"					"c8"
		"ypos"					"64"
		"zpos"					"20"
		"wide"					"300"
		"tall"					"%d"
		"visible"				"1"
		"enabled"				"1"
		"paintbackground"		"1"
		"paintbackgroundtype"	"2"
		"bgcolor_override"		"LtCard"
	}
	"FontTestTitle"
	{
		"ControlName"	"CExLabel"
		"fieldName"		"FontTestTitle"
		"xpos"			"c16"
		"ypos"			"66"
		"zpos"			"21"
		"wide"			"284"
		"tall"			"12"
		"visible"		"1"
		"enabled"		"1"
		"labelText"		"ClaudeHUD · prova font (da spegnere dopo il test)"
		"textAlignment"	"west"
		"font"			"TypeLabel"
		"allcaps"		"1"
		"fgcolor"		"LtAccentText"
	}
''']
y = 80
for name, text, tall in items:
    h = tall + 2
    out.append('''	"FontTest_%s"
	{
		"ControlName"	"CExLabel"
		"fieldName"		"FontTest_%s"
		"xpos"			"%s"
		"ypos"			"%d"
		"zpos"			"21"
		"wide"			"%s"
		"tall"			"%d"
		"visible"		"1"
		"enabled"		"1"
		"labelText"		"%s"
		"textAlignment"	"west"
		"font"			"%s"
		"fgcolor"		"LtText"
	}
''' % (name, name, x0, y, w, h, text, name))
    y += h + 1
out[0] = out[0] % (y - 64 + 6)
out.append("}\n")
open(os.path.join(ROOT, "resource/ui/claudehud_fonttest.res"), "w", newline="\n").write("".join(out))
print("ok, card height", y - 64 + 6)
