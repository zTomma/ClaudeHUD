// ClaudeHUD: migrato ai token (layout originale) - generato da tools/migrate.py
// modalita': dark (DESIGN.md par. 9)
#base "QuestLogPanel.res"
"Resource/UI/econ/QuestLogPanel.res"
{
	"QuestLog"
	{
		"ControlName"          	"CQuestLogPanel"
		"fieldName"            	"QuestLog"
		"xpos"                 	"c5"
		"ypos"                 	"65"
		"zpos"                 	"1"
		"wide"                 	"300"
		"tall"                 	"350"
		"visible"              	"0"
		"enabled"              	"1"
		"proportionaltoparent" 	"1"
	}
	"MainContainer"
	{
		"border"           	"MainMenuBGBorder"
		"QuestLogTitle"
		{
			"font"      	"HudFontSmallBold"
			"labelText" 	"#QuestLog_Title_Halloween"
			"fgcolor"   	"DkText"
		}
		"QuestList"
		{
			"no_quests"    	"#QuestLog_NoQuests_Halloween"
			"need_a_pass"  	"#QuestLog_NeedPassForContracts_Halloween"
			"not_possible" 	"#QuestLog_NoContractsPossible_Halloween"
		}
		"bgcolor_override" 	"DkCard"	// ClaudeHUD: riempimento al posto del bordo texture
	}
	"ProgressPanel"
	{
		"ContractMeterContainer"
		{
			"bgcolor_override" 	"Clear"
			"ContractsCompletedProgressMeter"
			{
				"visible" 	"0"
			}
		}
	}
}
