// ClaudeHUD: migrato ai token (layout originale) - generato da tools/migrate.py
// modalita': light (DESIGN.md par. 9)
#base "MatchMakingDashboardSidePanel.res"
"Resource/UI/MatchMakingDashboardEventMatch.res"
{
	"EventMatch"
	{
		"fieldName"            	"EventMatch"
		"xpos"                 	"r0"
		"ypos"                 	"10"
		"zpos"                 	"1002"
		"wide"                 	"270"
		"tall"                 	"f70"
		"visible"              	"1"
		"proportionaltoparent" 	"1"
	}
	"Title"
	{
		"ControlName"          	"Label"
		"fieldName"            	"Title"
		"xpos"                 	"8"
		"ypos"                 	"20"
		"zpos"                 	"99"
		"wide"                 	"f0"
		"tall"                 	"20"
		"proportionaltoparent" 	"1"
		"labeltext"            	"#TF_Matchmaking_HeaderSpecialEvent"
		"textAlignment"        	"west"
		"font"                 	"TypeTitle"
		"fgcolor_override"     	"LtTextMuted"
		"mouseinputenabled"    	"0"
	}
	"ModeTitle"
	{
		"ControlName"          	"Label"
		"fieldName"            	"ModeTitle"
		"xpos"                 	"8"
		"ypos"                 	"43"
		"zpos"                 	"99"
		"wide"                 	"f0"
		"tall"                 	"20"
		"proportionaltoparent" 	"1"
		"labeltext"            	"%title%"
		"textAlignment"        	"west"
		"font"                 	"TypeHeading"
		"fgcolor_override"     	"LtAccentText"
		"mouseinputenabled"    	"0"
	}
	"RankImage"
	{
		"ControlName"          	"CTFLocalPlayerBadgePanel"
		"fieldName"            	"RankImage"
		"xpos"                 	"-10"
		"ypos"                 	"45"
		"zpos"                 	"110"
		"wide"                 	"o1"
		"tall"                 	"70"
		"visible"              	"1"
		"enabled"              	"1"
		"proportionaltoparent" 	"1"
		"mouseinputenabled"    	"0"
		"matchgroup"           	"MatchGroup_Casual_12v12"
	}
	"RankPanel"
	{
		"ControlName"          	"CPvPRankPanel"
		"fieldName"            	"RankPanel"
		"xpos"                 	"-85"
		"ypos"                 	"25"
		"zpos"                 	"100"
		"wide"                 	"330"
		"tall"                 	"92"
		"visible"              	"1"
		"proportionaltoparent" 	"1"
		"mouseinputenabled"    	"0"
		"matchgroup"           	"MatchGroup_Casual_12v12"
		"show_model"           	"0"
		"show_name"            	"0"
	}
	"ModeImageGroup"
	{
		"ControlName" 	"EditablePanel"
		"fieldName"   	"ModeImageGroup"
		"xpos"        	"6"
		"ypos"        	"100"
		"zpos"        	"1"
		"wide"        	"250"
		"tall"        	"o0.25"
		"visible"     	"1"
		"enabled"     	"1"
		"DropShadow"
		{
			"ControlName"          	"EditablePanel"
			"fieldName"            	"DropShadow"
			"xpos"                 	"0"
			"ypos"                 	"0"
			"zpos"                 	"101"
			"wide"                 	"f0"
			"tall"                 	"f0"
			"visible"              	"1"
			"PaintBackgroundType"  	"2"
			"border"               	"InnerShadowBorder"
			"proportionaltoparent" 	"1"
			"mouseinputenabled"    	"0"
			"bgcolor_override"     	"Clear"	// ClaudeHUD: riempimento al posto del bordo texture
		}
		"ModeImage"
		{
			"ControlName"          	"ImagePanel"
			"fieldName"            	"ModeImage"
			"xpos"                 	"0"
			"ypos"                 	"0"
			"zpos"                 	"0"
			"wide"                 	"f0"
			"tall"                 	"f0"
			"visible"              	"1"
			"enabled"              	"1"
			"mouseinputenabled"    	"0"
			"image"                	"mvm/mannup"
			"scaleImage"           	"1"
			"proportionaltoparent" 	"1"
		}
	}
	"DescScroller"
	{
		"ControlName"          	"CExScrollingEditablePanel"
		"fieldName"            	"DescScroller"
		"xpos"                 	"cs-0.5"
		"ypos"                 	"165"
		"zpos"                 	"2"
		"wide"                 	"f20"
		"tall"                 	"215"
		"proportionaltoparent" 	"1"
		"ScrollBar"
		{
			"ControlName"          	"ScrollBar"
			"FieldName"            	"ScrollBar"
			"xpos"                 	"rs1-5"
			"ypos"                 	"0"
			"tall"                 	"f0"
			"wide"                 	"5"	// This gets slammed from client schme.  GG.
			"zpos"                 	"1000"
			"nobuttons"            	"1"
			"proportionaltoparent" 	"1"
			"Slider"
			{
				"fgcolor_override" 	"LtTextMuted"
			}
			"UpButton"
			{
				"ControlName"               	"Button"
				"FieldName"                 	"UpButton"
				"visible"                   	"0"
				"defaultFgColor_override"   	"LtText"	// ClaudeHUD: colore esplicito in modalita' chiara
				"armedFgColor_override"     	"LtOnButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
				"depressedFgColor_override" 	"LtOnButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
				"defaultBgColor_override"   	"LtCardAlt"	// ClaudeHUD: colore esplicito in modalita' chiara
				"armedBgColor_override"     	"LtButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
				"depressedBgColor_override" 	"LtButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
			}
			"DownButton"
			{
				"ControlName"               	"Button"
				"FieldName"                 	"DownButton"
				"visible"                   	"0"
				"defaultFgColor_override"   	"LtText"	// ClaudeHUD: colore esplicito in modalita' chiara
				"armedFgColor_override"     	"LtOnButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
				"depressedFgColor_override" 	"LtOnButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
				"defaultBgColor_override"   	"LtCardAlt"	// ClaudeHUD: colore esplicito in modalita' chiara
				"armedBgColor_override"     	"LtButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
				"depressedBgColor_override" 	"LtButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
			}
		}
		"ModeDesc"
		{
			"ControlName"          	"Label"
			"fieldName"            	"ModeDesc"
			"font"                 	"HudFontSmall"
			"fgcolor_override"     	"LtText"
			"labelText"            	"%desc%"
			"textAlignment"        	"north-west"
			"xpos"                 	"0"
			"ypos"                 	"0"
			"zpos"                 	"2"
			"wide"                 	"f0"
			"tall"                 	"300"
			"wrap"                 	"1"
			"proportionaltoparent" 	"1"
			"mouseinputenabled"    	"0"
			"auto_tall_tocontents" 	"1"
		}
	}
	"ToolTipButtonHack"
	{
		"ControlName"                   	"EditablePanel"
		"fieldName"                     	"ToolTipButtonHack"
		"xpos"                          	"cs-0.5"
		"ypos"                          	"rs1-8"
		"zpos"                          	"101"
		"wide"                          	"f20"
		"tall"                          	"20"
		"visible"                       	"0"
		"enabled"                       	"1"
		"mouseinputenabled"             	"1"
		"eatmouseinput"                 	"0"
		"showtooltipswhenmousedisabled" 	"1"
		"proportionaltoparent"          	"1"
	}
	"QueueButton"
	{
		"ControlName"               	"CExButton"
		"fieldName"                 	"QueueButton"
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
		"Command"                   	"find_game"
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
}
