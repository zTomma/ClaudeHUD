// ClaudeHUD: riscritto a mano (fase 4) - timer KOTH: due schede 80x28 affiancate, ognuna con il
// Segno nel colore della squadra; il timer attivo e' sottolineato in terracotta (ActiveTimerBG).
// Generato da tools/hand/gen_kothtime.py
"Resource/UI/HudObjectiveKothTimePanel.res"
{
	"HudKothTimeStatus"
	{
		"if_match"
		{
			"zpos" 	"5"
		}
	}
	"BlueTimer"
	{
		"ControlName"        	"CTFHudTimeStatus"
		"fieldName"          	"BlueTimer"
		"xpos"               	"0"
		"ypos"               	"8"
		"zpos"               	"2"
		"wide"               	"80"
		"tall"               	"52"
		"visible"            	"1"
		"enabled"            	"1"
		"delta_item_x"       	"22"
		"delta_item_start_y" 	"50"
		"delta_item_end_y"   	"70"
		"PositiveColor"      	"188 210 203 255"	// token: DkPositive
		"NegativeColor"      	"217 119 87 255"	// token: DkAccent
		"delta_lifetime"     	"1.5"
		"delta_item_font"    	"HudFontMedium"
		"if_match"
		{
			"proportionaltoparent" 	"1"
			"xpos"                 	"cs-0.5"
			"xpos_minmode"         	"cs-0.5"
			"ypos"                 	"0"
			"ypos_minmode"         	"0"
			"delta_item_x"         	"10"
			"delta_item_start_y"   	"12"
			"delta_item_end_y"     	"50"
			"PositiveColor"        	"DkPositive"
			"NegativeColor"        	"DkAccent"
			"delta_lifetime"       	"1.5"
			"delta_item_font"      	"HudFontMediumSmall"
		}
		"TimePanelValue"
		{
			"ControlName"   	"CExLabel"
			"fieldName"     	"TimePanelValue"
			"font"          	"NumL"
			"fgcolor"       	"DkText"
			"xpos"          	"2"
			"ypos"          	"0"
			"zpos"          	"3"
			"wide"          	"60"
			"tall"          	"28"
			"visible"       	"1"
			"enabled"       	"1"
			"textAlignment" 	"center"
			"labelText"     	"0:00"
			"if_match"
			{
				"proportionaltoparent" 	"1"
				"xpos"                 	"15"
				"xpos_minmode"         	"15"
				"ypos"                 	"12"
				"ypos_minmode"         	"12"
				"tall"                 	"10"
				"wide"                 	"35"
				"wide_minmode"         	"35"
				"font"                 	"HudFontSmall"
				"font_minmode"         	"HudFontSmall"
				"font_lodef"           	"HudFontSmall"
			}
		}
		"TeamSegnoBlue"
		{
			"ControlName" 	"ImagePanel"
			"fieldName"   	"TeamSegnoBlue"
			"xpos"        	"0"
			"ypos"        	"4"
			"zpos"        	"6"
			"wide"        	"2"
			"tall"        	"20"
			"visible"     	"1"
			"enabled"     	"1"
			"fillcolor"   	"16 88 137 255"	// token: DkBluFill
		}
	}
	"RedTimer"
	{
		"ControlName"        	"CTFHudTimeStatus"
		"fieldName"          	"RedTimer"
		"xpos"               	"84"
		"ypos"               	"8"
		"zpos"               	"2"
		"wide"               	"80"
		"tall"               	"52"
		"visible"            	"1"
		"enabled"            	"1"
		"delta_item_x"       	"22"
		"delta_item_start_y" 	"50"
		"delta_item_end_y"   	"70"
		"PositiveColor"      	"188 210 203 255"	// token: DkPositive
		"NegativeColor"      	"217 119 87 255"	// token: DkAccent
		"delta_lifetime"     	"1.5"
		"delta_item_font"    	"HudFontMedium"
		"if_match"
		{
			"proportionaltoparent" 	"1"
			"xpos"                 	"cs-0.5"
			"xpos_minmode"         	"cs-0.5"
			"ypos"                 	"0"
			"ypos_minmode"         	"0"
			"delta_item_x"         	"50"
			"delta_item_start_y"   	"12"
			"delta_item_end_y"     	"50"
			"PositiveColor"        	"DkPositive"
			"NegativeColor"        	"DkAccent"
			"delta_lifetime"       	"1.5"
			"delta_item_font"      	"HudFontMediumSmall"
		}
		"TimePanelValue"
		{
			"ControlName"   	"CExLabel"
			"fieldName"     	"TimePanelValue"
			"font"          	"NumL"
			"fgcolor"       	"DkText"
			"xpos"          	"2"
			"ypos"          	"0"
			"zpos"          	"3"
			"wide"          	"60"
			"tall"          	"28"
			"visible"       	"1"
			"enabled"       	"1"
			"textAlignment" 	"center"
			"labelText"     	"0:00"
			"if_match"
			{
				"proportionaltoparent" 	"1"
				"xpos"                 	"rs1-15"
				"xpos_minmode"         	"rs1-15"
				"ypos"                 	"12"
				"ypos_minmode"         	"12"
				"wide"                 	"35"
				"wide_minmode"         	"35"
				"tall"                 	"10"
				"font"                 	"HudFontSmall"
				"font_minmode"         	"HudFontSmall"
				"font_lodef"           	"HudFontSmall"
			}
		}
		"TeamSegnoRed"
		{
			"ControlName" 	"ImagePanel"
			"fieldName"   	"TeamSegnoRed"
			"xpos"        	"0"
			"ypos"        	"4"
			"zpos"        	"6"
			"wide"        	"2"
			"tall"        	"20"
			"visible"     	"1"
			"enabled"     	"1"
			"fillcolor"   	"217 119 87 255"	// token: DkRedFill
		}
	}
	"ActiveTimerBG"
	{
		"ControlName" 	"ImagePanel"
		"fieldName"   	"ActiveTimerBG"
		"xpos"        	"0"
		"ypos"        	"38"
		"zpos"        	"1"
		"wide"        	"80"
		"tall"        	"2"
		"visible"     	"0"
		"enabled"     	"1"
		"image"       	""
		"scaleImage"  	"1"
		"fillcolor"   	"217 119 87 255"	// token: DkAccent
	}
}
