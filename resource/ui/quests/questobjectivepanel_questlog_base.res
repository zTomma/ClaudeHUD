// ClaudeHUD: migrato ai token (layout originale) - generato da tools/migrate.py
// modalita': dark (DESIGN.md par. 9)
"Resource/UI/HudAchievementTrackerItem.res"
{
	"QuestObjectiveTextPanel"
	{
		"ControlName"                  	"EditablePanel"
		"fieldName"                    	"QuestObjectiveTextPanel"
		"xpos"                         	"p0.03"
		"ypos"                         	"p0.5"
		"zpos"                         	"300"
		"wide"                         	"f0"
		"tall"                         	"f0"
		"visible"                      	"1"
		"enabled"                      	"1"
		"mouseinputenabled"            	"0"
		"proportionaltoparent"         	"1"
		"PaintBackgroundType"          	"2"
		"enabled_text_color_override"  	"39 38 36 255"	// token: DkCard
		"disabled_text_color_override" 	"39 38 36 255"	// token: DkCard
		"normal_token"                 	"#QuestObjective_Required"
		"advanced_token"               	"#QuestObjective_Optional"
	}
	"AttribDesc"
	{
		"ControlName"          	"CExLabel"
		"fieldName"            	"AttribDesc"
		"labeltext"            	"%attr_desc%"
		"xpos"                 	"0"
		"ypos"                 	"0"
		"wide"                 	"f0"
		"tall"                 	"f0"
		"zpos"                 	"4"
		"font"                 	"QuestObjectiveText"
		"wrap"                 	"1"
		"TextAlignment"        	"north-west"
		"proportionaltoparent" 	"1"
	}
	"AttribGlow"
	{
		"ControlName"          	"Label"
		"fieldName"            	"AttribGlow"
		"labeltext"            	"%attr_desc%"
		"xpos"                 	"0"
		"ypos"                 	"0"
		"wide"                 	"f0"
		"tall"                 	"f0"
		"zpos"                 	"4"
		"visible"              	"0"
		"font"                 	"QuestObjectiveTracker_DescBlur"
		"textinsetx"           	"5"
		"textAlignment"        	"north-west"
		"wrap"                 	"1"
		"proportionaltoparent" 	"1"
	}
}
