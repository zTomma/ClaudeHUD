#!/usr/bin/env python3
"""Generate resource/ui/hudobjectivetimepanel.res - shared by the round timer and both KOTH timers."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, os.path.dirname(HERE)); import tokens as T

def hidden_img(name, ctl):
    return '''	"%s"
	{
		"ControlName"	"%s"
		"fieldName"		"%s"
		"xpos"			"0"
		"ypos"			"0"
		"zpos"			"0"
		"wide"			"0"
		"tall"			"0"
		"visible"		"0"
		"enabled"		"1"
		"image"			""
		"scaleImage"	"1"
	}
''' % (name, ctl, name)

def chip_label(name, text, color):
    return '''	"%s"
	{
		"ControlName"	"CExLabel"
		"fieldName"		"%s"
		"xpos"			"0"
		"ypos"			"32"
		"zpos"			"5"
		"wide"			"80"
		"tall"			"16"
		"visible"		"0"
		"enabled"		"1"
		"labelText"		"%s"
		"textAlignment"	"center"
		"dulltext"		"0"
		"brighttext"	"0"
		"wrap"			"0"
		"allcaps"		"1"
		"font"			"TypeLabel"
		"fgcolor"		"%s"
		"paintbackground"		"1"
		"paintbackgroundtype"	"2"
		"bgcolor_override"		"DkCard"
	}
''' % (name, name, text, color)

out = ['''// ClaudeHUD: riscritto a mano (fase 4) - timer di round (anche i due timer KOTH).
// Scheda DkCard 80x28: tempo in NumL avorio + piccola torta di avanzamento; sotto, una chip con lo
// stato (Preparazione, Supplementari, Morte improvvisa...). Terracotta solo per supplementari e
// morte improvvisa. Le texture della HUD di default sono nascoste.
"Resource/UI/HudObjectiveTimePanel.res"
{
	"TimeCard"
	{
		"ControlName"			"EditablePanel"
		"fieldName"				"TimeCard"
		"xpos"					"0"
		"ypos"					"0"
		"zpos"					"1"
		"wide"					"80"
		"tall"					"28"
		"visible"				"1"
		"enabled"				"1"
		"paintbackground"		"1"
		"paintbackgroundtype"	"2"
		"bgcolor_override"		"DkCard"
	}
''' + hidden_img("TimePanelBG", "ScalableImagePanel").replace('"image"\t\t\t""\n\t\t"scaleImage"\t"1"\n', '"image"\t\t\t""\n') + '''	"TimePanelProgressBar"
	{
		"ControlName"		"CTFProgressBar"
		"fieldName"			"TimePanelProgressBar"
		"xpos"				"62"
		"ypos"				"7"
		"zpos"				"4"
		"wide"				"14"
		"tall"				"14"
		"visible"			"1"
		"enabled"			"1"
		"scaleImage"		"1"
		"image"				"../hud/objectives_timepanel_progressbar"
		"color_active"		"TimerProgress.Active"
		"color_inactive"	"TimerProgress.InActive"
		"color_warning"		"TimerProgress.Warning"
		"percent_warning"	"0.75"
	}
''']
for name, text, color in [("WaitingForPlayersLabel", "#game_WaitingForPlayers", "DkTextMuted"),
                          ("OvertimeLabel", "#game_Overtime", "DkAccent"),
                          ("SuddenDeathLabel", "#game_SuddenDeath", "DkAccent"),
                          ("SetupLabel", "#game_Setup", "DkTextMuted"),
                          ("ServerTimeLimitLabel", "%servertimeleft%", "DkTextMuted")]:
    out.append(chip_label(name, text, color))
for name in ("WaitingForPlayersBG", "OvertimeBG", "SuddenDeathBG", "SetupBG", "ServerTimeLimitLabelBG"):
    out.append(hidden_img(name, "CTFImagePanel"))
out.append("}\n")
open(os.path.join(ROOT, "resource/ui/hudobjectivetimepanel.res"), "w", newline="\n").write("".join(out))
print("ok")
