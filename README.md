#Splunk Dashboard Generator

Quickly spin up a dashboard with this generator. This will set alternating row color and add "tabs" at the start of each row. Indicators for trends can be overwritten and tool tips can be included.

Arguments:
- num_rows: (Required) The number of rows you would like
- num_panels: (Required) The number of panels per row
- odd_row_color: (Optional) Hex code color for odd rows, default is #12161a
- even_row_color: (Optional) Hex code color for even rows, default is #262f36
- header_color: (Optional) Hex code color for the header text for each row, default is #00cefd
- overwrite_indicators: (Optional)
-  Value type: True/False
-  Purpose: will overwrite the colors for the directional trends (down = green #ADD2AD, up = red #FF5662)
- 
