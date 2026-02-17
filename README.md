## **Splunk Dashboard Generator**

Quickly spin up a dashboard with this generator. This will set alternating row color and add "tabs" at the start of each row. Indicators for trends can be overwritten and tool tips can be included.

**Arguments:**
- **num_rows (Required):**
  - Default: None
  - Value type: Int
  - Purpose: The number of rows you would like
- **num_panels (Required):**
  - Default: None
  - Value type: Int
  - Purpose: The number of panels per row
- **odd_row_color (Optional):**
  - Default: #12161A
  - Value type: Hex code
  - Purpose: Hex code color for odd rows
- **even_row_color (Optional):**
  - Default: #262F36
  - Value type: Hex code
  - Purpose: Hex code color for even rows
- **header_color (Optional):**
  - Default: #00CEFD
  - Value type: Hex code
  - Purpose: Hex code color for the header text for each row
- **overwrite_indicators (Optional):**
  - Default: True (down = green #ADD2AD, up = red #FF5662)
  - Value type: True/False
  - Purpose: will overwrite the colors for the directional trends
- **incl_tool_tip (Optional):**
  - Default: False
  - Value type: True/False
  - Purpose: Will include a CSS tool tip for each panel
 
To use this, clone the repo locally. It's easiest to use in a Jupyter Notebook so you can easily copy the output.
```from dashboard_generator import dashboard_gen```
```dashboard_gen(6,4)```
One the dashboard gen has finished running, press the 3 buttons next to the cell output and click 'copy cell content'
<img width="342" height="196" alt="image" src="https://github.com/user-attachments/assets/fa904326-7c19-4f01-b243-5f162e7e7a2b" />

