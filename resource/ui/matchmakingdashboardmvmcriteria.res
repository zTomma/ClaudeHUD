// ClaudeHUD: migrato ai token (layout originale) - generato da tools/migrate.py
// modalita': light (DESIGN.md par. 9)
#base "MatchMakingDashboardSidePanel.res"
"Resource/UI/MatchMakingDashboardMvMCriteria.res"
{
	"MVMCriteria"
	{
		"fieldName"            	"MVMCriteria"
		"xpos"                 	"r0"
		"ypos"                 	"10"
		"zpos"                 	"1003"
		"wide"                 	"420"
		"tall"                 	"f70"
		"visible"              	"1"
		"proportionaltoparent" 	"1"
	}
	"criteria"
	{
		"ControlName"          	"CMVMCriteriaPanel"
		"fieldName"            	"criteria"
		"xpos"                 	"5"
		"ypos"                 	"15"
		"zpos"                 	"100"
		"wide"                 	"410"
		"tall"                 	"f50"
		"visible"              	"1"
		"proportionaltoparent" 	"1"
		"pinCorner"            	"2"
	}
	"BackButton"
	{
		"ControlName"               	"CExButton"
		"fieldName"                 	"BackButton"
		"xpos"                      	"6"
		"ypos"                      	"rs1-8"
		"zpos"                      	"100"
		"wide"                      	"90"
		"tall"                      	"20"
		"autoResize"                	"0"
		"pinCorner"                 	"3"
		"visible"                   	"1"
		"enabled"                   	"1"
		"tabPosition"               	"0"
		"font"                      	"TypeHeading"
		"textAlignment"             	"center"
		"dulltext"                  	"0"
		"brighttext"                	"0"
		"Command"                   	"back"
		"proportionaltoparent"      	"1"
		"labeltext"                 	"#TF_Matchmaking_Back"
		"mouseinputenabled"         	"1"
		"keyboardinputenabled"      	"0"
		"sound_depressed"           	"UI/buttonclick.wav"
		"sound_released"            	"UI/buttonclickrelease.wav"
		"defaultFgColor_override"   	"LtText"	// ClaudeHUD: colore esplicito in modalita' chiara
		"armedFgColor_override"     	"LtOnButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
		"depressedFgColor_override" 	"LtOnButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
		"defaultBgColor_override"   	"LtCardAlt"	// ClaudeHUD: colore esplicito in modalita' chiara
		"armedBgColor_override"     	"LtButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
		"depressedBgColor_override" 	"LtButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
	}
	"MannUpToolTipButtonHack"
	{
		"ControlName"                   	"EditablePanel"
		"fieldName"                     	"MannUpToolTipButtonHack"
		"xpos"                          	"106"
		"ypos"                          	"rs1-8"
		"zpos"                          	"101"
		"wide"                          	"170"
		"tall"                          	"20"
		"visible"                       	"0"
		"enabled"                       	"1"
		"mouseinputenabled"             	"1"
		"eatmouseinput"                 	"0"
		"showtooltipswhenmousedisabled" 	"1"
		"proportionaltoparent"          	"1"
	}
	"MannUpQueueButton"
	{
		"ControlName"               	"CExButton"
		"fieldName"                 	"MannUpQueueButton"
		"xpos"                      	"106"
		"ypos"                      	"rs1-8"
		"zpos"                      	"100"
		"wide"                      	"170"
		"tall"                      	"20"
		"autoResize"                	"0"
		"pinCorner"                 	"3"
		"visible"                   	"1"
		"enabled"                   	"1"
		"tabPosition"               	"0"
		"font"                      	"TypeHeading"
		"textAlignment"             	"center"
		"dulltext"                  	"0"
		"brighttext"                	"0"
		"Command"                   	"start_search"
		"proportionaltoparent"      	"1"
		"labeltext"                 	"#TF_Matchmaking_StartSearch"
		"mouseinputenabled"         	"1"
		"keyboardinputenabled"      	"0"
		"actionsignallevel"         	"1"
		"sound_depressed"           	"UI/buttonclick.wav"
		"sound_released"            	"UI/buttonclickrelease.wav"
		"armedBgColor_override"     	"LtPositive"
		"defaultBgColor_override"   	"LtPositive"
		"defaultFgColor_override"   	"LtText"	// ClaudeHUD: colore esplicito in modalita' chiara
		"armedFgColor_override"     	"LtOnButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
		"depressedFgColor_override" 	"LtOnButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
	}
	"BootCampToolTipButtonHack"
	{
		"ControlName"                   	"EditablePanel"
		"fieldName"                     	"BootCampToolTipButtonHack"
		"xpos"                          	"5"
		"ypos"                          	"rs1-8"
		"zpos"                          	"101"
		"wide"                          	"270"
		"tall"                          	"20"
		"visible"                       	"0"
		"enabled"                       	"1"
		"mouseinputenabled"             	"1"
		"eatmouseinput"                 	"0"
		"showtooltipswhenmousedisabled" 	"1"
		"proportionaltoparent"          	"1"
	}
	"BootCampQueueButton"
	{
		"ControlName"               	"CExButton"
		"fieldName"                 	"BootCampQueueButton"
		"xpos"                      	"5"
		"ypos"                      	"rs1-8"
		"zpos"                      	"100"
		"wide"                      	"270"
		"tall"                      	"20"
		"autoResize"                	"0"
		"pinCorner"                 	"3"
		"visible"                   	"1"
		"enabled"                   	"1"
		"tabPosition"               	"0"
		"font"                      	"TypeHeading"
		"textAlignment"             	"center"
		"dulltext"                  	"0"
		"brighttext"                	"0"
		"Command"                   	"start_search"
		"proportionaltoparent"      	"1"
		"labeltext"                 	"#TF_Matchmaking_StartSearch"
		"mouseinputenabled"         	"1"
		"keyboardinputenabled"      	"0"
		"actionsignallevel"         	"1"
		"sound_depressed"           	"UI/buttonclick.wav"
		"sound_released"            	"UI/buttonclickrelease.wav"
		"armedBgColor_override"     	"LtPositive"
		"defaultBgColor_override"   	"LtPositive"
		"defaultFgColor_override"   	"LtText"	// ClaudeHUD: colore esplicito in modalita' chiara
		"armedFgColor_override"     	"LtOnButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
		"depressedFgColor_override" 	"LtOnButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
	}
	"NextButton"
	{
		"ControlName"               	"CExButton"
		"fieldName"                 	"NextButton"
		"xpos"                      	"cs-0.5"
		"ypos"                      	"rs1-8"
		"zpos"                      	"100"
		"wide"                      	"f20"
		"tall"                      	"20"
		"autoResize"                	"0"
		"pinCorner"                 	"3"
		"visible"                   	"1"
		"enabled"                   	"1"
		"tabPosition"               	"0"
		"font"                      	"TypeHeading"
		"textAlignment"             	"center"
		"dulltext"                  	"0"
		"brighttext"                	"0"
		"Command"                   	"select_tour"
		"proportionaltoparent"      	"1"
		"labeltext"                 	"#TF_MvM_SelectChallenge"
		"mouseinputenabled"         	"1"
		"keyboardinputenabled"      	"0"
		"sound_depressed"           	"UI/buttonclick.wav"
		"sound_released"            	"UI/buttonclickrelease.wav"
		"defaultFgColor_override"   	"LtText"	// ClaudeHUD: colore esplicito in modalita' chiara
		"armedFgColor_override"     	"LtOnButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
		"depressedFgColor_override" 	"LtOnButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
		"defaultBgColor_override"   	"LtCardAlt"	// ClaudeHUD: colore esplicito in modalita' chiara
		"armedBgColor_override"     	"LtButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
		"depressedBgColor_override" 	"LtButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
	}
	"JoinLateCheckButton"
	{
		"ControlName"          	"CheckButton"
		"fieldName"            	"JoinLateCheckButton"
		"xpos"                 	"rs1"
		"ypos"                 	"rs1-9"
		"zpos"                 	"50"
		"wide"                 	"140"
		"tall"                 	"20"
		"font"                 	"HudFontSmallest"
		"labelText"            	""
		"proportionaltoparent" 	"1"
		"fgcolor_override"     	"LtText"	// ClaudeHUD: colore esplicito in modalita' chiara
	}
	"JoinLateLabel"
	{
		"ControlName"          	"Label"
		"fieldName"            	"JoinLateLabel"
		"xpos"                 	"rs1"
		"ypos"                 	"rs1-9"
		"zpos"                 	"50"
		"wide"                 	"115"
		"tall"                 	"20"
		"font"                 	"HudFontSmallest"
		"labelText"            	"#TF_Matchmaking_JoinInProgress"
		"proportionaltoparent" 	"1"
		"fgcolor_override"     	"LtText"	// ClaudeHUD: colore esplicito in modalita' chiara
	}
}
