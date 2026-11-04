#!/usr/bin/env python3
"""Generate resource/ui/hudplayerhealth.res (hand-designed layout; repetitive status icons generated)."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, os.path.dirname(HERE)); import tokens as T

def lit(role): return '"%s"\t// token: %s' % (T.rgba_str(role), role)

# status icons: name -> (image, slot). Slots are 24 units apart on the row above the card.
ICONS = [
    ("PlayerStatusBleedImage", "../vgui/bleed_drop", 0), ("PlayerStatusHookBleedImage", "../vgui/bleed_drop_grapple", 0),
    ("PlayerStatusSlowed", "../vgui/slowed", 0),
    ("PlayerStatusMilkImage", "../vgui/bleed_drop", 1), ("PlayerStatusGasImage", "../vgui/covered_in_gas", 1),
    ("PlayerStatusMarkedForDeathImage", "../vgui/marked_for_death", 2), ("PlayerStatusMarkedForDeathSilentImage", "../vgui/marked_for_death", 2),
    ("PlayerStatus_SpyMarked", "", 2),
    ("PlayerStatus_MedicUberBulletResistImage", "../HUD/defense_buff_bullet_blue", 3), ("PlayerStatus_MedicUberBlastResistImage", "../HUD/defense_buff_explosion_blue", 3),
    ("PlayerStatus_MedicUberFireResistImage", "../HUD/defense_buff_fire_blue", 3), ("PlayerStatus_MedicSmallBulletResistImage", "../HUD/defense_buff_bullet_blue", 3),
    ("PlayerStatus_MedicSmallBlastResistImage", "../HUD/defense_buff_explosion_blue", 3), ("PlayerStatus_MedicSmallFireResistImage", "../HUD/defense_buff_fire_blue", 3),
    ("PlayerStatus_SoldierOffenseBuff", "../HUD/defense_buff_bullet_blue", 3), ("PlayerStatus_SoldierDefenseBuff", "../HUD/defense_buff_bullet_blue", 3),
    ("PlayerStatus_SoldierHealOnHitBuff", "../HUD/defense_buff_bullet_blue", 3), ("PlayerStatus_Parachute", "", 3),
    ("PlayerStatus_WheelOfDoom", "../signs/death_wheel_whammy", 4),
]
for rune in ("Strength", "Haste", "Regen", "Resist", "Vampire", "Reflect", "Precision", "Agility", "Knockout", "King", "Plague", "Supernova"):
    ICONS.append(("PlayerStatus_Rune" + rune, "../Effects/powerup_%s_hud" % rune.lower(), 4))
HIDDEN_BY_DEFAULT = {"PlayerStatus_SpyMarked", "PlayerStatus_Parachute"}

out = ['''// ClaudeHUD: riscritto a mano (fase 3) - scheda salute. DESIGN.md par. 2, 4, 5, 6.
// Struttura: riga icone di stato (y 0-20) + scheda DkCard 88x36 con il numero NumXL.
// Il Segno (barra terracotta a sinistra) appare solo sotto il 49%% di salute (animazioni).
"Resource/UI/HudPlayerHealth.res"
{
	"HudPlayerHealth"
	{
		"ControlName"				"EditablePanel"
		"fieldName"					"HudPlayerHealth"
		"xpos"						"12"
		"ypos"						"r76"
		"zpos"						"2"
		"wide"						"124"
		"tall"						"64"
		"visible"					"1"
		"enabled"					"1"
		"HealthBonusPosAdj"			"0"
		"HealthDeathWarning"		"0.49"
		"HealthDeathWarningColor"	"DkAccent"
	}
	"HealthCard"
	{
		"ControlName"			"EditablePanel"
		"fieldName"				"HealthCard"
		"xpos"					"0"
		"ypos"					"28"
		"zpos"					"1"
		"wide"					"88"
		"tall"					"36"
		"visible"				"1"
		"enabled"				"1"
		"paintbackground"		"1"
		"paintbackgroundtype"	"2"
		"bgcolor_override"		"DkCard"
	}
	"HealthSegno"
	{
		"ControlName"	"ImagePanel"
		"fieldName"		"HealthSegno"
		"xpos"			"0"
		"ypos"			"32"
		"zpos"			"6"
		"wide"			"2"
		"tall"			"28"
		"visible"		"1"
		"enabled"		"1"
		"alpha"			"0"
		"fillcolor"		%(accent)s
	}
	"PlayerStatusHealthImage"
	{
		"ControlName"	"ImagePanel"
		"fieldName"		"PlayerStatusHealthImage"
		"xpos"			"0"
		"ypos"			"0"
		"zpos"			"0"
		"wide"			"0"
		"tall"			"0"
		"visible"		"0"
		"enabled"		"0"
		"scaleImage"	"1"
	}
	"PlayerStatusHealthImageBG"
	{
		"ControlName"	"ImagePanel"
		"fieldName"		"PlayerStatusHealthImageBG"
		"xpos"			"0"
		"ypos"			"0"
		"zpos"			"0"
		"wide"			"0"
		"tall"			"0"
		"visible"		"0"
		"enabled"		"0"
		"image"			""
		"scaleImage"	"1"
	}
	"PlayerStatusHealthBonusImage"
	{
		"ControlName"	"ImagePanel"
		"fieldName"		"PlayerStatusHealthBonusImage"
		"xpos"			"0"
		"ypos"			"28"
		"zpos"			"0"
		"wide"			"0"
		"tall"			"0"
		"visible"		"0"
		"enabled"		"1"
		"image"			""
		"scaleImage"	"1"
	}
	"PlayerStatusHealthValue"
	{
		"ControlName"	"CExLabel"
		"fieldName"		"PlayerStatusHealthValue"
		"xpos"			"6"
		"ypos"			"28"
		"zpos"			"5"
		"wide"			"52"
		"tall"			"36"
		"visible"		"1"
		"enabled"		"1"
		"labelText"		"%%Health%%"
		"textAlignment"	"east"
		"font"			"NumXL"
		"fgcolor"		"DkText"
	}
	"PlayerStatusMaxHealthValue"
	{
		"ControlName"	"CExLabel"
		"fieldName"		"PlayerStatusMaxHealthValue"
		"xpos"			"62"
		"ypos"			"28"
		"zpos"			"6"
		"wide"			"24"
		"tall"			"27"
		"visible"		"1"
		"enabled"		"1"
		"labelText"		"%%MaxHealth%%"
		"textAlignment"	"south-west"
		"font"			"NumXS"
		"fgcolor"		"DkTextMuted"
	}
''' % {"accent": lit("DkAccent")}]
for name, image, slot in ICONS:
    out.append('''	"%s"
	{
		"ControlName"	"ImagePanel"
		"fieldName"		"%s"
		"xpos"			"%d"
		"ypos"			"0"
		"zpos"			"7"
		"wide"			"20"
		"tall"			"20"
		"visible"		"%s"
		"enabled"		"1"
		"scaleImage"	"1"
		"image"			"%s"
	}
''' % (name, name, slot * 24, "0" if name in HIDDEN_BY_DEFAULT else "1", image))
out.append("}\n")
open(os.path.join(ROOT, "resource/ui/hudplayerhealth.res"), "w", newline="\n").write("".join(out))
print("ok", len(ICONS), "status icons")
