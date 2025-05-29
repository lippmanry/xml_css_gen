from xml_skel import xml_skeleton
from lone_panel_styles import lone_panel_css
from rows_tabs_css import rows_tabs_css

def dashboard_gen(num_rows, num_panels,odd_row_color="#12161A", even_row_color="#262F36",header_color="#00cefd", overwrite_indicators="True",incl_tool_tip="False"):
    num_rows = num_rows
    num_panels = num_panels
    odd_row_color = odd_row_color
    even_row_color = even_row_color
    overwrite_indicators = overwrite_indicators
    header_color = header_color
    incl_tool_tip = incl_tool_tip
    
    xml_skeleton(num_rows, num_panels)
    
    css_row_start = f'<row depends="$hideCSS$">\n <html>\n  <style>'
    css_row_end = f'  </style>\n </html>\n</row>'
    print(css_row_start)
    
    rows_tabs_css(num_rows, num_panels,odd_row_color, even_row_color,header_color, overwrite_indicators, incl_tool_tip)
    lone_panel_css(num_rows, num_panels)
    
    print(css_row_end)