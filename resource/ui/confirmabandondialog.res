// ClaudeHUD: migrato ai token (layout originale) - generato da tools/migrate.py
// modalita': light (DESIGN.md par. 9)
"Resource/UI/ConfirmDialogOptOut.res"
{
	"ConfirmDialog"
	{
		"ControlName"         	"Frame"
		"fieldName"           	"ConfirmDialog"
		"xpos"                	"c-150"
		"ypos"                	"140"
		"wide"                	"300"
		"tall"                	"250"
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
		"labelText"        	"#ConfirmTitle"
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
		"fgcolor_override" 	"LtText"	// ClaudeHUD: colore esplicito in modalita' chiara
	}
	"ExplanationLabel"
	{
		"ControlName"      	"CExLabel"
		"fieldName"        	"ExplanationLabel"
		"font"             	"HudFontSmallBold"
		"labelText"        	"%text%"
		"textAlignment"    	"center"
		"xpos"             	"40"
		"ypos"             	"45"
		"zpos"             	"1"
		"wide"             	"220"
		"tall"             	"130"
		"autoResize"       	"0"
		"pinCorner"        	"0"
		"visible"          	"1"
		"enabled"          	"1"
		"centerwrap"       	"1"
		"fgcolor_override" 	"LtAccentText"
	}
	"CancelButton"
	{
		"ControlName"               	"CExButton"
		"fieldName"                 	"CancelButton"
		"xpos"                      	"190"
		"ypos"                      	"185"
		"zpos"                      	"20"
		"wide"                      	"100"
		"tall"                      	"25"
		"autoResize"                	"0"
		"pinCorner"                 	"0"
		"visible"                   	"1"
		"enabled"                   	"1"
		"tabPosition"               	"0"
		"labelText"                 	"#Cancel"
		"font"                      	"HudFontSmallBold"
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
	"CancelButtonHintIcon"
	{
		"ControlName" 	"CSCHintIcon"
		"fieldName"   	"CancelButtonHintIcon"
		"xpos"        	"195"
		"ypos"        	"165"
		"zpos"        	"25"
		"wide"        	"25"
		"tall"        	"25"
		"visible"     	"1"
		"actionSet"   	"MenuControls"
		"actionName"  	"menu_cancel"
	}
	"ConfirmButton"
	{
		"ControlName"               	"CExButton"
		"fieldName"                 	"ConfirmButton"
		"xpos"                      	"10"
		"ypos"                      	"185"
		"zpos"                      	"20"
		"wide"                      	"175"
		"tall"                      	"25"
		"default"                   	"1"
		"autoResize"                	"0"
		"pinCorner"                 	"0"
		"visible"                   	"1"
		"enabled"                   	"1"
		"tabPosition"               	"0"
		"labelText"                 	"#ConfirmButtonText"
		"font"                      	"HudFontSmallBold"
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
	"ConfirmButtonHintIcon"
	{
		"ControlName" 	"CSCHintIcon"
		"fieldName"   	"ConfirmButtonHintIcon"
		"xpos"        	"15"
		"ypos"        	"165"
		"zpos"        	"25"
		"wide"        	"25"
		"tall"        	"25"
		"visible"     	"1"
		"actionSet"   	"MenuControls"
		"actionName"  	"menu_select"
	}
	"OptOutCheckbox"
	{
		"ControlName"               	"CheckButton"
		"fieldName"                 	"OptOutCheckbox"
		"xpos"                      	"0"
		"ypos"                      	"217"
		"zpos"                      	"2"
		"wide"                      	"300"
		"tall"                      	"25"
		"autoResize"                	"0"
		"pinCorner"                 	"0"
		"visible"                   	"1"
		"enabled"                   	"1"
		"tabPosition"               	"0"
		"labelText"                 	"#TF_Confirm_Opt_Out"
		"textAlignment"             	"center"
		"dulltext"                  	"0"
		"brighttext"                	"0"
		"wrap"                      	"0"
		"font"                      	"HudFontSmallest"
		"selected_fgcolor_override" 	"160 90 67 255"	// token: LtAccentText
		"fgcolor_override"          	"LtText"	// ClaudeHUD: colore esplicito in modalita' chiara
	}
}
