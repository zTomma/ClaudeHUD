// ClaudeHUD: migrato ai token (layout originale) - generato da tools/migrate.py
// modalita': light (DESIGN.md par. 9)
"Resource\UI\TFAdvancedOptionsDialog.res"
{
	"TFAdvancedOptionsDialog"
	{
		"ControlName"         	"EditablePanel"
		"fieldName"           	"TFAdvancedOptionsDialog"
		"xpos"                	"c-250"
		"ypos"                	"90"
		"wide"                	"500"
		"tall"                	"350"
		"autoResize"          	"0"
		"pinCorner"           	"0"
		"visible"             	"1"
		"enabled"             	"1"
		"tabPosition"         	"0"
		"bgcolor_override"    	"LtCard"
		"paintbackgroundtype" 	"2"
		"settitlebarvisible"  	""
		"paintborder"         	"1"
		"paintbackground"     	"0"
		"border"              	"GrayDialogBorder"
		"control_w"           	"500"
		"control_h"           	"25"
		"slider_w"            	"500"
		"slider_h"            	"25"
	}
	"TitleLabel"
	{
		"ControlName"      	"CExLabel"
		"fieldName"        	"TitleLabel"
		"font"             	"TypeHeading"
		"labelText"        	"#TF_AdvancedOptions"
		"textAlignment"    	"center"
		"xpos"             	"0"
		"ypos"             	"0"
		"zpos"             	"1"
		"wide"             	"500"
		"tall"             	"40"
		"autoResize"       	"0"
		"pinCorner"        	"0"
		"visible"          	"1"
		"enabled"          	"1"
		"fgcolor_override" 	"LtAccentText"
	}
	"CancelButton"
	{
		"ControlName"               	"CExButton"
		"fieldName"                 	"CancelButton"
		"xpos"                      	"150"
		"ypos"                      	"310"
		"zpos"                      	"1"
		"wide"                      	"100"
		"tall"                      	"25"
		"autoResize"                	"0"
		"pinCorner"                 	"3"
		"visible"                   	"1"
		"enabled"                   	"1"
		"tabPosition"               	"0"
		"labelText"                 	"#Cancel"
		"font"                      	"HudFontSmallBold"
		"textAlignment"             	"center"
		"dulltext"                  	"0"
		"brighttext"                	"0"
		"default"                   	"1"
		"Command"                   	"Close"
		"sound_depressed"           	"UI/buttonclick.wav"
		"sound_released"            	"UI/buttonclickrelease.wav"
		"defaultFgColor_override"   	"LtText"	// ClaudeHUD: colore esplicito in modalita' chiara
		"armedFgColor_override"     	"LtOnButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
		"depressedFgColor_override" 	"LtOnButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
		"defaultBgColor_override"   	"LtCardAlt"	// ClaudeHUD: colore esplicito in modalita' chiara
		"armedBgColor_override"     	"LtButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
		"depressedBgColor_override" 	"LtButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
	}
	"OkButton"
	{
		"ControlName"               	"CExButton"
		"fieldName"                 	"OkButton"
		"xpos"                      	"300"
		"ypos"                      	"310"
		"zpos"                      	"1"
		"wide"                      	"100"
		"tall"                      	"25"
		"autoResize"                	"0"
		"pinCorner"                 	"3"
		"visible"                   	"1"
		"enabled"                   	"1"
		"tabPosition"               	"0"
		"labelText"                 	"#GameUI_Ok"
		"font"                      	"HudFontSmallBold"
		"textAlignment"             	"center"
		"dulltext"                  	"0"
		"brighttext"                	"0"
		"default"                   	"1"
		"Command"                   	"Ok"
		"sound_depressed"           	"UI/buttonclick.wav"
		"sound_released"            	"UI/buttonclickrelease.wav"
		"defaultFgColor_override"   	"LtText"	// ClaudeHUD: colore esplicito in modalita' chiara
		"armedFgColor_override"     	"LtOnButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
		"depressedFgColor_override" 	"LtOnButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
		"defaultBgColor_override"   	"LtCardAlt"	// ClaudeHUD: colore esplicito in modalita' chiara
		"armedBgColor_override"     	"LtButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
		"depressedBgColor_override" 	"LtButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
	}
	"PanelListPanel"
	{
		"ControlName"      	"CPanelListPanel"
		"fieldName"        	"PanelListPanel"
		"xpos"             	"10"
		"ypos"             	"40"
		"wide"             	"480"
		"tall"             	"260"
		"autoResize"       	"0"
		"pinCorner"        	"0"
		"visible"          	"1"
		"enabled"          	"1"
		"tabPosition"      	"0"
		"bgcolor_override" 	"Clear"
	}
	"TooltipPanel"
	{
		"ControlName"         	"EditablePanel"
		"fieldName"           	"TooltipPanel"
		"xpos"                	"0"
		"ypos"                	"0"
		"zpos"                	"100"
		"wide"                	"240"
		"tall"                	"50"
		"visible"             	"0"
		"PaintBackgroundType" 	"2"
		"border"              	"MainMenuBGBorder"
		"TipLabel"
		{
			"ControlName"      	"CExLabel"
			"fieldName"        	"TipLabel"
			"font"             	"HudFontSmallest"
			"labelText"        	"%tiptext%"
			"textAlignment"    	"center"
			"xpos"             	"20"
			"ypos"             	"10"
			"zpos"             	"2"
			"wide"             	"200"
			"tall"             	"30"
			"autoResize"       	"0"
			"pinCorner"        	"0"
			"visible"          	"1"
			"enabled"          	"1"
			"fgcolor_override" 	"LtText"
			"wrap"             	"1"
		}
		"bgcolor_override"    	"LtCard"	// ClaudeHUD: riempimento al posto del bordo texture
	}
}
