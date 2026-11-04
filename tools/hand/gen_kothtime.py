#!/usr/bin/env python3
"""resource/ui/hudobjectivekothtimepanel.res: two timer cards, each with its team Segno; the active
timer gets a terracotta underline (ActiveTimerBG, moved by the code via blue/red_active_xpos)."""
import os, sys
from _patch import patch, lit, T
def mark(name, role):
    return '''"%s"
{
	"ControlName"	"ImagePanel"
	"fieldName"		"%s"
	"xpos"			"0"
	"ypos"			"4"
	"zpos"			"6"
	"wide"			"2"
	"tall"			"20"
	"visible"		"1"
	"enabled"		"1"
	"fillcolor"		"%s"	// token: %s
}''' % (name, name, T.rgba_str(role), role)
patch("resource/ui/hudobjectivekothtimepanel.res", {
    ("BlueTimer",): {"xpos": "0", "ypos": "8", "wide": "80", "tall": "52"},
    ("RedTimer",): {"xpos": "84", "ypos": "8", "wide": "80", "tall": "52"},
    ("BlueTimer", "TimePanelValue"): {"xpos": "2", "ypos": "0", "wide": "60", "tall": "28", "font": "NumL",
                                      "fgcolor": "DkText", "textAlignment": "center"},
    ("RedTimer", "TimePanelValue"): {"xpos": "2", "ypos": "0", "wide": "60", "tall": "28", "font": "NumL",
                                     "fgcolor": "DkText", "textAlignment": "center"},
    ("ActiveTimerBG",): {"xpos": "0", "ypos": "38", "wide": "80", "tall": "2", "visible": "0", "image": "",
                         "fillcolor": lit("DkAccent")},
}, add=[(("BlueTimer",), mark("TeamSegnoBlue", "DkBluFill")), (("RedTimer",), mark("TeamSegnoRed", "DkRedFill"))],
header="""ClaudeHUD: riscritto a mano (fase 4) - timer KOTH: due schede 80x28 affiancate, ognuna con il
Segno nel colore della squadra; il timer attivo e' sottolineato in terracotta (ActiveTimerBG).
Generato da tools/hand/gen_kothtime.py""")
print("ok")
