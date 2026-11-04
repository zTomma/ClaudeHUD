// ClaudeHUD: migrato ai token (layout originale) - generato da tools/migrate.py
// modalita': light (DESIGN.md par. 9)
#base "LobbyContainerFrame.res"
"Resource/UI/LobbyContainerFrame_MvM.res"
{
	"OptionsButton"
	{
		"ControlName"               	"CExImageButton"
		"fieldName"                 	"OptionsButton"
		"visible"                   	"0"
		"defaultFgColor_override"   	"LtText"	// ClaudeHUD: colore esplicito in modalita' chiara
		"armedFgColor_override"     	"LtOnButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
		"depressedFgColor_override" 	"LtOnButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
		"defaultBgColor_override"   	"LtCardAlt"	// ClaudeHUD: colore esplicito in modalita' chiara
		"armedBgColor_override"     	"LtButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
		"depressedBgColor_override" 	"LtButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
	}
	"LearnMoreButton"
	{
		"ControlName"               	"CExImageButton"
		"fieldName"                 	"LearnMoreButton"
		"xpos"                      	"c106"
		"ypos"                      	"385"
		"zpos"                      	"2"
		"wide"                      	"195"
		"tall"                      	"25"
		"autoResize"                	"0"
		"visible"                   	"1"
		"enabled"                   	"1"
		"tabPosition"               	"0"
		"labelText"                 	"#TF_MvM_LearnMore"
		"font"                      	"HudFontSmallBold"
		"textAlignment"             	"center"
		"dulltext"                  	"0"
		"brighttext"                	"0"
		"Command"                   	"learn_more"
		"NavUp"                     	"PracticeButton"
		"NavLeft"                   	"BackButton"
		"NavRight"                  	"NextButton"
		"sound_depressed"           	"UI/buttonclick.wav"
		"sound_released"            	"UI/buttonclickrelease.wav"
		"defaultFgColor_override"   	"LtText"	// ClaudeHUD: colore esplicito in modalita' chiara
		"armedFgColor_override"     	"LtOnButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
		"depressedFgColor_override" 	"LtOnButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
		"defaultBgColor_override"   	"LtCardAlt"	// ClaudeHUD: colore esplicito in modalita' chiara
		"armedBgColor_override"     	"LtButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
		"depressedBgColor_override" 	"LtButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
	}
	"PlayNowButton"
	{
		"ControlName"               	"CExButton"
		"fieldName"                 	"PlayNowButton"
		"xpos"                      	"c-295"
		"ypos"                      	"303"
		"zpos"                      	"20"
		"wide"                      	"180"
		"tall"                      	"40"
		"autoResize"                	"0"
		"pinCorner"                 	"0"
		"visible"                   	"1"
		"enabled"                   	"1"
		"tabPosition"               	"0"
		"labelText"                 	"#TF_MvM_MannUp"
		"font"                      	"TypeHeading"
		"textAlignment"             	"center"
		"textinsetx"                	"50"
		"dulltext"                  	"0"
		"brighttext"                	"0"
		"Command"                   	"mannup"
		"NavUp"                     	"Sheet"
		"NavDown"                   	"BackButton"
		"NavLeft"                   	"Sheet"
		"NavRight"                  	"PracticeButton"
		"sound_depressed"           	"UI/buttonclick.wav"
		"sound_released"            	"UI/buttonclickrelease.wav"
		"border_default"            	"MainMenuButtonDefault"
		"border_armed"              	"MainMenuButtonArmed"
		"paintbackground"           	"0"
		"defaultFgColor_override"   	"LtText"
		"armedFgColor_override"     	"LtText"
		"depressedFgColor_override" 	"LtText"
	}
	"PracticeButton"
	{
		"ControlName"               	"CExButton"
		"fieldName"                 	"PracticeButton"
		"xpos"                      	"c-95"
		"ypos"                      	"303"
		"zpos"                      	"20"
		"wide"                      	"180"
		"tall"                      	"40"
		"autoResize"                	"0"
		"pinCorner"                 	"0"
		"visible"                   	"1"
		"enabled"                   	"1"
		"tabPosition"               	"0"
		"labelText"                 	"#TF_MvM_BootCamp"
		"font"                      	"TypeHeading"
		"textAlignment"             	"center"
		"textinsetx"                	"50"
		"dulltext"                  	"0"
		"brighttext"                	"0"
		"Command"                   	"practice"
		"NavUp"                     	"Sheet"
		"NavDown"                   	"LearnMoreButton"
		"NavLeft"                   	"PlayNowButton"
		"NavRight"                  	"StartPartyButton"
		"sound_depressed"           	"UI/buttonclick.wav"
		"sound_released"            	"UI/buttonclickrelease.wav"
		"border_default"            	"MainMenuButtonDefault"
		"border_armed"              	"MainMenuButtonArmed"
		"paintbackground"           	"0"
		"defaultFgColor_override"   	"LtText"
		"armedFgColor_override"     	"LtText"
		"depressedFgColor_override" 	"LtText"
	}
	"PlayWithFriendsExplanation"
	{
		"ControlName"         	"EditablePanel"
		"fieldName"           	"PlayWithFriendsExplanation"
		"xpos"                	"c+100"
		"ypos"                	"62"
		"zpos"                	"8"
		"wide"                	"200"
		"tall"                	"285"
		"PaintBackgroundType" 	"0"
		"paintbackground"     	"1"
		"bgcolor_override"    	"LtCardAltA80"
		"border"              	"QuickplayBorder"
		"PlayWithFriendsExplanationTitle"
		{
			"ControlName"      	"CExLabel"
			"fieldName"        	"PlayWithFriendsExplanationTitle"
			"font"             	"HudFontSmallBold"
			"labelText"        	"#TF_Matchmaking_PlayWithFriends"
			"textAlignment"    	"center"
			"xpos"             	"0"
			"ypos"             	"0"
			"zpos"             	"10"
			"wide"             	"200"
			"tall"             	"32"
			"fgcolor_override" 	"LtText"	// ClaudeHUD: colore esplicito in modalita' chiara
		}
		"FriendsImage"
		{
			"ControlName" 	"ImagePanel"
			"fieldName"   	"FriendsImage"
			"xpos"        	"10"
			"ypos"        	"32"
			"zpos"        	"0"
			"wide"        	"180"
			"tall"        	"90"
			"visible"     	"1"
			"enabled"     	"1"
			"image"       	"pve/mvm_friends_image"
			"scaleImage"  	"1"
		}
		"PlayWithFriendsExplanationLabel"
		{
			"ControlName"      	"CExLabel"
			"fieldName"        	"PlayWithFriendsExplanationLabel"
			"font"             	"HudFontSmall"
			"labelText"        	"#TF_MvM_PlayWithFriendsExplanation"
			"textAlignment"    	"north-west"
			"xpos"             	"10"
			"ypos"             	"130"
			"zpos"             	"10"
			"wide"             	"180"
			"tall"             	"150"
			"wrap"             	"1"
			"fgcolor_override" 	"LtText"	// ClaudeHUD: colore esplicito in modalita' chiara
		}
	}
}
