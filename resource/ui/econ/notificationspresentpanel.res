// ClaudeHUD: migrato ai token (layout originale) - generato da tools/migrate.py
// modalita': dark (DESIGN.md par. 9)
"Resource/UI/NotificationsPresentPanel.res"
{
	"NotificationsPresentPanel"
	{
		"ControlName"      	"CNotificationsPresentPanel"
		"fieldName"        	"NotificationsPresentPanel"
		"xpos"             	"c80"
		"ypos"             	"25"
		"zpos"             	"10000"
		"wide"             	"220"
		"tall"             	"26"
		"visible"          	"0"
		"enabled"          	"1"
		"border"           	"TFThinLineBorder"
		"bgcolor_override" 	"DkCard"	// ClaudeHUD: riempimento al posto del bordo texture
	}
	"TextLabel"
	{
		"ControlName"          	"CExLabel"
		"fieldName"            	"TextLabel"
		"fgcolor"              	"DkText"
		"xpos"                 	"cs-0.5"
		"ypos"                 	"0"
		"zpos"                 	"2"
		"wide"                 	"f10"
		"tall"                 	"f0"
		"autoResize"           	"0"
		"pinCorner"            	"0"
		"visible"              	"1"
		"enabled"              	"1"
		"wrap"                 	"0"
		"labelText"            	"#Notifications_Present"
		"textAlignment"        	"center"
		"font"                 	"TFFontSmall"
		"proportionaltoparent" 	"1"
	}
}
