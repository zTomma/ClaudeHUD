// ClaudeHUD: migrato ai token (layout originale) - generato da tools/migrate.py
// modalita': light (DESIGN.md par. 9)
"Resource/UI/VRCalibration.res"
{
	"Background"
	{
		"ControlName"      	"EditablePanel"
		"fieldName"        	"Background"
		"xpos"             	"0"
		"ypos"             	"0"
		"zpos"             	"-2"
		"wide"             	"f0"
		"tall"             	"480"
		"visible"          	"1"
		"bgcolor_override" 	"LtCard"
	}
	"MainLabelDropShadow"
	{
		"ControlName"   	"CExLabel"
		"fieldName"     	"MainLabelDropShadow"
		"font"          	"TypeTitle"
		"labelText"     	"#TF_VR_Calibration"
		"textAlignment" 	"center"
		"xpos"          	"2"
		"ypos"          	"77"
		"wide"          	"f0"
		"tall"          	"35"
		"fgcolor"       	"LtText"
	}
	"MainLabel"
	{
		"ControlName"   	"CExLabel"
		"fieldName"     	"MainLabel"
		"font"          	"TypeTitle"
		"labelText"     	"#TF_VR_Calibration"
		"textAlignment" 	"center"
		"xpos"          	"0"
		"ypos"          	"75"
		"wide"          	"f0"
		"tall"          	"35"
		"fgcolor"       	"LtText"
	}
	"LeftSquare"
	{
		"ControlName"      	"EditablePanel"
		"fieldName"        	"LeftSquare"
		"xpos"             	"c-200"
		"ypos"             	"130"
		"wide"             	"400"
		"tall"             	"30"
		"visible"          	"1"
		"bgcolor_override" 	"Clear"
		"IsActive"
		{
			"ControlName"      	"EditablePanel"
			"fieldName"        	"IsActive"
			"xpos"             	"0"
			"ypos"             	"0"
			"zpos"             	"-1"
			"wide"             	"f0"
			"tall"             	"f0"
			"visible"          	"0"
			"bgcolor_override" 	"LtCard"
		}
		"Label"
		{
			"ControlName"   	"CExLabel"
			"fieldName"     	"Label"
			"font"          	"ScoreboardMedium"
			"labelText"     	"%eyestats%"
			"textAlignment" 	"center"
			"xpos"          	"0"
			"ypos"          	"0"
			"wide"          	"400"
			"tall"          	"35"
			"visible"       	"1"
			"fgcolor"       	"LtText"
		}
	}
	"RightSquare"
	{
		"ControlName"      	"EditablePanel"
		"fieldName"        	"RightSquare"
		"xpos"             	"c-200"
		"ypos"             	"155"
		"wide"             	"400"
		"tall"             	"30"
		"visible"          	"1"
		"bgcolor_override" 	"Clear"
		"IsActive"
		{
			"ControlName"      	"EditablePanel"
			"fieldName"        	"IsActive"
			"xpos"             	"0"
			"ypos"             	"0"
			"zpos"             	"-1"
			"wide"             	"f0"
			"tall"             	"f0"
			"visible"          	"0"
			"bgcolor_override" 	"LtCard"
		}
		"Label"
		{
			"ControlName"   	"CExLabel"
			"fieldName"     	"Label"
			"font"          	"ScoreboardMedium"
			"labelText"     	"%eyestats%"
			"textAlignment" 	"center"
			"xpos"          	"0"
			"ypos"          	"0"
			"wide"          	"400"
			"tall"          	"35"
			"visible"       	"1"
			"fgcolor"       	"LtText"
		}
	}
	"IpdSquare"
	{
		"ControlName"      	"EditablePanel"
		"fieldName"        	"IpdSquare"
		"xpos"             	"c-200"
		"ypos"             	"180"
		"wide"             	"400"
		"tall"             	"35"
		"visible"          	"1"
		"bgcolor_override" 	"Clear"
		"IsActive"
		{
			"ControlName"      	"EditablePanel"
			"fieldName"        	"IsActive"
			"xpos"             	"0"
			"ypos"             	"0"
			"zpos"             	"-1"
			"wide"             	"f0"
			"tall"             	"f0"
			"visible"          	"0"
			"bgcolor_override" 	"LtCard"
		}
		"Label"
		{
			"ControlName"   	"CExLabel"
			"fieldName"     	"Label"
			"font"          	"ScoreboardMedium"
			"labelText"     	"%ipdstats%"
			"textAlignment" 	"center"
			"xpos"          	"0"
			"ypos"          	"0"
			"wide"          	"400"
			"tall"          	"35"
			"visible"       	"1"
			"fgcolor"       	"LtText"
		}
	}
	"LeftReliefSquare"
	{
		"ControlName"      	"EditablePanel"
		"fieldName"        	"LeftReliefSquare"
		"xpos"             	"c-200"
		"ypos"             	"175"
		"wide"             	"400"
		"tall"             	"35"
		"visible"          	"0"	// Hidden for now, since we don't do anything with it!
		"bgcolor_override" 	"Clear"
		"IsActive"
		{
			"ControlName"      	"EditablePanel"
			"fieldName"        	"IsActive"
			"xpos"             	"0"
			"ypos"             	"0"
			"zpos"             	"-1"
			"wide"             	"f0"
			"tall"             	"f0"
			"visible"          	"0"
			"bgcolor_override" 	"LtCard"
		}
		"Label"
		{
			"ControlName"   	"CExLabel"
			"fieldName"     	"Label"
			"font"          	"ScoreboardMedium"
			"labelText"     	"%eyerelief%"
			"textAlignment" 	"center"
			"xpos"          	"0"
			"ypos"          	"0"
			"wide"          	"400"
			"tall"          	"35"
			"visible"       	"1"
			"fgcolor"       	"LtText"
		}
	}
	"RightReliefSquare"
	{
		"ControlName"      	"EditablePanel"
		"fieldName"        	"RightReliefSquare"
		"xpos"             	"c-200"
		"ypos"             	"200"
		"wide"             	"400"
		"tall"             	"35"
		"visible"          	"0"	// Hidden for now, since we don't do anything with it!
		"bgcolor_override" 	"Clear"
		"IsActive"
		{
			"ControlName"      	"EditablePanel"
			"fieldName"        	"IsActive"
			"xpos"             	"0"
			"ypos"             	"0"
			"zpos"             	"-1"
			"wide"             	"f0"
			"tall"             	"f0"
			"visible"          	"0"
			"bgcolor_override" 	"LtCard"
		}
		"Label"
		{
			"ControlName"   	"CExLabel"
			"fieldName"     	"Label"
			"font"          	"ScoreboardMedium"
			"labelText"     	"%eyerelief%"
			"textAlignment" 	"center"
			"xpos"          	"0"
			"ypos"          	"0"
			"wide"          	"400"
			"tall"          	"35"
			"visible"       	"1"
			"fgcolor"       	"LtText"
		}
	}
	"MainLineInstruction"
	{
		"ControlName"   	"CExLabel"
		"fieldName"     	"MainLineInstruction"
		"font"          	"ScoreboardMedium"
		"labelText"     	"#TF_VR_MoveLine"	// Will be changed by code.
		"textAlignment" 	"center"
		"xpos"          	"0"
		"ypos"          	"215"
		"wide"          	"f0"
		"tall"          	"70"
		"fgcolor"       	"LtText"
	}
	"MainInstruction"
	{
		"ControlName"   	"CExLabel"
		"fieldName"     	"MainInstruction"
		"font"          	"ScoreboardMedium"
		"labelText"     	"#TF_VR_UseControls"
		"textAlignment" 	"center"
		"xpos"          	"0"
		"ypos"          	"275"
		"wide"          	"f0"
		"tall"          	"70"
		"fgcolor"       	"LtText"
	}
	"LessLotsButton"
	{
		"ControlName"               	"CExImageButton"
		"fieldName"                 	"LessLotsButton"
		"font"                      	"ScoreboardMedium"
		"xpos"                      	"c-150"
		"ypos"                      	"340"
		"wide"                      	"60"
		"tall"                      	"25"
		"autoResize"                	"0"
		"visible"                   	"1"
		"enabled"                   	"1"
		"tabPosition"               	"0"
		"labelText"                 	"#TF_VR_LessLots"
		"font"                      	"HudFontSmallBold"
		"textAlignment"             	"center"
		"dulltext"                  	"0"
		"brighttext"                	"0"
		"default"                   	"1"
		"sound_depressed"           	"UI/buttonclick.wav"
		"sound_released"            	"UI/buttonclickrelease.wav"
		"image_drawcolor"           	"20 20 19 255"	// token: LtText
		"Command"                   	"adjust_less_lots"
		"defaultFgColor_override"   	"LtText"	// ClaudeHUD: colore esplicito in modalita' chiara
		"armedFgColor_override"     	"LtOnButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
		"depressedFgColor_override" 	"LtOnButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
		"defaultBgColor_override"   	"LtCardAlt"	// ClaudeHUD: colore esplicito in modalita' chiara
		"armedBgColor_override"     	"LtButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
		"depressedBgColor_override" 	"LtButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
	}
	"LessButton"
	{
		"ControlName"               	"CExImageButton"
		"fieldName"                 	"LessButton"
		"font"                      	"ScoreboardMedium"
		"xpos"                      	"c-70"
		"ypos"                      	"340"
		"wide"                      	"60"
		"tall"                      	"25"
		"autoResize"                	"0"
		"visible"                   	"1"
		"enabled"                   	"1"
		"tabPosition"               	"0"
		"labelText"                 	"#TF_VR_Less"
		"font"                      	"HudFontSmallBold"
		"textAlignment"             	"center"
		"dulltext"                  	"0"
		"brighttext"                	"0"
		"default"                   	"1"
		"sound_depressed"           	"UI/buttonclick.wav"
		"sound_released"            	"UI/buttonclickrelease.wav"
		"image_drawcolor"           	"20 20 19 255"	// token: LtText
		"Command"                   	"adjust_less"
		"defaultFgColor_override"   	"LtText"	// ClaudeHUD: colore esplicito in modalita' chiara
		"armedFgColor_override"     	"LtOnButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
		"depressedFgColor_override" 	"LtOnButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
		"defaultBgColor_override"   	"LtCardAlt"	// ClaudeHUD: colore esplicito in modalita' chiara
		"armedBgColor_override"     	"LtButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
		"depressedBgColor_override" 	"LtButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
	}
	"MoreButton"
	{
		"ControlName"               	"CExImageButton"
		"fieldName"                 	"MoreButton"
		"font"                      	"ScoreboardMedium"
		"xpos"                      	"c10"
		"ypos"                      	"340"
		"wide"                      	"60"
		"tall"                      	"25"
		"autoResize"                	"0"
		"visible"                   	"1"
		"enabled"                   	"1"
		"tabPosition"               	"0"
		"labelText"                 	"#TF_VR_More"
		"font"                      	"HudFontSmallBold"
		"textAlignment"             	"center"
		"dulltext"                  	"0"
		"brighttext"                	"0"
		"default"                   	"1"
		"sound_depressed"           	"UI/buttonclick.wav"
		"sound_released"            	"UI/buttonclickrelease.wav"
		"image_drawcolor"           	"20 20 19 255"	// token: LtText
		"Command"                   	"adjust_more"
		"defaultFgColor_override"   	"LtText"	// ClaudeHUD: colore esplicito in modalita' chiara
		"armedFgColor_override"     	"LtOnButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
		"depressedFgColor_override" 	"LtOnButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
		"defaultBgColor_override"   	"LtCardAlt"	// ClaudeHUD: colore esplicito in modalita' chiara
		"armedBgColor_override"     	"LtButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
		"depressedBgColor_override" 	"LtButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
	}
	"MoreLotsButton"
	{
		"ControlName"               	"CExImageButton"
		"fieldName"                 	"MoreLotsButton"
		"font"                      	"ScoreboardMedium"
		"xpos"                      	"c90"
		"ypos"                      	"340"
		"wide"                      	"60"
		"tall"                      	"25"
		"autoResize"                	"0"
		"visible"                   	"1"
		"enabled"                   	"1"
		"tabPosition"               	"0"
		"labelText"                 	"#TF_VR_MoreLots"
		"font"                      	"HudFontSmallBold"
		"textAlignment"             	"center"
		"dulltext"                  	"0"
		"brighttext"                	"0"
		"default"                   	"1"
		"sound_depressed"           	"UI/buttonclick.wav"
		"sound_released"            	"UI/buttonclickrelease.wav"
		"image_drawcolor"           	"20 20 19 255"	// token: LtText
		"Command"                   	"adjust_more_lots"
		"defaultFgColor_override"   	"LtText"	// ClaudeHUD: colore esplicito in modalita' chiara
		"armedFgColor_override"     	"LtOnButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
		"depressedFgColor_override" 	"LtOnButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
		"defaultBgColor_override"   	"LtCardAlt"	// ClaudeHUD: colore esplicito in modalita' chiara
		"armedBgColor_override"     	"LtButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
		"depressedBgColor_override" 	"LtButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
	}
	"NextButton"
	{
		"ControlName"               	"CExImageButton"
		"fieldName"                 	"NextButton"
		"font"                      	"ScoreboardMedium"
		"xpos"                      	"c-90"
		"ypos"                      	"380"
		"wide"                      	"80"
		"tall"                      	"25"
		"autoResize"                	"0"
		"visible"                   	"1"
		"enabled"                   	"1"
		"tabPosition"               	"0"
		"labelText"                 	"#TF_VR_NextAdjust"
		"font"                      	"HudFontSmallBold"
		"textAlignment"             	"center"
		"dulltext"                  	"0"
		"brighttext"                	"0"
		"default"                   	"1"
		"sound_depressed"           	"UI/buttonclick.wav"
		"sound_released"            	"UI/buttonclickrelease.wav"
		"image_drawcolor"           	"20 20 19 255"	// token: LtText
		"Command"                   	"adjust_next"
		"defaultFgColor_override"   	"LtText"	// ClaudeHUD: colore esplicito in modalita' chiara
		"armedFgColor_override"     	"LtOnButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
		"depressedFgColor_override" 	"LtOnButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
		"defaultBgColor_override"   	"LtCardAlt"	// ClaudeHUD: colore esplicito in modalita' chiara
		"armedBgColor_override"     	"LtButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
		"depressedBgColor_override" 	"LtButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
	}
	"CloseButton"
	{
		"ControlName"               	"CExImageButton"
		"fieldName"                 	"CloseButton"
		"font"                      	"ScoreboardMedium"
		"xpos"                      	"c10"
		"ypos"                      	"380"
		"wide"                      	"80"
		"tall"                      	"25"
		"autoResize"                	"0"
		"visible"                   	"1"
		"enabled"                   	"1"
		"tabPosition"               	"0"
		"labelText"                 	"#TF_VR_Close"
		"font"                      	"HudFontSmallBold"
		"textAlignment"             	"center"
		"dulltext"                  	"0"
		"brighttext"                	"0"
		"default"                   	"1"
		"sound_depressed"           	"UI/buttonclick.wav"
		"sound_released"            	"UI/buttonclickrelease.wav"
		"image_drawcolor"           	"20 20 19 255"	// token: LtText
		"Command"                   	"close"
		"defaultFgColor_override"   	"LtText"	// ClaudeHUD: colore esplicito in modalita' chiara
		"armedFgColor_override"     	"LtOnButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
		"depressedFgColor_override" 	"LtOnButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
		"defaultBgColor_override"   	"LtCardAlt"	// ClaudeHUD: colore esplicito in modalita' chiara
		"armedBgColor_override"     	"LtButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
		"depressedBgColor_override" 	"LtButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
	}
}
