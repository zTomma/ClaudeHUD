// ClaudeHUD: migrato ai token (layout originale) - generato da tools/migrate.py
// modalita': light (DESIGN.md par. 9)
"Resource/UI/replaybrowser/confirmquitdlg.res"
{
	"confirmquitdlg"
	{
		"ControlName"         	"Frame"
		"fieldName"           	"confirmquitdlg"
		"xpos"                	"c-200"
		"ypos"                	"c-95"
		"wide"                	"400"
		"tall"                	"275"
		"autoResize"          	"0"
		"pinCorner"           	"0"
		"visible"             	"1"
		"enabled"             	"1"
		"tabPosition"         	"0"
		"settitlebarvisible"  	"0"
		"PaintBackgroundType" 	"0"
	}
	"BGPanel"
	{
		"ControlName"         	"EditablePanel"
		"fieldName"           	"BGPanel"
		"xpos"                	"25"
		"ypos"                	"0"
		"wide"                	"350"
		"tall"                	"190"
		"visible"             	"1"
		"PaintBackgroundType" 	"2"
		"bgcolor_override"    	"LtCardAlt"
	}
	"TitleLabel"
	{
		"ControlName"      	"CExLabel"
		"fieldName"        	"TitleLabel"
		"font"             	"TypeHeading"
		"labelText"        	"#Replay_ConfirmQuitTitle"
		"textAlignment"    	"north"
		"xpos"             	"0"
		"ypos"             	"15"
		"zpos"             	"1"
		"wide"             	"400"
		"tall"             	"50"
		"autoResize"       	"1"
		"pinCorner"        	"0"
		"visible"          	"1"
		"enabled"          	"1"
		"fgcolor_override" 	"LtAccentText"
	}
	"ExplanationLabel"
	{
		"ControlName"      	"CExLabel"
		"fieldName"        	"ExplanationLabel"
		"font"             	"HudFontSmall"
		"labelText"        	"#Replay_ConfirmQuit"
		"textAlignment"    	"north"
		"xpos"             	"10"
		"ypos"             	"45"
		"zpos"             	"1"
		"wide"             	"380"
		"tall"             	"100"
		"autoResize"       	"0"
		"pinCorner"        	"0"
		"visible"          	"1"
		"enabled"          	"1"
		"centerwrap"       	"1"
		"fgcolor_override" 	"LtText"	// ClaudeHUD: colore esplicito in modalita' chiara
	}
	"RenderButton"
	{
		"ControlName"               	"CExButton"
		"fieldName"                 	"RenderButton"
		"xpos"                      	"65"
		"ypos"                      	"90"
		"zpos"                      	"20"
		"wide"                      	"270"
		"tall"                      	"20"
		"autoResize"                	"0"
		"pinCorner"                 	"0"
		"visible"                   	"1"
		"enabled"                   	"1"
		"tabPosition"               	"0"
		"labelText"                 	"#Replay_RenderNow"
		"font"                      	"ReplayMediumSmall"
		"textAlignment"             	"center"
		"textinsetx"                	"50"
		"dulltext"                  	"0"
		"brighttext"                	"0"
		"Command"                   	"rendernow"
		"sound_depressed"           	"UI/buttonclick.wav"
		"sound_released"            	"UI/buttonclickrelease.wav"
		"defaultFgColor_override"   	"LtText"	// ClaudeHUD: colore esplicito in modalita' chiara
		"armedFgColor_override"     	"LtOnButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
		"depressedFgColor_override" 	"LtOnButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
		"defaultBgColor_override"   	"LtCardAlt"	// ClaudeHUD: colore esplicito in modalita' chiara
		"armedBgColor_override"     	"LtButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
		"depressedBgColor_override" 	"LtButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
	}
	"ReplaysButton"
	{
		"ControlName"               	"CExButton"
		"fieldName"                 	"ReplaysButton"
		"xpos"                      	"65"
		"ypos"                      	"115"
		"zpos"                      	"20"
		"wide"                      	"270"
		"tall"                      	"20"
		"autoResize"                	"0"
		"pinCorner"                 	"0"
		"visible"                   	"1"
		"enabled"                   	"1"
		"tabPosition"               	"0"
		"labelText"                 	"#Replay_TakeMeToReplays"
		"font"                      	"ReplayMediumSmall"
		"textAlignment"             	"center"
		"textinsetx"                	"50"
		"dulltext"                  	"0"
		"brighttext"                	"0"
		"Command"                   	"gotoreplays"
		"sound_depressed"           	"UI/buttonclick.wav"
		"sound_released"            	"UI/buttonclickrelease.wav"
		"defaultFgColor_override"   	"LtText"	// ClaudeHUD: colore esplicito in modalita' chiara
		"armedFgColor_override"     	"LtOnButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
		"depressedFgColor_override" 	"LtOnButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
		"defaultBgColor_override"   	"LtCardAlt"	// ClaudeHUD: colore esplicito in modalita' chiara
		"armedBgColor_override"     	"LtButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
		"depressedBgColor_override" 	"LtButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
	}
	"QuitButton"
	{
		"ControlName"               	"CExButton"
		"fieldName"                 	"QuitButton"
		"xpos"                      	"65"
		"ypos"                      	"140"
		"zpos"                      	"20"
		"wide"                      	"270"
		"tall"                      	"20"
		"autoResize"                	"0"
		"pinCorner"                 	"0"
		"visible"                   	"1"
		"enabled"                   	"1"
		"tabPosition"               	"0"
		"labelText"                 	"#Replay_YesReallyQuit"
		"font"                      	"ReplayMediumSmall"
		"textAlignment"             	"center"
		"textinsetx"                	"50"
		"dulltext"                  	"0"
		"brighttext"                	"0"
		"Command"                   	"quit"
		"sound_depressed"           	"UI/buttonclick.wav"
		"sound_released"            	"UI/buttonclickrelease.wav"
		"defaultFgColor_override"   	"LtText"	// ClaudeHUD: colore esplicito in modalita' chiara
		"armedFgColor_override"     	"LtOnButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
		"depressedFgColor_override" 	"LtOnButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
		"defaultBgColor_override"   	"LtCardAlt"	// ClaudeHUD: colore esplicito in modalita' chiara
		"armedBgColor_override"     	"LtButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
		"depressedBgColor_override" 	"LtButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
	}
	"DontShowThisAgainCheckbox"
	{
		"ControlName"      	"CheckButton"
		"fieldName"        	"DontShowThisAgainCheckbox"
		"labelText"        	"#Replay_DontShowThisAgain"
		"Font"             	"ItemFontAttribSmall"
		"textAlignment"    	"west"
		"wrap"             	"0"
		"xpos"             	"130"
		"ypos"             	"165"
		"zpos"             	"1"
		"wide"             	"200"
		"tall"             	"20"
		"autoResize"       	"0"
		"pinCorner"        	"0"
		"visible"          	"1"
		"enabled"          	"1"
		"dulltext"         	"0"
		"brighttext"       	"0"
		"tabPosition"      	"10"
		"fgcolor_override" 	"LtText"	// ClaudeHUD: colore esplicito in modalita' chiara
	}
}
