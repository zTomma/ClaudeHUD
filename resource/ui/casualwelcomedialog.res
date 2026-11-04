// ClaudeHUD: migrato ai token (layout originale) - generato da tools/migrate.py
// modalita': light (DESIGN.md par. 9)
"Resource/UI/CasualWelcomeDialog.res"
{
	"ConfirmDialog"
	{
		"ControlName"         	"Frame"
		"fieldName"           	"ConfirmDialog"
		"wide"                	"564"
		"tall"                	"200"	// Bottom of confirm button + 10 margin
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
	"CasualTitleLabel"
	{
		"ControlName"          	"CExLabel"
		"fieldName"            	"CasualTitleLabel"
		"font"                 	"HudFontSmallBold"
		"labelText"            	"#TF_Casual_Welcome_Title"
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
	"SubtitleLabel"
	{
		"ControlName"          	"CExLabel"
		"fieldName"            	"SubtitleLabel"
		"font"                 	"Link"
		"labelText"            	"#TF_Casual_Welcome_Subtitle"
		"textAlignment"        	"north"
		"proportionalToParent" 	"1"
		"xpos"                 	"cs-0.5"
		"ypos"                 	"29"
		"zpos"                 	"1"
		"wide"                 	"p0.9"
		"tall"                 	"14"
		"autoResize"           	"0"
		"pinCorner"            	"0"
		"visible"              	"1"
		"enabled"              	"1"
		"fgcolor_override"     	"LtText"
	}
	"SectionOneTitleLabel"
	{
		"ControlName"          	"CExLabel"
		"fieldName"            	"SectionOneTitleLabel"
		"font"                 	"HudFontSmallest"
		"labelText"            	"#TF_Casual_Welcome_Section_One_Title"
		"textAlignment"        	"north"
		"proportionalToParent" 	"1"
		"xpos"                 	"cs-0.5"
		"ypos"                 	"47"	// 4 margin
		"zpos"                 	"1"
		"wide"                 	"p0.9"
		"tall"                 	"11"
		"autoResize"           	"0"
		"pinCorner"            	"0"
		"visible"              	"1"
		"enabled"              	"1"
		"wrap"                 	"1"
		"fgcolor_override"     	"LtText"
	}
	"SectionOneTextLabel"
	{
		"ControlName"          	"CExLabel"
		"fieldName"            	"SectionOneTextLabel"
		"font"                 	"HudFontSmallest"
		"labelText"            	"#TF_Casual_Welcome_Section_One_Text"
		"textAlignment"        	"north"
		"proportionalToParent" 	"1"
		"xpos"                 	"cs-0.5"
		"ypos"                 	"60"	// 2 margin
		"zpos"                 	"1"
		"wide"                 	"p0.9"
		"tall"                 	"44"	// Size 11 font - 4 rows
		"autoResize"           	"0"
		"pinCorner"            	"0"
		"visible"              	"1"
		"enabled"              	"1"
		"wrap"                 	"1"
		"fgcolor_override"     	"LtTextMuted"
	}
	"SectionThreeTitleLabel"
	{
		"ControlName"          	"CExLabel"
		"fieldName"            	"SectionThreeTitleLabel"
		"font"                 	"HudFontSmallest"
		"labelText"            	"#TF_Casual_Welcome_Section_Three_Title"
		"textAlignment"        	"north"
		"proportionalToParent" 	"1"
		"xpos"                 	"cs-0.5"
		"ypos"                 	"108"	// 4 margin
		"zpos"                 	"1"
		"wide"                 	"p0.9"
		"tall"                 	"11"
		"autoResize"           	"0"
		"pinCorner"            	"0"
		"visible"              	"1"
		"enabled"              	"1"
		"wrap"                 	"1"
		"fgcolor_override"     	"LtText"
	}
	"SectionThreeTextLabel"
	{
		"ControlName"          	"CExLabel"
		"fieldName"            	"SectionThreeTextLabel"
		"font"                 	"HudFontSmallest"
		"labelText"            	"#TF_Casual_Welcome_Section_Three_Text"
		"textAlignment"        	"north"
		"proportionalToParent" 	"1"
		"xpos"                 	"cs-0.5"
		"ypos"                 	"121"	// 2 margin
		"zpos"                 	"1"
		"wide"                 	"p0.9"
		"tall"                 	"44"	// Size 11 font - 4 rows
		"autoResize"           	"0"
		"pinCorner"            	"0"
		"visible"              	"1"
		"enabled"              	"1"
		"wrap"                 	"1"
		"fgcolor_override"     	"LtTextMuted"
	}
	"TakeTourButton"
	{
		"ControlName"               	"CExButton"
		"fieldName"                 	"TakeTourButton"
		"proportionalToParent"      	"1"
		"xpos"                      	"rs1-170"
		"ypos"                      	"rs1-10"	// 10 margin
		"zpos"                      	"20"
		"wide"                      	"150"
		"tall"                      	"25"
		"default"                   	"1"
		"autoResize"                	"0"
		"pinCorner"                 	"0"
		"visible"                   	"1"
		"enabled"                   	"1"
		"tabPosition"               	"0"
		"labelText"                 	"#TF_MM_TakeUITour"
		"font"                      	"EconFontSmall"
		"textAlignment"             	"center"
		"textinsetx"                	"50"
		"dulltext"                  	"0"
		"brighttext"                	"0"
		"Command"                   	"show_explanations"
		"sound_depressed"           	"UI/buttonclick.wav"
		"sound_released"            	"UI/buttonclickrelease.wav"
		"border_default"            	"Econ.Button.Border.Default"
		"border_armed"              	"Econ.Button.Border.Armed"
		"armedBgColor_override"     	"LtAccent"
		"armedFgColor_override"     	"LtText"
		"depressedBgColor_override" 	"LtAccent"
		"depressedFgColor_override" 	"LtText"
		"defaultBgColor_override"   	"LtCardAlt"	// ClaudeHUD: riempimento al posto del bordo texture
		"armedBgColor_override"     	"LtButtonHover"	// ClaudeHUD: riempimento al posto del bordo texture
		"depressedBgColor_override" 	"LtButtonHover"	// ClaudeHUD: riempimento al posto del bordo texture
		"defaultFgColor_override"   	"LtText"	// ClaudeHUD: riempimento al posto del bordo texture
		"armedFgColor_override"     	"LtOnButtonHover"	// ClaudeHUD: riempimento al posto del bordo texture
		"depressedFgColor_override" 	"LtOnButtonHover"	// ClaudeHUD: riempimento al posto del bordo texture
	}
	"ConfirmButton"
	{
		"ControlName"               	"CExButton"
		"fieldName"                 	"ConfirmButton"
		"proportionalToParent"      	"1"
		"xpos"                      	"rs1-10"
		"ypos"                      	"rs1-10"	// 10 margin
		"zpos"                      	"20"
		"wide"                      	"150"
		"tall"                      	"25"
		"default"                   	"1"
		"autoResize"                	"0"
		"pinCorner"                 	"0"
		"visible"                   	"1"
		"enabled"                   	"1"
		"tabPosition"               	"0"
		"labelText"                 	"#TF_Competitive_Welcome_Confirm"
		"font"                      	"EconFontSmall"
		"textAlignment"             	"center"
		"textinsetx"                	"50"
		"dulltext"                  	"0"
		"brighttext"                	"0"
		"Command"                   	"confirm"
		"sound_depressed"           	"UI/buttonclick.wav"
		"sound_released"            	"UI/buttonclickrelease.wav"
		"border_default"            	"Econ.Button.Border.Default"
		"border_armed"              	"Econ.Button.Border.Armed"
		"armedBgColor_override"     	"LtAccent"
		"armedFgColor_override"     	"LtText"
		"depressedBgColor_override" 	"LtAccent"
		"depressedFgColor_override" 	"LtText"
		"defaultBgColor_override"   	"LtCardAlt"	// ClaudeHUD: riempimento al posto del bordo texture
		"armedBgColor_override"     	"LtButtonHover"	// ClaudeHUD: riempimento al posto del bordo texture
		"depressedBgColor_override" 	"LtButtonHover"	// ClaudeHUD: riempimento al posto del bordo texture
		"defaultFgColor_override"   	"LtText"	// ClaudeHUD: riempimento al posto del bordo texture
		"armedFgColor_override"     	"LtOnButtonHover"	// ClaudeHUD: riempimento al posto del bordo texture
		"depressedFgColor_override" 	"LtOnButtonHover"	// ClaudeHUD: riempimento al posto del bordo texture
	}
	"NeverShowAgainCheckBox"
	{
		"ControlName"          	"CheckButton"
		"fieldName"            	"NeverShowAgainCheckBox"
		"xpos"                 	"20"
		"ypos"                 	"rs1-10"	// 10 margin
		"zpos"                 	"-1"
		"wide"                 	"200"
		"tall"                 	"20"
		"font"                 	"HudFontSmall"
		"labelText"            	"#TF_Competitive_Welcome_DontShow"
		"proportionalToParent" 	"1"
	}
}
