// ClaudeHUD: migrato ai token (layout originale) - generato da tools/migrate.py
// modalita': light (DESIGN.md par. 9)
"PublishedFileBrowserDialog.res"
{
	"PublishedFileBrowserDialog"
	{
		"ControlName"        	"CPublishedFileBrowserDialog"
		"fieldName"          	"PublishedFileBrowserDialog"
		"xpos"               	"0"
		"ypos"               	"0"
		"wide"               	"600"
		"tall"               	"292"
		"autoResize"         	"0"
		"pinCorner"          	"0"
		"visible"            	"1"
		"enabled"            	"1"
		"tabPosition"        	"0"
		"settitlebarvisible" 	"1"
		"Title"              	"#TF_PublishedFiles_Browse"
		"border"             	"QuickplayBorder"
		"bgcolor_override"   	"LtCard"	// ClaudeHUD: riempimento al posto del bordo texture
	}
	"Background"
	{
		"ControlName"      	"EditablePanel"
		"fieldName"        	"Background"
		"xpos"             	"0"
		"ypos"             	"0"
		"zpos"             	"-100"
		"wide"             	"600"
		"tall"             	"292"
		"autoResize"       	"0"
		"pinCorner"        	"0"
		"visible"          	"1"
		"enabled"          	"1"
		"tabPosition"      	"0"
		"bgcolor_override" 	"LtCard"
	}
	"LabelPublishedFiles"
	{
		"ControlName"      	"Label"
		"fieldName"        	"LabelPublishedFiles"
		"xpos"             	"32"
		"ypos"             	"32"
		"wide"             	"180"
		"tall"             	"24"
		"autoResize"       	"0"
		"pinCorner"        	"0"
		"visible"          	"1"
		"enabled"          	"1"
		"tabPosition"      	"0"
		"labelText"        	"#TF_PublishedFiles_Files"
		"textAlignment"    	"west"
		"dulltext"         	"0"
		"brighttext"       	"0"
		"wrap"             	"0"
		"fgcolor_override" 	"LtText"	// ClaudeHUD: colore esplicito in modalita' chiara
	}
	"PublishedFileList"
	{
		"ControlName"   	"ListPanel"
		"fieldName"     	"PublishedFileList"
		"xpos"          	"32"
		"ypos"          	"56"
		"wide"          	"300"
		"tall"          	"180"
		"autoResize"    	"0"
		"pinCorner"     	"0"
		"visible"       	"1"
		"enabled"       	"1"
		"tabPosition"   	"0"
		"textAlignment" 	"west"
		"dulltext"      	"0"
		"brighttext"    	"0"
		"wrap"          	"0"
	}
	"LabelPublishedFileTitle"
	{
		"ControlName"      	"Label"
		"fieldName"        	"LabelPublishedFileTitle"
		"xpos"             	"354"
		"ypos"             	"32"
		"wide"             	"180"
		"tall"             	"24"
		"autoResize"       	"0"
		"pinCorner"        	"0"
		"visible"          	"1"
		"enabled"          	"1"
		"tabPosition"      	"0"
		"labelText"        	"#TF_PublishFile_TitleLabel"
		"textAlignment"    	"west"
		"dulltext"         	"0"
		"brighttext"       	"0"
		"wrap"             	"0"
		"fgcolor_override" 	"LtText"	// ClaudeHUD: colore esplicito in modalita' chiara
	}
	"LabelPublishedFileTitleValue"
	{
		"ControlName"      	"Label"
		"fieldName"        	"LabelPublishedFileTitleValue"
		"xpos"             	"354"
		"ypos"             	"56"
		"wide"             	"250"
		"tall"             	"24"
		"autoResize"       	"0"
		"pinCorner"        	"0"
		"visible"          	"1"
		"enabled"          	"1"
		"tabPosition"      	"0"
		"textAlignment"    	"west"
		"dulltext"         	"0"
		"brighttext"       	"0"
		"wrap"             	"0"
		"labelText"        	""
		"fgcolor_override" 	"LtText"	// ClaudeHUD: colore esplicito in modalita' chiara
	}
	"LabelPublishedFileDesc"
	{
		"ControlName"      	"Label"
		"fieldName"        	"LabelPublishedFileDesc"
		"xpos"             	"354"
		"ypos"             	"100"
		"wide"             	"180"
		"tall"             	"24"
		"autoResize"       	"0"
		"pinCorner"        	"0"
		"visible"          	"1"
		"enabled"          	"1"
		"tabPosition"      	"0"
		"labelText"        	"#TF_PublishFile_DescLabel"
		"textAlignment"    	"west"
		"dulltext"         	"0"
		"brighttext"       	"0"
		"wrap"             	"1"
		"fgcolor_override" 	"LtText"	// ClaudeHUD: colore esplicito in modalita' chiara
	}
	"LabelPublishedFileDescValue"
	{
		"ControlName"      	"Label"
		"fieldName"        	"LabelPublishedFileDescValue"
		"xpos"             	"354"
		"ypos"             	"124"
		"wide"             	"250"
		"tall"             	"112"
		"autoResize"       	"0"
		"pinCorner"        	"1"
		"visible"          	"1"
		"enabled"          	"1"
		"tabPosition"      	"0"
		"textAlignment"    	"north-west"
		"dulltext"         	"0"
		"brighttext"       	"0"
		"wrap"             	"1"
		"labelText"        	""
		"fgcolor_override" 	"LtText"	// ClaudeHUD: colore esplicito in modalita' chiara
	}
	"ButtonAddFile"
	{
		"ControlName"               	"Button"
		"fieldName"                 	"ButtonAddFile"
		"xpos"                      	"32"
		"ypos"                      	"244"
		"wide"                      	"64"
		"tall"                      	"24"
		"autoResize"                	"0"
		"pinCorner"                 	"0"
		"visible"                   	"1"
		"enabled"                   	"1"
		"tabPosition"               	"0"
		"labelText"                 	"#TF_PublishedFiles_Add"
		"textAlignment"             	"center"
		"dulltext"                  	"0"
		"brighttext"                	"0"
		"wrap"                      	"0"
		"Command"                   	"AddFile"
		"Default"                   	"0"
		"defaultFgColor_override"   	"LtText"	// ClaudeHUD: colore esplicito in modalita' chiara
		"armedFgColor_override"     	"LtOnButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
		"depressedFgColor_override" 	"LtOnButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
		"defaultBgColor_override"   	"LtCardAlt"	// ClaudeHUD: colore esplicito in modalita' chiara
		"armedBgColor_override"     	"LtButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
		"depressedBgColor_override" 	"LtButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
	}
	"ButtonDeleteFile"
	{
		"ControlName"               	"Button"
		"fieldName"                 	"ButtonDeleteFile"
		"xpos"                      	"104"
		"ypos"                      	"244"
		"wide"                      	"64"
		"tall"                      	"24"
		"autoResize"                	"0"
		"pinCorner"                 	"0"
		"visible"                   	"1"
		"enabled"                   	"1"
		"tabPosition"               	"0"
		"labelText"                 	"#TF_PublishedFiles_Delete"
		"textAlignment"             	"center"
		"dulltext"                  	"0"
		"brighttext"                	"0"
		"wrap"                      	"0"
		"Command"                   	"DeleteFile"
		"Default"                   	"0"
		"defaultFgColor_override"   	"LtText"	// ClaudeHUD: colore esplicito in modalita' chiara
		"armedFgColor_override"     	"LtOnButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
		"depressedFgColor_override" 	"LtOnButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
		"defaultBgColor_override"   	"LtCardAlt"	// ClaudeHUD: colore esplicito in modalita' chiara
		"armedBgColor_override"     	"LtButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
		"depressedBgColor_override" 	"LtButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
	}
	"ButtonEditFile"
	{
		"ControlName"               	"Button"
		"fieldName"                 	"ButtonEditFile"
		"xpos"                      	"176"
		"ypos"                      	"244"
		"wide"                      	"64"
		"tall"                      	"24"
		"autoResize"                	"0"
		"pinCorner"                 	"0"
		"visible"                   	"1"
		"enabled"                   	"1"
		"tabPosition"               	"0"
		"labelText"                 	"#TF_PublishedFiles_Edit"
		"textAlignment"             	"center"
		"dulltext"                  	"0"
		"brighttext"                	"0"
		"wrap"                      	"0"
		"Command"                   	"EditFile"
		"Default"                   	"0"
		"defaultFgColor_override"   	"LtText"	// ClaudeHUD: colore esplicito in modalita' chiara
		"armedFgColor_override"     	"LtOnButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
		"depressedFgColor_override" 	"LtOnButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
		"defaultBgColor_override"   	"LtCardAlt"	// ClaudeHUD: colore esplicito in modalita' chiara
		"armedBgColor_override"     	"LtButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
		"depressedBgColor_override" 	"LtButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
	}
	"ButtonRefresh"
	{
		"ControlName"               	"Button"
		"fieldName"                 	"ButtonRefresh"
		"xpos"                      	"248"
		"ypos"                      	"244"
		"wide"                      	"64"
		"tall"                      	"24"
		"autoResize"                	"0"
		"pinCorner"                 	"0"
		"visible"                   	"1"
		"enabled"                   	"1"
		"tabPosition"               	"0"
		"labelText"                 	"#TF_PublishedFiles_Refresh"
		"textAlignment"             	"center"
		"dulltext"                  	"0"
		"brighttext"                	"0"
		"wrap"                      	"0"
		"Command"                   	"Refresh"
		"Default"                   	"0"
		"defaultFgColor_override"   	"LtText"	// ClaudeHUD: colore esplicito in modalita' chiara
		"armedFgColor_override"     	"LtOnButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
		"depressedFgColor_override" 	"LtOnButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
		"defaultBgColor_override"   	"LtCardAlt"	// ClaudeHUD: colore esplicito in modalita' chiara
		"armedBgColor_override"     	"LtButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
		"depressedBgColor_override" 	"LtButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
	}
	"ButtonClose"
	{
		"ControlName"               	"Button"
		"fieldName"                 	"ButtonClose"
		"xpos"                      	"320"
		"ypos"                      	"244"
		"wide"                      	"64"
		"tall"                      	"24"
		"autoResize"                	"0"
		"pinCorner"                 	"0"
		"visible"                   	"1"
		"enabled"                   	"1"
		"tabPosition"               	"0"
		"labelText"                 	"#TF_CLOSE"
		"textAlignment"             	"center"
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
}
