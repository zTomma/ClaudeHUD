// ClaudeHUD: migrato ai token (layout originale) - generato da tools/migrate.py
// modalita': light (DESIGN.md par. 9)
"Resource/UI/YouTubeLoginDialog.res"
{
	"ConfirmDialog"
	{
		"ControlName"         	"Frame"
		"fieldName"           	"ConfirmDialog"
		"xpos"                	"c-150"
		"ypos"                	"75"
		"zpos"                	"1000"
		"wide"                	"300"
		"tall"                	"200"
		"autoResize"          	"0"
		"pinCorner"           	"0"
		"visible"             	"1"
		"enabled"             	"1"
		"tabPosition"         	"0"
		"settitlebarvisible"  	"0"
		"PaintBackgroundType" 	"0"
	}
	"TitleLabel"
	{
		"ControlName"      	"CExLabel"
		"fieldName"        	"TitleLabel"
		"font"             	"TypeHeading"
		"labelText"        	"#YouTube_LoginDlg_Title"
		"textAlignment"    	"north"
		"xpos"             	"0"
		"ypos"             	"15"
		"zpos"             	"1"
		"wide"             	"300"
		"tall"             	"20"
		"autoResize"       	"1"
		"pinCorner"        	"0"
		"visible"          	"1"
		"enabled"          	"1"
		"fgcolor_override" 	"LtAccentText"
	}
	"UserNameLabel"
	{
		"ControlName"      	"CExLabel"
		"fieldName"        	"UserNameLabel"
		"font"             	"EconFontSmall"
		"labelText"        	"#YouTube_LoginDlg_UserName"
		"textAlignment"    	"west"
		"xpos"             	"10"
		"ypos"             	"50"
		"zpos"             	"1"
		"wide"             	"150"
		"tall"             	"25"
		"autoResize"       	"0"
		"pinCorner"        	"0"
		"visible"          	"1"
		"enabled"          	"1"
		"fgcolor_override" 	"LtText"	// ClaudeHUD: colore esplicito in modalita' chiara
	}
	"UserNameTextEntry"
	{
		"ControlName"      	"TextEntry"
		"fieldName"        	"UserNameTextEntry"
		"maxchars"         	"255"
		"textHidden"       	"0"
		"textAlignment"    	"west"
		"unicode"          	"1"
		"wrap"             	"0"
		"xpos"             	"10"
		"ypos"             	"75"
		"zpos"             	"1"
		"wide"             	"280"
		"tall"             	"20"
		"autoResize"       	"0"
		"pinCorner"        	"0"
		"visible"          	"1"
		"enabled"          	"1"
		"tabPosition"      	"1"
		"fgcolor_override" 	"LtText"
		"bgcolor_override" 	"LtCardAlt"
		"Font"             	"ReplayBrowserSmallest"
	}
	"PasswordLabel"
	{
		"ControlName"      	"CExLabel"
		"fieldName"        	"PasswordLabel"
		"font"             	"EconFontSmall"
		"labelText"        	"#YouTube_LoginDlg_Password"
		"textAlignment"    	"west"
		"xpos"             	"10"
		"ypos"             	"100"
		"zpos"             	"1"
		"wide"             	"150"
		"tall"             	"25"
		"autoResize"       	"0"
		"pinCorner"        	"0"
		"visible"          	"1"
		"enabled"          	"1"
		"fgcolor_override" 	"LtText"	// ClaudeHUD: colore esplicito in modalita' chiara
	}
	"PasswordTextEntry"
	{
		"ControlName"      	"TextEntry"
		"fieldName"        	"PasswordTextEntry"
		"maxchars"         	"255"
		"textAlignment"    	"west"
		"unicode"          	"1"
		"wrap"             	"0"
		"xpos"             	"10"
		"ypos"             	"125"
		"zpos"             	"1"
		"wide"             	"280"
		"tall"             	"20"
		"autoResize"       	"0"
		"pinCorner"        	"0"
		"visible"          	"1"
		"enabled"          	"1"
		"tabPosition"      	"2"
		"textHidden"       	"1"
		"fgcolor_override" 	"LtText"
		"bgcolor_override" 	"LtCardAlt"
		"Font"             	"ReplayBrowserSmallest"
	}
	"RegisterButton"
	{
		"ControlName"               	"CExButton"
		"fieldName"                 	"RegisterButton"
		"xpos"                      	"10"
		"ypos"                      	"165"
		"zpos"                      	"20"
		"wide"                      	"85"
		"tall"                      	"25"
		"autoResize"                	"0"
		"pinCorner"                 	"0"
		"visible"                   	"1"
		"enabled"                   	"1"
		"tabPosition"               	"0"
		"labelText"                 	"#YouTube_LoginDlg_Register"
		"font"                      	"EconFontSmall"
		"textAlignment"             	"center"
		"textinsetx"                	"50"
		"dulltext"                  	"0"
		"brighttext"                	"0"
		"Command"                   	"register"
		"sound_depressed"           	"UI/buttonclick.wav"
		"sound_released"            	"UI/buttonclickrelease.wav"
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
		"xpos"                      	"100"
		"ypos"                      	"165"
		"zpos"                      	"20"
		"wide"                      	"95"
		"tall"                      	"25"
		"default"                   	"1"
		"autoResize"                	"0"
		"pinCorner"                 	"0"
		"visible"                   	"1"
		"enabled"                   	"1"
		"tabPosition"               	"0"
		"labelText"                 	"#YouTube_LoginDlg_Login"
		"font"                      	"EconFontSmall"
		"textAlignment"             	"center"
		"textinsetx"                	"50"
		"dulltext"                  	"0"
		"brighttext"                	"0"
		"Command"                   	"confirm"
		"sound_depressed"           	"UI/buttonclick.wav"
		"sound_released"            	"UI/buttonclickrelease.wav"
		"defaultFgColor_override"   	"LtText"	// ClaudeHUD: colore esplicito in modalita' chiara
		"armedFgColor_override"     	"LtOnButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
		"depressedFgColor_override" 	"LtOnButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
		"defaultBgColor_override"   	"LtCardAlt"	// ClaudeHUD: colore esplicito in modalita' chiara
		"armedBgColor_override"     	"LtButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
		"depressedBgColor_override" 	"LtButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
	}
	"CancelButton"
	{
		"ControlName"               	"CExButton"
		"fieldName"                 	"CancelButton"
		"xpos"                      	"200"
		"ypos"                      	"165"
		"zpos"                      	"20"
		"wide"                      	"95"
		"tall"                      	"25"
		"autoResize"                	"0"
		"pinCorner"                 	"0"
		"visible"                   	"1"
		"enabled"                   	"1"
		"tabPosition"               	"0"
		"labelText"                 	"#Cancel"
		"font"                      	"EconFontSmall"
		"textAlignment"             	"center"
		"textinsetx"                	"50"
		"dulltext"                  	"0"
		"brighttext"                	"0"
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
}
