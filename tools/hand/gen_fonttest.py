#!/usr/bin/env python3
"""resource/ui/claudehud_fonttest.res - font test card shown in the main menu (phase 2 checkpoint).
Every type token with its size, digits 0-9, Italian accents and the symbols the HUD uses.
Disable it by removing the '#base "claudehud_fonttest.res"' line at the top of mainmenuoverride.res."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, os.path.dirname(HERE)); import tokens as T

SAMPLE_BIG = "Àè 0123456789"
SAMPLE = "Àà èéìòù 0123456789 • × – — ← → % / :"
x0, y, w = "c24", 52, "396"
items = []
for name, (fw, tall, role) in T.TYPE.items():
    text = "%s %d  %s" % (name, tall, SAMPLE_BIG if tall >= 18 else SAMPLE)
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
		"xpos"					"c16"
		"ypos"					"64"
		"zpos"					"20"
		"wide"					"412"
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
		"xpos"			"c24"
		"ypos"			"66"
		"zpos"			"21"
		"wide"			"396"
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
