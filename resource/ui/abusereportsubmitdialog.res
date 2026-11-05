// ClaudeHUD: migrato ai token (layout originale) - generato da tools/migrate.py
// modalita': light (DESIGN.md par. 9)
"Resource/UI/AbuseReportSubmitDialog.res"
{
	"AbuseReportSubmitDialog"
	{
		"fieldName"        	"AbuseReportSubmitDialog"
		"visible"          	"1"
		"enabled"          	"1"
		"xpos"             	"c-280"
		"ypos"             	"c-240"
		"wide"             	"560"
		"tall"             	"405"
		"border"           	"GrayDialogBorder"
		"bgcolor_override" 	"LtCard"	// ClaudeHUD: riempimento al posto del bordo texture
	}
	"TitleLabel"
	{
		"ControlName"      	"CExLabel"
		"fieldName"        	"TitleLabel"
		"font"             	"TypeHeading"
		"labelText"        	"#AbuseReport_DialogTitle"
		"textAlignment"    	"north-west"
		"xpos"             	"10"
		"ypos"             	"10"
		"zpos"             	"0"
		"wide"             	"540"
		"tall"             	"20"
		"centerwrap"       	"1"
		"fgcolor_override" 	"LtText"	// ClaudeHUD: colore esplicito in modalita' chiara
	}
	"GameServerRadio"
	{
		"ControlName"      	"RadioButton"
		"fieldName"        	"GameServerRadio"
		"labelText"        	"#AbuseReport_GameServer"
		"xpos"             	"10"
		"ypos"             	"40"
		"zpos"             	"-1"
		"wide"             	"170"
		"tall"             	"20"
		"editable"         	"0"
		"font"             	"HudFontSmall"
		"fgcolor_override" 	"LtText"	// ClaudeHUD: colore esplicito in modalita' chiara
	}
	"PlayerRadio"
	{
		"ControlName"      	"RadioButton"
		"fieldName"        	"PlayerRadio"
		"labelText"        	"#AbuseReport_Player"
		"xpos"             	"10"
		"ypos"             	"60"
		"zpos"             	"-1"
		"wide"             	"170"
		"tall"             	"20"
		"editable"         	"0"
		"font"             	"HudFontSmall"
		"fgcolor_override" 	"LtText"	// ClaudeHUD: colore esplicito in modalita' chiara
	}
	"PlayerLabel"
	{
		"ControlName"      	"CExLabel"
		"fieldName"        	"PlayerLabel"
		"labelText"        	"#AbuseReport_PlayerLabel"
		"xpos"             	"10"
		"ypos"             	"90"
		"zpos"             	"-1"
		"wide"             	"170"
		"tall"             	"15"
		"editable"         	"0"
		"font"             	"HudFontSmall"
		"fgcolor_override" 	"LtText"	// ClaudeHUD: colore esplicito in modalita' chiara
	}
	"PlayerComboBox"
	{
		"ControlName"                       	"ComboBox"
		"fieldName"                         	"PlayerComboBox"
		"xpos"                              	"10"
		"ypos"                              	"105"
		"zpos"                              	"-1"
		"wide"                              	"170"
		"tall"                              	"15"
		"editable"                          	"0"
		"font"                              	"HudFontSmall"
		"bgcolor_override"                  	"LtCardAlt"
		"disabledBgColor_override"          	"LtCardAlt"
		"selectionColor_override"           	"LtCardAlt"
		"selectionTextColor_override"       	"LtText"
		"defaultSelectionBG2Color_override" 	"Clear"
	}
	"AbuseContentLabel"
	{
		"ControlName"      	"CExLabel"
		"fieldName"        	"AbuseContentLabel"
		"labelText"        	"#AbuseReport_ContentLabel"
		"xpos"             	"10"
		"ypos"             	"130"
		"zpos"             	"-1"
		"wide"             	"170"
		"tall"             	"15"
		"editable"         	"0"
		"font"             	"HudFontSmall"
		"fgcolor_override" 	"LtText"	// ClaudeHUD: colore esplicito in modalita' chiara
	}
	"AbuseContentComboBox"
	{
		"ControlName"                       	"ComboBox"
		"fieldName"                         	"AbuseContentComboBox"
		"xpos"                              	"10"
		"ypos"                              	"145"
		"zpos"                              	"-1"
		"wide"                              	"170"
		"tall"                              	"15"
		"editable"                          	"0"
		"font"                              	"HudFontSmall"
		"bgcolor_override"                  	"LtCardAlt"
		"disabledBgColor_override"          	"LtCardAlt"
		"selectionColor_override"           	"LtCardAlt"
		"selectionTextColor_override"       	"LtText"
		"defaultSelectionBG2Color_override" 	"Clear"
	}
	"AbuseTypeLabel"
	{
		"ControlName"      	"CExLabel"
		"fieldName"        	"AbuseTypeLabel"
		"labelText"        	"#AbuseReport_CategoryLabel"
		"xpos"             	"10"
		"ypos"             	"170"
		"zpos"             	"-1"
		"wide"             	"170"
		"tall"             	"15"
		"editable"         	"0"
		"font"             	"HudFontSmall"
		"fgcolor_override" 	"LtText"	// ClaudeHUD: colore esplicito in modalita' chiara
	}
	"AbuseTypeComboBox"
	{
		"ControlName"                       	"ComboBox"
		"fieldName"                         	"AbuseTypeComboBox"
		"xpos"                              	"10"
		"ypos"                              	"185"
		"zpos"                              	"-1"
		"wide"                              	"170"
		"tall"                              	"15"
		"editable"                          	"0"
		"font"                              	"HudFontSmall"
		"bgcolor_override"                  	"LtCardAlt"
		"disabledBgColor_override"          	"LtCardAlt"
		"selectionColor_override"           	"LtCardAlt"
		"selectionTextColor_override"       	"LtText"
		"defaultSelectionBG2Color_override" 	"Clear"
	}
	"ScreenShotBitmap"
	{
		"ControlName" 	"CBitmapPanel"
		"fieldName"   	"ScreenShotBitmap"
		"xpos"        	"190"
		"ypos"        	"40"
		"wide"        	"360"
		"tall"        	"200"
		"visible"     	"1"
		"enabled"     	"1"
	}
	"ScreenShotAttachCheckButton"
	{
		"ControlName"      	"CheckButton"
		"fieldName"        	"ScreenShotAttachCheckButton"
		"xpos"             	"190"
		"ypos"             	"245"
		"zpos"             	"1"
		"wide"             	"360"
		"tall"             	"18"
		"labelText"        	"#AbuseReport_UploadScreenshot"
		"font"             	"HudFontSmall"
		"textAlignment"    	"west"
		"sound_depressed"  	"UI/buttonclick.wav"
		"sound_released"   	"UI/buttonclickrelease.wav"
		"fgcolor_override" 	"LtText"	// ClaudeHUD: colore esplicito in modalita' chiara
	}
	"AvatarImage"
	{
		"ControlName" 	"CAvatarImagePanel"
		"fieldName"   	"AvatarImage"
		"xpos"        	"260"
		"ypos"        	"40"
		"wide"        	"200"
		"tall"        	"200"
		"visible"     	"1"
		"enabled"     	"1"
		"scaleImage"  	"1"
	}
	"NoAvatarLabel"
	{
		"ControlName"      	"CExLabel"
		"fieldName"        	"NoAvatarLabel"
		"xpos"             	"260"
		"ypos"             	"40"
		"wide"             	"220"
		"tall"             	"220"
		"visible"          	"1"
		"enabled"          	"1"
		"labelText"        	"#AbuseReport_NoAvatar"
		"font"             	"HudFontSmall"
		"centerwrap"       	"1"
		"fgcolor_override" 	"LtText"	// ClaudeHUD: colore esplicito in modalita' chiara
	}
	"CustomTextureImage"
	{
		"ControlName" 	"CCustomTextureImagePanel"
		"fieldName"   	"CustomTextureImage"
		"xpos"        	"260"
		"ypos"        	"40"
		"wide"        	"220"
		"tall"        	"220"
		"visible"     	"1"
		"enabled"     	"1"
	}
	"CustomTexturePrevButton"
	{
		"ControlName"               	"CExButton"
		"fieldName"                 	"CustomTexturePrevButton"
		"xpos"                      	"230"
		"ypos"                      	"128"
		"zpos"                      	"20"
		"wide"                      	"18"
		"tall"                      	"43"
		"autoResize"                	"0"
		"pinCorner"                 	"0"
		"visible"                   	"1"
		"enabled"                   	"1"
		"tabPosition"               	"0"
		"labelText"                 	"#TF_LessThan"
		"font"                      	"HudFontSmallBold"
		"textAlignment"             	"center"
		"textinsetx"                	"0"
		"dulltext"                  	"0"
		"brighttext"                	"0"
		"Command"                   	"prevcustomtexture"
		"sound_depressed"           	"UI/buttonclick.wav"
		"sound_released"            	"UI/buttonclickrelease.wav"
		"defaultFgColor_override"   	"LtText"	// ClaudeHUD: colore esplicito in modalita' chiara
		"armedFgColor_override"     	"LtOnButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
		"depressedFgColor_override" 	"LtOnButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
		"defaultBgColor_override"   	"LtCardAlt"	// ClaudeHUD: colore esplicito in modalita' chiara
		"armedBgColor_override"     	"LtButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
		"depressedBgColor_override" 	"LtButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
	}
	"CustomTextureNextButton"
	{
		"ControlName"               	"CExButton"
		"fieldName"                 	"CustomTextureNextButton"
		"xpos"                      	"492"
		"ypos"                      	"128"
		"zpos"                      	"20"
		"wide"                      	"18"
		"tall"                      	"43"
		"autoResize"                	"0"
		"pinCorner"                 	"0"
		"visible"                   	"1"
		"enabled"                   	"1"
		"tabPosition"               	"0"
		"labelText"                 	"#TF_GreaterThan"
		"font"                      	"HudFontSmallBold"
		"textAlignment"             	"center"
		"textinsetx"                	"0"
		"dulltext"                  	"0"
		"brighttext"                	"0"
		"Command"                   	"nextcustomtexture"
		"sound_depressed"           	"UI/buttonclick.wav"
		"sound_released"            	"UI/buttonclickrelease.wav"
		"defaultFgColor_override"   	"LtText"	// ClaudeHUD: colore esplicito in modalita' chiara
		"armedFgColor_override"     	"LtOnButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
		"depressedFgColor_override" 	"LtOnButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
		"defaultBgColor_override"   	"LtCardAlt"	// ClaudeHUD: colore esplicito in modalita' chiara
		"armedBgColor_override"     	"LtButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
		"depressedBgColor_override" 	"LtButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
	}
	"NoCustomTexturesLabel"
	{
		"ControlName"      	"CExLabel"
		"fieldName"        	"NoCustomTexturesLabel"
		"xpos"             	"260"
		"ypos"             	"40"
		"wide"             	"220"
		"tall"             	"220"
		"visible"          	"1"
		"enabled"          	"1"
		"labelText"        	"#AbuseReport_NoCustomTextures"
		"font"             	"HudFontSmall"
		"centerwrap"       	"1"
		"fgcolor_override" 	"LtText"	// ClaudeHUD: colore esplicito in modalita' chiara
	}
	"DescriptionLabel"
	{
		"ControlName"      	"CExLabel"
		"fieldName"        	"DescriptionLabel"
		"labelText"        	"#AbuseReport_DescriptionLabel"
		"xpos"             	"10"
		"ypos"             	"250"
		"zpos"             	"-1"
		"wide"             	"140"
		"tall"             	"15"
		"editable"         	"0"
		"font"             	"HudFontSmall"
		"fgcolor_override" 	"LtText"	// ClaudeHUD: colore esplicito in modalita' chiara
	}
	"DescriptionTextEntry"
	{
		"ControlName"      	"TextEntry"
		"fieldName"        	"DescriptionTextEntry"
		"xpos"             	"10"
		"ypos"             	"270"
		"zpos"             	"-1"
		"wide"             	"540"
		"tall"             	"90"
		"font"             	"HudFontSmall"
		"bgcolor_override" 	"LtCardAlt"
		"fgcolor_override" 	"LtText"
		"maxchars"         	"512"
	}
	"DiscardButton"
	{
		"ControlName"               	"CExButton"
		"fieldName"                 	"DiscardButton"
		"xpos"                      	"10"
		"ypos"                      	"370"
		"zpos"                      	"1"
		"wide"                      	"130"
		"tall"                      	"25"
		"labelText"                 	"#AbuseReport_Discard"
		"font"                      	"HudFontSmallBold"
		"textAlignment"             	"center"
		"Command"                   	"discard"
		"sound_depressed"           	"UI/buttonclick.wav"
		"sound_released"            	"UI/buttonclickrelease.wav"
		"defaultFgColor_override"   	"LtText"	// ClaudeHUD: colore esplicito in modalita' chiara
		"armedFgColor_override"     	"LtOnButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
		"depressedFgColor_override" 	"LtOnButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
		"defaultBgColor_override"   	"LtCardAlt"	// ClaudeHUD: colore esplicito in modalita' chiara
		"armedBgColor_override"     	"LtButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
		"depressedBgColor_override" 	"LtButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
	}
	"SubmitButton"
	{
		"ControlName"               	"CExButton"
		"fieldName"                 	"SubmitButton"
		"xpos"                      	"280"
		"ypos"                      	"370"
		"zpos"                      	"1"
		"wide"                      	"130"
		"tall"                      	"25"
		"labelText"                 	"#AbuseReport_Submit"
		"font"                      	"HudFontSmallBold"
		"textAlignment"             	"center"
		"Command"                   	"submit"
		"sound_depressed"           	"UI/buttonclick.wav"
		"sound_released"            	"UI/buttonclickrelease.wav"
		"defaultFgColor_override"   	"LtText"	// ClaudeHUD: colore esplicito in modalita' chiara
		"armedFgColor_override"     	"LtOnButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
		"depressedFgColor_override" 	"LtOnButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
		"defaultBgColor_override"   	"LtCardAlt"	// ClaudeHUD: colore esplicito in modalita' chiara
		"armedBgColor_override"     	"LtButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
		"depressedBgColor_override" 	"LtButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
	}
	"SaveForLaterButton"
	{
		"ControlName"               	"CExButton"
		"fieldName"                 	"SaveForLaterButton"
		"xpos"                      	"420"
		"ypos"                      	"370"
		"zpos"                      	"1"
		"wide"                      	"130"
		"tall"                      	"25"
		"labelText"                 	"#AbuseReport_SaveForLater"
		"font"                      	"HudFontSmallBold"
		"textAlignment"             	"center"
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
