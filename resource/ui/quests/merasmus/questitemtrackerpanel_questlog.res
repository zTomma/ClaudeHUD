// ClaudeHUD: migrato ai token (layout originale) - generato da tools/migrate.py
// modalita': dark (DESIGN.md par. 9)
#base "..\QuestItemTrackerPanel_QuestLog_Base.res"
"Resource/UI/HudAchievementTrackerItem.res"
{
	"ItemTrackerPanel"
	{
		"item_attribute_res_file"         	"resource/UI/quests/merasmus/QuestObjectivePanel_QuestLog.res"
		"progress_bar_standard_loc_token" 	"#QuestPoints_Standard_Merasmus"
		"progress_bar_advanced_loc_token" 	"#QuestPoints_Bonus_Merasmus"
	}
	"ItemName"
	{
		"visible" 	"0"
	}
	"ProgressBarBG"
	{
		"tall" 	"10"
		"PointsLabel"
		{
			"fgcolor_override" 	"DkCard"
			"font"             	"QuestInstructionText_Merasmus"
		}
		"ProgressBarStandard"
		{
			"PointsLabelInvert"
			{
				"font"             	"QuestInstructionText_Merasmus"
				"fgcolor_override" 	"DkText"
			}
		}
		"ProgressBarBonus"
		{
			"PointsLabelInvert"
			{
				"font"             	"QuestInstructionText_Merasmus"
				"fgcolor_override" 	"DkText"
			}
		}
	}
}
