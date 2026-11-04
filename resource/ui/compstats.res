// ClaudeHUD: migrato ai token (layout originale) - generato da tools/migrate.py
// modalita': light (DESIGN.md par. 9)
"Resource/UI/CompStats.res"
{
	"ScrollableContainer"
	{
		"ControlName"          	"EditablePanel"
		"fieldName"            	"ScrollableContainer"
		"xpos"                 	"0"
		"ypos"                 	"0"
		"zpos"                 	"100"
		"wide"                 	"260"
		"tall"                 	"330"
		"visible"              	"1"
		"proportionaltoparent" 	"1"
		"RankImage"
		{
			"ControlName"          	"CTFLocalPlayerBadgePanel"
			"fieldName"            	"RankImage"
			"xpos"                 	"-8"
			"ypos"                 	"-15"
			"zpos"                 	"110"
			"wide"                 	"o1"
			"tall"                 	"70"
			"visible"              	"1"
			"enabled"              	"1"
			"proportionaltoparent" 	"1"
			"mouseinputenabled"    	"0"
			"matchgroup"           	"MatchGroup_Ladder_6v6"
		}
		"RankPanel"
		{
			"ControlName"          	"CPvPRankPanel"
			"fieldName"            	"RankPanel"
			"xpos"                 	"-75"
			"ypos"                 	"-35"
			"zpos"                 	"100"
			"wide"                 	"320"
			"tall"                 	"100"
			"visible"              	"1"
			"proportionaltoparent" 	"1"
			"mouseinputenabled"    	"0"
			"matchgroup"           	"MatchGroup_Ladder_6v6"
			"show_model"           	"0"
			"show_name"            	"0"
			"BGBorder"
			{
				"visible" 	"0"
			}
		}
		"ShowLeaderboardsButton"
		{
			"ControlName"               	"CExButton"
			"fieldName"                 	"ShowLeaderboardsButton"
			"xpos"                      	"rs1-10"
			"ypos"                      	"40"
			"zpos"                      	"0"
			"wide"                      	"p0.45"
			"tall"                      	"15"
			"visible"                   	"1"
			"proportionaltoparent"      	"1"
			"actionsignallevel"         	"2"
			"command"                   	"show_leaderboards"
			"labeltext"                 	"#TF_Competitive_ViewLeaderboards"
			"font"                      	"HudFontSmallestBold"
			"fgcolor_override"          	"LtText"
			"textAlignment"             	"center"
			"sound_depressed"           	"UI/buttonclick.wav"
			"sound_released"            	"UI/buttonclickrelease.wav"
			"defaultBgColor_override"   	"LtCardAlt"	// ClaudeHUD: colore esplicito in modalita' chiara
			"armedBgColor_override"     	"LtButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
			"depressedBgColor_override" 	"LtButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
		}
		"ShowMatchHistoryButton"
		{
			"ControlName"               	"Button"
			"fieldName"                 	"ShowMatchHistoryButton"
			"xpos"                      	"10"
			"ypos"                      	"40"
			"zpos"                      	"0"
			"wide"                      	"p0.45"
			"tall"                      	"15"
			"visible"                   	"1"
			"proportionaltoparent"      	"1"
			"actionsignallevel"         	"2"
			"command"                   	"show_match_history"
			"labeltext"                 	"#TF_Competitive_ViewMatches"
			"font"                      	"HudFontSmallestBold"
			"fgcolor_override"          	"LtText"
			"textAlignment"             	"center"
			"sound_depressed"           	"UI/buttonclick.wav"
			"sound_released"            	"UI/buttonclickrelease.wav"
			"defaultBgColor_override"   	"LtCardAlt"	// ClaudeHUD: colore esplicito in modalita' chiara
			"armedBgColor_override"     	"LtButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
			"depressedBgColor_override" 	"LtButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
		}
		"PlaylistBGPanel"
		{
			"ControlName"          	"EditablePanel"
			"fieldName"            	"PlaylistBGPanel"
			"xpos"                 	"cs-0.5"
			"ypos"                 	"35"
			"zpos"                 	"-1"
			"wide"                 	"p0.98"
			"tall"                 	"p1-200"
			"visible"              	"1"
			"PaintBackgroundType"  	"2"
			"proportionaltoparent" 	"1"
			"pinCorner"            	"2"
			"autoResize"           	"1"
			"PlayListDropShadow"
			{
				"ControlName"          	"EditablePanel"
				"fieldName"            	"PlayListDropShadow"
				"xpos"                 	"cs-0.5"
				"ypos"                 	"25"
				"zpos"                 	"100"
				"wide"                 	"p0.95"
				"tall"                 	"p0.89"
				"visible"              	"1"
				"PaintBackgroundType"  	"2"
				"border"               	"InnerShadowBorder"
				"proportionaltoparent" 	"1"
				"mouseinputenabled"    	"0"
				"bgcolor_override"     	"Clear"	// ClaudeHUD: riempimento al posto del bordo texture
			}
			"MatchHistoryCategories"
			{
				"ControlName"          	"EditablePanel"
				"fieldName"            	"MatchHistoryCategories"
				"xpos"                 	"cs-0.5"
				"ypos"                 	"25"
				"zpos"                 	"10"
				"wide"                 	"p0.95"
				"tall"                 	"20"
				"visible"              	"1"
				"proportionaltoparent" 	"1"
				"BGPanel"
				{
					"ControlName"          	"EditablePanel"
					"fieldName"            	"BGPanel"
					"xpos"                 	"cs-0.5"
					"ypos"                 	"rs1"
					"zpos"                 	"-100"
					"wide"                 	"p1.2"
					"tall"                 	"p1.3"
					"visible"              	"1"
					"proportionaltoparent" 	"1"
					"border"               	"MainMenuBGBorder"
					"bgcolor_override"     	"LtCard"	// ClaudeHUD: riempimento al posto del bordo texture
				}
				"SortArrow"
				{
					"ControlName"              	"Label"
					"fieldName"                	"SortArrow"
					"xpos"                     	"0"
					"ypos"                     	"0"
					"wide"                     	"20"
					"tall"                     	"f0"
					"proportionaltoparent"     	"1"
					"visible"                  	"1"
					"paintbackground"          	"0"
					"mouseinputenabled"        	"0"
					"labeltext"                	"6"
					"font"                     	"MarlettSmall"
					"textAlignment"            	"west"
					"defaultFgColor_override"  	"LtTextMuted"
					"armedFgColor_override"    	"LtTextMuted"
					"selectedFgColor_override" 	"LtTextMuted"
					"fgcolor_override"         	"LtText"	// ClaudeHUD: colore esplicito in modalita' chiara
				}
				"ResultButton"
				{
					"ControlName"              	"CExButton"
					"fieldName"                	"ResultButton"
					"xpos"                     	"0"
					"ypos"                     	"0"
					"wide"                     	"p0.18"
					"tall"                     	"18"
					"proportionaltoparent"     	"1"
					"visible"                  	"1"
					"paintbackground"          	"0"
					"border_default"           	"SortCategoryBorder"
					"labeltext"                	"#TF_Competitive_Result"
					"font"                     	"HudFontSmallest"
					"fgcolor_override"         	"LtAccentText"
					"textAlignment"            	"west"
					"textinsetx"               	"15"
					"defaultFgColor_override"  	"LtTextMuted"
					"armedFgColor_override"    	"LtAccentText"
					"selectedFgColor_override" 	"LtText"
					"image_selectedcolor"      	"255 255 255 255"	// token: Untinted
					"image_armedcolor"         	"Clear"
					"image_drawcolor"          	"Clear"
					"command"                  	"sort0"
					"actionsignallevel"        	"4"
					"sound_depressed"          	"UI/buttonclick.wav"
					"sound_released"           	"UI/buttonclickrelease.wav"
				}
				"DateButton"
				{
					"ControlName"              	"CExButton"
					"fieldName"                	"DateButton"
					"xpos"                     	"p0.18"
					"ypos"                     	"0"
					"wide"                     	"p0.4"
					"tall"                     	"18"
					"proportionaltoparent"     	"1"
					"visible"                  	"1"
					"paintbackground"          	"0"
					"border_default"           	"SortCategoryBorder"
					"labeltext"                	"#TF_Competitive_Date"
					"font"                     	"HudFontSmallest"
					"fgcolor_override"         	"LtText"
					"textAlignment"            	"west"
					"textinsetx"               	"15"
					"defaultFgColor_override"  	"LtTextMuted"
					"armedFgColor_override"    	"LtAccentText"
					"selectedFgColor_override" 	"LtText"
					"image_selectedcolor"      	"255 255 255 255"	// token: Untinted
					"image_armedcolor"         	"Clear"
					"image_drawcolor"          	"Clear"
					"command"                  	"sort1"
					"actionsignallevel"        	"4"
					"sound_depressed"          	"UI/buttonclick.wav"
					"sound_released"           	"UI/buttonclickrelease.wav"
				}
				"MapButton"
				{
					"ControlName"              	"CExButton"
					"fieldName"                	"MapButton"
					"xpos"                     	"p0.58"
					"ypos"                     	"0"
					"wide"                     	"p0.29"
					"tall"                     	"18"
					"proportionaltoparent"     	"1"
					"visible"                  	"1"
					"paintbackground"          	"0"
					"border_default"           	"SortCategoryBorder"
					"labeltext"                	"#TF_Competitive_Map"
					"font"                     	"HudFontSmallest"
					"fgcolor_override"         	"LtText"
					"textAlignment"            	"west"
					"textinsetx"               	"15"
					"defaultFgColor_override"  	"LtTextMuted"
					"armedFgColor_override"    	"LtAccentText"
					"selectedFgColor_override" 	"LtText"
					"image_selectedcolor"      	"255 255 255 255"	// token: Untinted
					"image_armedcolor"         	"Clear"
					"image_drawcolor"          	"Clear"
					"command"                  	"sort2"
					"actionsignallevel"        	"4"
					"sound_depressed"          	"UI/buttonclick.wav"
					"sound_released"           	"UI/buttonclickrelease.wav"
				}
				"KDRButton"
				{
					"ControlName"              	"CExButton"
					"fieldName"                	"KDRButton"
					"xpos"                     	"p0.87"
					"ypos"                     	"0"
					"wide"                     	"p0.12"
					"tall"                     	"18"
					"proportionaltoparent"     	"1"
					"visible"                  	"1"
					"paintbackground"          	"0"
					"labeltext"                	"#TF_Competitive_KDR"
					"font"                     	"HudFontSmallest"
					"fgcolor_override"         	"LtText"
					"textAlignment"            	"west"
					"defaultFgColor_override"  	"LtTextMuted"
					"armedFgColor_override"    	"LtAccentText"
					"selectedFgColor_override" 	"LtText"
					"image_selectedcolor"      	"255 255 255 255"	// token: Untinted
					"image_armedcolor"         	"Clear"
					"image_drawcolor"          	"Clear"
					"command"                  	"sort3"
					"actionsignallevel"        	"4"
					"sound_depressed"          	"UI/buttonclick.wav"
					"sound_released"           	"UI/buttonclickrelease.wav"
				}
			}
			"MatchHistoryContainer"
			{
				"ControlName"          	"CScrollableList"
				"fieldName"            	"MatchHistoryContainer"
				"xpos"                 	"cs-0.5"
				"ypos"                 	"40"
				"wide"                 	"p0.95"
				"tall"                 	"p0.78"
				"visible"              	"1"
				"proportionaltoparent" 	"1"
				"restrict_width"       	"0"
				"ScrollBar"
				{
					"ControlName"          	"ScrollBar"
					"FieldName"            	"ScrollBar"
					"xpos"                 	"rs1-1"
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
			}
			"Leaderboard"
			{
				"ControlName"          	"CLadderLobbyLeaderboard"
				"fieldName"            	"Leaderboard"
				"xpos"                 	"cs-0.5"
				"ypos"                 	"7"
				"wide"                 	"p0.95"
				"tall"                 	"p0.89"
				"tall"                 	"f20"
				"visible"              	"0"
				"enabled"              	"1"
				"mouseinputenabled"    	"1"
				"scaleImage"           	"1"
				"entry_step"           	"23"
				"proportionaltoparent" 	"1"
			}
		}
	}
}
