// ClaudeHUD: migrato ai token (layout originale) - generato da tools/migrate.py
// modalita': light (DESIGN.md par. 9)
"Resource/UI/SaxxyAwards_SubmitForm.res"
{
	"SaxxySubmitForm"
	{
		"ControlName"         	"Frame"
		"fieldName"           	"SaxxySubmitForm"
		"xpos"                	"c-160"
		"ypos"                	"c-75"
		"wide"                	"320"
		"tall"                	"150"
		"autoResize"          	"0"
		"pinCorner"           	"0"
		"visible"             	"1"
		"enabled"             	"1"
		"tabPosition"         	"0"
		"PaintBackgroundType" 	"2"
		"bgcolor_override"    	"LtCardAlt"
	}
	"DirectionsLabel"
	{
		"ControlName"      	"CExLabel"
		"fieldName"        	"DirectionsLabel"
		"font"             	"HudFontSmallBold"
		"labelText"        	"#Replay_Contest_SubmitFormDirections"
		"textAlignment"    	"center"
		"xpos"             	"0"
		"ypos"             	"25"
		"zpos"             	"1"
		"wide"             	"320"
		"tall"             	"20"
		"autoResize"       	"0"
		"pinCorner"        	"0"
		"visible"          	"1"
		"enabled"          	"1"
		"wrap"             	"0"
		"fgcolor_override" 	"LtText"	// ClaudeHUD: colore esplicito in modalita' chiara
	}
	"URLInput"
	{
		"ControlName"           	"TextEntry"
		"fieldName"             	"URLInput"
		"maxchars"              	"255"
		"textHidden"            	"0"
		"textAlignment"         	"west"
		"unicode"               	"1"
		"wrap"                  	"0"
		"xpos"                  	"60"
		"ypos"                  	"55"
		"zpos"                  	"1"
		"wide"                  	"200"
		"tall"                  	"15"
		"autoResize"            	"0"
		"pinCorner"             	"0"
		"visible"               	"1"
		"enabled"               	"1"
		"tabPosition"           	"0"
		"fgcolor_override"      	"LtText"
		"bgcolor_override"      	"LtButtonHover"
		"Font"                  	"HudFontSmallestBold"
		"selectallonfirstfocus" 	"1"
	}
	"CategoryCombo"
	{
		"ControlName"      	"ComboBox"
		"fieldName"        	"CategoryCombo"
		"textAlignment"    	"west"
		"wrap"             	"0"
		"xpos"             	"60"
		"ypos"             	"75"
		"zpos"             	"1"
		"wide"             	"200"
		"tall"             	"15"
		"autoResize"       	"0"
		"pinCorner"        	"0"
		"visible"          	"1"
		"enabled"          	"1"
		"dulltext"         	"0"
		"brighttext"       	"0"
		"tabPosition"      	"10"
		"editable"         	"0"
		"fgcolor_override" 	"LtText"
		"bgcolor_override" 	"LtButtonHover"
		"Font"             	"HudFontSmallestBold"
	}
	"CancelButton"
	{
		"ControlName"               	"CExButton"
		"fieldName"                 	"CancelButton"
		"xpos"                      	"20"
		"ypos"                      	"120"
		"zpos"                      	"1"
		"wide"                      	"90"
		"tall"                      	"20"
		"autoResize"                	"0"
		"pinCorner"                 	"0"
		"visible"                   	"1"
		"enabled"                   	"1"
		"tabPosition"               	"2"
		"labelText"                 	"#Replay_Cancel"
		"font"                      	"HudFontSmallBold"
		"textAlignment"             	"center"
		"textinsetx"                	"50"
		"dulltext"                  	"0"
		"brighttext"                	"1"
		"Command"                   	"cancel"
		"sound_depressed"           	"UI/buttonclick.wav"
		"sound_released"            	"UI/buttonclickrelease.wav"
		"defaultFgColor_override"   	"LtText"	// ClaudeHUD: colore esplicito in modalita' chiara
		"armedFgColor_override"     	"LtOnButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
		"depressedFgColor_override" 	"LtOnButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
		"defaultBgColor_override"   	"LtCardAlt"	// ClaudeHUD: colore esplicito in modalita' chiara
		"armedBgColor_override"     	"LtButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
		"depressedBgColor_override" 	"LtButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
	}
	"RulesButton"
	{
		"ControlName"               	"CExButton"
		"fieldName"                 	"RulesButton"
		"xpos"                      	"115"
		"ypos"                      	"120"
		"zpos"                      	"1"
		"wide"                      	"90"
		"tall"                      	"20"
		"autoResize"                	"0"
		"pinCorner"                 	"0"
		"visible"                   	"1"
		"enabled"                   	"1"
		"tabPosition"               	"2"
		"labelText"                 	"#Replay_Contest_Rules"
		"font"                      	"HudFontSmallBold"
		"textAlignment"             	"center"
		"textinsetx"                	"50"
		"dulltext"                  	"0"
		"brighttext"                	"1"
		"Command"                   	"rules"
		"sound_depressed"           	"UI/buttonclick.wav"
		"sound_released"            	"UI/buttonclickrelease.wav"
		"defaultFgColor_override"   	"LtText"	// ClaudeHUD: colore esplicito in modalita' chiara
		"armedFgColor_override"     	"LtOnButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
		"depressedFgColor_override" 	"LtOnButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
		"defaultBgColor_override"   	"LtCardAlt"	// ClaudeHUD: colore esplicito in modalita' chiara
		"armedBgColor_override"     	"LtButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
		"depressedBgColor_override" 	"LtButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
	}
	"SubmitButton"
	{
		"ControlName"               	"CExButton"
		"fieldName"                 	"SubmitButton"
		"xpos"                      	"210"
		"ypos"                      	"120"
		"zpos"                      	"1"
		"wide"                      	"90"
		"tall"                      	"20"
		"autoResize"                	"0"
		"pinCorner"                 	"0"
		"visible"                   	"1"
		"enabled"                   	"1"
		"tabPosition"               	"2"
		"labelText"                 	"#Replay_Contest_Submit"
		"font"                      	"HudFontSmallBold"
		"textAlignment"             	"center"
		"textinsetx"                	"50"
		"dulltext"                  	"0"
		"brighttext"                	"0"
		"Command"                   	"submit"
		"sound_depressed"           	"UI/buttonclick.wav"
		"sound_released"            	"UI/buttonclickrelease.wav"
		"defaultFgColor_override"   	"LtText"	// ClaudeHUD: colore esplicito in modalita' chiara
		"armedFgColor_override"     	"LtOnButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
		"depressedFgColor_override" 	"LtOnButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
		"defaultBgColor_override"   	"LtCardAlt"	// ClaudeHUD: colore esplicito in modalita' chiara
		"armedBgColor_override"     	"LtButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
		"depressedBgColor_override" 	"LtButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
	}
}
