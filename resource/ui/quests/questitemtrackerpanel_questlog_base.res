// ClaudeHUD: migrato ai token (layout originale) - generato da tools/migrate.py
// modalita': dark (DESIGN.md par. 9)
#base "QuestItemTrackerPanel_Base.res"
"Resource/UI/HudAchievementTrackerItem.res"
{
	"ItemTrackerPanel"
	{
		"xpos"                            	"0"
		"ypos"                            	"0"
		"wide"                            	"f0"
		"tall"                            	"100"
		"propotionaltoparent"             	"1"
		"bar_gap"                         	"5"
		"attrib_y_step"                   	"5"
		"map_view"                        	"1"
		"item_attribute_res_file"         	"resource/UI/quests/QuestObjectivePanel_QuestLog_Base.res"
		"progress_bar_standard_loc_token" 	"#QuestPoints_Standard"
		"progress_bar_advanced_loc_token" 	"#QuestPoints_Bonus"
	}
	"ItemName"
	{
		"visible" 	"0"
	}
	"ProgressBarBG"
	{
		"wide"                 	"f0"
		"proportionaltoparent" 	"1"
		"bgcolor_override"     	"DkCardA30"
		"PointsLabel"
		{
			"fgcolor_override" 	"DkCard"
			"font"             	"QuestFlavorText"
		}
		"ProgressBarStandard"
		{
			"ControlName"          	"EditablePanel"
			"fieldName"            	"ProgressBarStandard"
			"visible"              	"1"
			"enabled"              	"1"
			"proportionaltoparent" 	"1"
			"bgcolor_override"     	"DkCardA70"
			"PointsLabelInvert"
			{
				"font"             	"QuestFlavorText"
				"fgcolor_override" 	"DkText"
			}
		}
		"ProgressBarBonus"
		{
			"bgcolor_override" 	"DkBluFill"
			"PointsLabelInvert"
			{
				"font"             	"QuestFlavorText"
				"fgcolor_override" 	"DkText"
			}
		}
	}
}
