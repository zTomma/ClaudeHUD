// ClaudeHUD: migrato ai token (layout originale) - generato da tools/migrate.py
// modalita': light (DESIGN.md par. 9)
"Resource/UI/SupportNotificationDialog.res"
{
	"ConfirmDialog"
	{
		"ControlName"         	"Frame"
		"fieldName"           	"ConfirmDialog"
		"wide"                	"564"
		"tall"                	"387"	// Bottom of confirm button + 10 margin
		"autoResize"          	"0"
		"pinCorner"           	"0"
		"visible"             	"1"
		"enabled"             	"1"
		"tabPosition"         	"0"
		"settitlebarvisible"  	"0"
		"PaintBackgroundType" 	"0"
		"paintbackground"     	"1"
		"bgcolor_override"    	"Clear"
	}
	"TitleLabel"
	{
		"ControlName"          	"CExLabel"
		"fieldName"            	"ComptTitleLabel"
		"font"                 	"HudFontSmallBold"
		"labelText"            	"#TF_Support_Message_Title"
		"textAlignment"        	"north"
		"proportionalToParent" 	"1"
		"xpos"                 	"cs-0.5"
		"ypos"                 	"15"
		"zpos"                 	"1"
		"wide"                 	"p0.9"
		"tall"                 	"14"
		"autoResize"           	"0"
		"pinCorner"            	"0"
		"visible"              	"1"
		"enabled"              	"1"
		"centerwrap"           	"1"
		"fgcolor_override"     	"StoreGreen"
	}
	"MessageLabel"
	{
		"ControlName"          	"CExLabel"
		"fieldName"            	"SectionOneTextLabel"
		"font"                 	"HudFontSmallest"
		"labelText"            	"%text%"	// Filled with the CS message
		"textAlignment"        	"north"
		"proportionalToParent" 	"1"
		"xpos"                 	"cs-0.5"
		"ypos"                 	"47"	// 2 margin
		"zpos"                 	"1"
		"wide"                 	"p0.9"
		"tall"                 	"301"	// Size 11 font - 27 rows & change
		"autoResize"           	"0"
		"pinCorner"            	"0"
		"visible"              	"1"
		"enabled"              	"1"
		"wrap"                 	"1"
		"fgcolor_override"     	"LtText"
	}
	"ShowLaterButton"
	{
		"ControlName"               	"CExButton"
		"fieldName"                 	"ShowLaterButton"
		"proportionalToParent"      	"1"
		"xpos"                      	"rs1-10"
		"ypos"                      	"352"	// 4 margin
		"zpos"                      	"20"
		"wide"                      	"150"
		"tall"                      	"25"
		"default"                   	"1"
		"autoResize"                	"0"
		"pinCorner"                 	"0"
		"visible"                   	"1"
		"enabled"                   	"1"
		"tabPosition"               	"0"
		"labelText"                 	"#TF_Support_Message_Show_Later"
		"font"                      	"EconFontSmall"
		"textAlignment"             	"center"
		"textinsetx"                	"50"
		"dulltext"                  	"0"
		"brighttext"                	"0"
		"Command"                   	"show_later"
		"sound_depressed"           	"UI/buttonclick.wav"
		"sound_released"            	"UI/buttonclickrelease.wav"
		"border_default"            	"Econ.Button.Border.Default"
		"border_armed"              	"Econ.Button.Border.Armed"
		"armedBgColor_override"     	"LtAccent"
		"armedFgColor_override"     	"LtText"
		"depressedBgColor_override" 	"LtAccent"
		"depressedFgColor_override" 	"LtText"
		"defaultFgColor_override"   	"LtText"	// ClaudeHUD: colore esplicito in modalita' chiara
		"armedFgColor_override"     	"LtOnButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
		"depressedFgColor_override" 	"LtOnButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
		"defaultBgColor_override"   	"LtCardAlt"	// ClaudeHUD: colore esplicito in modalita' chiara
		"armedBgColor_override"     	"LtButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
		"depressedBgColor_override" 	"LtButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
	}
	"ConfirmButton"
	{
		"ControlName"               	"CExButton"
		"fieldName"                 	"ConfirmButton"
		"proportionalToParent"      	"1"
		"xpos"                      	"rs1-170"
		"ypos"                      	"352"	// 4 margin
		"zpos"                      	"20"
		"wide"                      	"150"
		"tall"                      	"25"
		"default"                   	"1"
		"autoResize"                	"0"
		"pinCorner"                 	"0"
		"visible"                   	"1"
		"enabled"                   	"1"
		"tabPosition"               	"0"
		"labelText"                 	"#TF_Support_Message_Acknowledge"
		"font"                      	"EconFontSmall"
		"textAlignment"             	"center"
		"textinsetx"                	"50"
		"dulltext"                  	"0"
		"brighttext"                	"0"
		"Command"                   	"acknowledge"
		"sound_depressed"           	"UI/buttonclick.wav"
		"sound_released"            	"UI/buttonclickrelease.wav"
		"border_default"            	"Econ.Button.Border.Default"
		"border_armed"              	"Econ.Button.Border.Armed"
		"armedBgColor_override"     	"LtRedFill"
		"defaultBgColor_override"   	"LtAccent"
		"defaultFgColor_override"   	"LtText"	// ClaudeHUD: colore esplicito in modalita' chiara
		"armedFgColor_override"     	"LtOnButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
		"depressedFgColor_override" 	"LtOnButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
	}
}
