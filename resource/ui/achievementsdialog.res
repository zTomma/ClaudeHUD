// ClaudeHUD: migrato ai token (layout originale) - generato da tools/migrate.py
// modalita': light (DESIGN.md par. 9)
"AchievementsDialog.res"
{
	"AchievementsDialog"
	{
		"ControlName"        	"CAchievementsDialog"
		"fieldName"          	"AchievementsDialog"
		"xpos"               	"272"
		"ypos"               	"154"
		"wide"               	"630"
		"tall"               	"444"
		"autoResize"         	"0"
		"pinCorner"          	"0"
		"visible"            	"1"
		"enabled"            	"1"
		"tabPosition"        	"0"
		"settitlebarvisible" 	"1"
		"title"              	"#GameUI_Achievements_Title"
		"borderwidth"        	"15"
	}
	"Back"
	{
		"ControlName"               	"Button"
		"fieldName"                 	"Back"
		"xpos"                      	"544"
		"ypos"                      	"410"
		"wide"                      	"70"
		"tall"                      	"24"
		"autoResize"                	"0"
		"pinCorner"                 	"3"
		"visible"                   	"1"
		"enabled"                   	"1"
		"tabPosition"               	"4"
		"labelText"                 	"#GameUI_Back"
		"textAlignment"             	"west"
		"dulltext"                  	"0"
		"brighttext"                	"0"
		"wrap"                      	"0"
		"Command"                   	"Close"
		"Default"                   	"0"
		"defaultFgColor_override"   	"LtText"	// ClaudeHUD: colore esplicito in modalita' chiara
		"armedFgColor_override"     	"LtOnButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
		"depressedFgColor_override" 	"LtOnButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
		"defaultBgColor_override"   	"LtCardAlt"	// ClaudeHUD: colore esplicito in modalita' chiara
		"armedBgColor_override"     	"LtButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
		"depressedBgColor_override" 	"LtButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
	}
	"ResetAchievements"
	{
		"ControlName"               	"Button"
		"fieldName"                 	"ResetAchievements"
		"xpos"                      	"25"
		"ypos"                      	"410"
		"wide"                      	"200"
		"tall"                      	"24"
		"autoResize"                	"0"
		"pinCorner"                 	"3"
		"visible"                   	"1"
		"enabled"                   	"1"
		"tabPosition"               	"0"
		"labelText"                 	"#TF_ConfirmResetAchievements_Title"
		"textAlignment"             	"west"
		"dulltext"                  	"0"
		"brighttext"                	"0"
		"wrap"                      	"0"
		"Command"                   	"ResetAchievements"
		"Default"                   	"0"
		"defaultFgColor_override"   	"LtText"	// ClaudeHUD: colore esplicito in modalita' chiara
		"armedFgColor_override"     	"LtOnButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
		"depressedFgColor_override" 	"LtOnButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
		"defaultBgColor_override"   	"LtCardAlt"	// ClaudeHUD: colore esplicito in modalita' chiara
		"armedBgColor_override"     	"LtButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
		"depressedBgColor_override" 	"LtButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
	}
	"listpanel_achievements"
	{
		"ControlName" 	"PanelListPanel"
		"fieldName"   	"listpanel_achievements"
		"xpos"        	"15"
		"ypos"        	"136"
		"wide"        	"600"
		"tall"        	"268"
		"autoResize"  	"3"
		"pinCorner"   	"0"
		"visible"     	"1"
		"enabled"     	"1"
		"tabPosition" 	"1"
	}
	"listpanel_background"
	{
		"ControlName" 	"ImagePanel"
		"fieldName"   	"listpanel_background"
		"xpos"        	"15"
		"ypos"        	"136"
		"wide"        	"600"
		"tall"        	"268"
		"fillcolor"   	"255 255 255 255"	// token: LtCard
		"zpos"        	"-3"
		"visible"     	"1"
		"enabled"     	"1"
		"pinCorner"   	"0"
		"autoResize"  	"3"
	}
	"PercentageBarBackground"
	{
		"ControlName" 	"ImagePanel"
		"fieldName"   	"PercentageBarBackground"
		"xpos"        	"23"
		"ypos"        	"67"
		"wide"        	"584"
		"tall"        	"16"
		"fillcolor"   	"255 255 255 255"	// token: LtCard
		"zpos"        	"-2"
		"visible"     	"0"
		"enabled"     	"1"
	}
	"PercentageBar"
	{
		"ControlName" 	"ImagePanel"
		"fieldName"   	"PercentageBar"
		"xpos"        	"23"
		"ypos"        	"67"
		"wide"        	"0"
		"tall"        	"16"
		"fillcolor"   	"217 119 87 255"	// token: LtAccent
		"zpos"        	"-1"
		"visible"     	"0"
		"enabled"     	"1"
	}
	"PercentageText"
	{
		"ControlName"      	"Label"
		"fieldName"        	"PercentageText"
		"xpos"             	"407"
		"ypos"             	"46"
		"wide"             	"200"
		"tall"             	"20"
		"autoResize"       	"0"
		"pinCorner"        	"0"
		"visible"          	"0"
		"enabled"          	"1"
		"tabPosition"      	"0"
		"labelText"        	"0%"
		"textAlignment"    	"east"
		"dulltext"         	"0"
		"brighttext"       	"0"
		"wrap"             	"0"
		"fillcolor"        	"217 119 87 255"	// token: LtButtonHover
		"font"             	"AchievementItemDescription"	// "defaultlarg"
		"fgcolor_override" 	"LtText"	// ClaudeHUD: colore esplicito in modalita' chiara
	}
	"achievement_pack_combo"
	{
		"ControlName" 	"ComboBox"
		"fieldName"   	"achievement_pack_combo"
		"xpos"        	"15"
		"ypos"        	"102"
		"wide"        	"225"
		"tall"        	"24"
		"enabled"     	"1"
		"visible"     	"1"
		"editable"    	"0"
	}
	"ProgressBackground"
	{
		"ControlName" 	"ImagePanel"
		"fieldName"   	"ProgressBackground"
		"xpos"        	"15"
		"ypos"        	"42"
		"wide"        	"600"
		"tall"        	"50"
		"fillcolor"   	"255 255 255 255"	// token: LtCard
		"zpos"        	"-3"
		"visible"     	"1"
		"enabled"     	"1"
	}
	"AchievementsEarnedLabel"
	{
		"ControlName"      	"Label"
		"fieldName"        	"AchievementsEarnedLabel"
		"xpos"             	"23"
		"ypos"             	"46"
		"wide"             	"200"
		"tall"             	"20"
		"autoResize"       	"0"
		"pinCorner"        	"0"
		"visible"          	"1"
		"enabled"          	"1"
		"tabPosition"      	"0"
		"labelText"        	"#GameUI_Achievements_Earned"
		"textAlignment"    	"west"
		"dulltext"         	"0"
		"brighttext"       	"0"
		"wrap"             	"0"
		"fillcolor"        	"217 119 87 255"	// token: LtButtonHover
		"font"             	"AchievementItemDescription"	// "defaultlarg"
		"fgcolor_override" 	"LtText"	// ClaudeHUD: colore esplicito in modalita' chiara
	}
	"HideAchieved"
	{
		"ControlName"      	"CheckButton"
		"fieldName"        	"HideAchieved"
		"xpos"             	"255"
		"ypos"             	"102"
		"wide"             	"150"
		"tall"             	"24"
		"autoResize"       	"0"
		"pinCorner"        	"0"
		"visible"          	"1"
		"enabled"          	"1"
		"tabPosition"      	"0"
		"labelText"        	"#GameUI_Achievement_Hide_Achieved"
		"textAlignment"    	"west"
		"dulltext"         	"0"
		"brighttext"       	"0"
		"wrap"             	"0"
		"font"             	"AchievementItemDescription"
		"fgcolor_override" 	"LtText"	// ClaudeHUD: colore esplicito in modalita' chiara
	}
}
