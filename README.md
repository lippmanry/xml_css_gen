#Splunk Dashboard Generator

##Quickly spin up a dashboard with this generator. This will set alternating row color and add "tabs" at the start of each row. Indicators for trends can be overwritten and tool tips can be included.

Arguments:
- num_rows (Required):
  - Default: None
  - Value type: Int
  - Purpose: The number of rows you would like
- num_panels (Required):
  - Default: None
  - Value type: Int
  - Purpose: The number of panels per row
- odd_row_color (Optional):
  - Default: #12161A
  - Value type: Hex code
  - Purpose: Hex code color for odd rows
- even_row_color (Optional):
  - Default: #262F36
  - Value type: Hex code
  - Purpose: Hex code color for even rows
- header_color (Optional):
  - Default: #00CEFD
  - Value type: Hex code
  - Purpose: Hex code color for the header text for each row
- overwrite_indicators (Optional):
  - Default: True (down = green #ADD2AD, up = red #FF5662)
  - Value type: True/False
  - Purpose: will overwrite the colors for the directional trends
- incl_tool_tip (Optional):
  - Default: False
  - Value type: True/False
  - Purpose: Will include a CSS tool tip for each panel 
