def rows_tabs_css(num_rows, num_panels, odd_row_color="#12161A", even_row_color="#262F36", header_color="#00cefd", overwrite_indicators="True", incl_tool_tip="False"):
    try:
        num_rows = num_rows
        num_panels = num_panels
        overwrite_ind = overwrite_indicators
        odd_row_color = odd_row_color
        even_row_color = even_row_color
        header_color = header_color
        incl_tool_tip = incl_tool_tip        
        if (type(num_rows) and type(num_panels) != int):
            raise ValueError("Row and panel values must be integers. One or more definitions are incorrectly formatted.",type(num_panels))
        if type(overwrite_ind) != str and type(overwrite_ind) != bool:
            raise ValueError("Overwrite indicators value must be true or false.")
        if '#' not in odd_row_color or '#' not in even_row_color or '#' not in header_color:
            raise ValueError("Color definitions must be in hex format (# and alphanumeric hex code). One or more definitions are incorrectly formatted.")
        if type(incl_tool_tip) != str and type(incl_tool_tip) != bool:
            raise ValueError("Tool tip option must be true or false.")        

    except ValueError as e:
        print("Error:", e)
    
    overwrite_indicators = str(overwrite_ind).lower()
    incl_tool_tip = str(incl_tool_tip).lower()
        
    even_rows = 0
    odd_rows = 0


    for i in range(num_rows):
        i = i + 1
        if i % 2 == 0:
            even_rows += 1
        else:
            odd_rows += 1


    even_tab_panel_classes = ""
    even_tab_alone_classes = ""
    even_row_alone_classes = ""

    odd_tab_panel_classes = ""
    odd_tab_alone_classes = ""
    odd_row_alone_classes = ""

    all_tabs_rows_classes = ""
    all_tabs_panels_classes = ""
    all_rows_alone_classes = ""
    all_rows_panel_classes = ""
    tool_tip = ""



    e = 0
    o = 0

    for i in range(num_rows):
        i = i + 1
        j = i % 2  
        if j == 0:
            e += 1
        else:
            o += 1
        
        #handle even rows
        if j == 0 and e == even_rows:
            last_count = ""
        elif j == 0 and e < even_rows:
            last_count = ",\n"

        #handle odd rows 
        if j != 0 and o == odd_rows:
            last_count = ""
        elif j != 0 and o < odd_rows:
            last_count = ",\n"
        
        #handle all rows commas
        if i == num_rows:
            all_last_count = ""
        elif i < num_rows:
            all_last_count = ",\n"

        
        #light gray tabs/rows
        if j == 0:
            color = even_row_color
            even_tab_panel_classes = even_tab_panel_classes + f'\t#r{i}Tab .dashboard-panel{last_count}'
            even_tab_panels = f' {{\n\t border-radius: 12px 12px 0px 0px !important;\n \t background-color: {color};\n\t text-align: center; \n\t}}\n'
            even_tab_alone_classes = even_tab_alone_classes+ f'\t#row{i}Tab{last_count}'
            even_tab_alone = f' {{\n\t width: 15% !important;\n\t border-radius: 12px 12px 0px 0px !important;\n \t background-color: {color};\n\t}}\n'
            even_row_alone_classes = even_row_alone_classes + f'\t#row{i}{last_count}'
            even_row_alone = f' {{\n\t background-color: {color} !important;\n\t}}'    

        #dark gray tabs/rows    
        if j != 0:
            color = odd_row_color
            odd_tab_panel_classes = odd_tab_panel_classes + f'\t#r{i}Tab .dashboard-panel{last_count}'
            odd_tab_panels = f' {{\n\t border-radius: 12px 12px 0px 0px !important;\n \t background-color: {color};\n\t text-align: center; \n\t}}\n'
            odd_tab_alone_classes = odd_tab_alone_classes + f'\t#row{i}Tab{last_count}'
            odd_tab_alone = f' {{\n\t width: 15% !important;\n\t border-radius: 12px 12px 0px 0px !important;\n \t background-color: {color};\n\t}}\n'
            odd_row_alone_classes = odd_row_alone_classes + f'\t#row{i}{last_count}'
            odd_row_alone = f' {{\n\t background-color: {color} !important;\n\t}}'
        
        #all tabs - h1 and p
        all_tabs_rows_classes = all_tabs_rows_classes + f'\t#row{i}Tab H1{all_last_count}'
        all_tabs_rows = f' {{\n\t color: {header_color} !important;\n\t font-weight: bold !important;\n\t font-size: 22px !important;\n\t}}\n'
        all_tabs_panels_classes = all_tabs_panels_classes + f'\t#r{i}Tab .dashboard-panel p{all_last_count}'
        all_tabs_panels = f' {{\n\t text-align: center !important;\n\t font-size: 16px !important;\n\t padding: 5px 15px !important;\n\t color: {header_color} !important;}}\n'
        
        if num_rows == 1:            
            even_tab_panels = ""
            even_tab_alone = ""
            even_row_alone = ""             

        #all rows
        all_rows_alone_classes = all_rows_alone_classes + f'\t#row{i}{all_last_count}'
        all_rows_alone = f' {{\n\t display: flex !important;\n\t flex-direction: row !important;\n\t}}\n'
        all_rows_panel_classes =  all_rows_panel_classes + f'\t#row{i} .dashboard-panel{all_last_count}'
        
        for k in range(num_panels):
            k = 1 + k
            if incl_tool_tip == "true":        
                tool_tip = tool_tip + f'\t#row{i}Panel{k} .panel-element-row:hover:after {{\n\t background: #333;\n\t background: rgba(0,0,0,.8);\n\t border-radius: 5px;\n\t bottom: 26px;\n\t color: #fff;\n\t font-weight: bold !important;\n\t content: "Hover Text Contents";\n\t right: -5%;\n\t padding: 5px 15px;\n\t position: absolute;\n\t z-index: 300 !important;\n\t width: 220px;\n\t max-width:130px !important;\n\t height: 30px !important;\n\t display: block !important;\n\t overflow-wrap: break-word !important;\n\t opacity: 95% !important;\n\t top: -25% !important;\n\t }}\n'
            else:
                tool_tip = ""
        

    all_tabs_css = all_tabs_rows_classes + all_tabs_rows + all_tabs_panels_classes + all_tabs_panels

    all_panel_css = f'\n/*###### ALL panel CSS ######*/\n\n\t.dashboard-element-title {{\n\t font-size: 16px !important;\n\t text-align: center !important;\n\t font-weight: bold !important;\n\t}}\n\t.dashboard-row .dashboard-panel .panel-head h3 {{\n\t padding: 12px 12px 10px 12px !important;\n\t}}\n\t.dashboard-row .dashboard-panel p {{\n\t text-align: center !important;\n\t font-size: 11.5px !important;\n\t padding: 5px 15px !important\n\t}}\n'
    if overwrite_indicators == "true":
        all_rows_inc_css = f'\n/*###### ALL row CSS ######*/\n\n\t.dashboard-row .dashboard-panel .panel-body.html, .dashboard-row .dashboard-panel .panel-body.splunk-html {{\n\t padding: 0px;\n\t}}\n\t.dashboard-row {{\n\t border-radius: 0px 10px 10px 10px;\n\t}}\n\n\t/*###### changes indicator colors ######*/\n\n\tg.delta-indicator .delta-down-indicator polyline {{\n\t stroke: #ADD2AD !important;\n\t fill: #ADD2AD !important;\n\t}}\n\tg.delta-indicator.delta-down-indicator line {{\n\t fill: #ADD2AD !important;\n\t stroke: #ADD2AD !important;\n\t}}\n\tg.delta-indicator.delta-up-indicator polyline {{\n\t stroke: #FF5662 !important;\n\t}}\n\tg.delta-indicator.delta-up-indicator line {{\n\t fill: #FF5662 !important;\n\t stroke: #FF5662 !important;\n\t}}\n\n\t/*###### changes trendline colors - only white possible for override ######*/\n\n\tg.single-value-delta.shared-singlevalue-delta text {{\n\t fill: #FFF !important;\n\t}}\n\tg.single-value-sparkline.shared-singlevalue-sparkline path,\n\tg.single-value-sparkline.shared-singlevalue-sparkline circle {{\n\t fill: #FFF !important;\n\t stroke: #FFF !important;\n\t}}\n'
    elif overwrite_indicators == "false":
        all_rows_inc_css = f'\n/*###### ALL row CSS ######*/\n\n\t.dashboard-row .dashboard-panel .panel-body.html, .dashboard-row .dashboard-panel .panel-body.splunk-html {{\n\t padding: 0px;\n\t}}\n\t.dashboard-row {{\n\t border-radius: 0px 10px 10px 10px;\n\t}}\n'
    

    even_tabs_css = even_tab_panel_classes + even_tab_panels + even_tab_alone_classes + even_tab_alone 
    odd_tabs_css =  odd_tab_panel_classes + odd_tab_panels + odd_tab_alone_classes + odd_tab_alone 
    all_tabs_css = all_tabs_rows_classes + all_tabs_rows + all_tabs_panels_classes + all_tabs_panels
    odd_rows_css = odd_row_alone_classes + odd_row_alone
    even_rows_css = even_row_alone_classes + even_row_alone
    all_rows_css = all_rows_alone_classes + all_rows_alone
    all_rows_panels_css = all_rows_panel_classes + ' {\n\t background-color: #000000;\n\t border-radius: 10px;\n\t}'

    print('/*###### odd tabs - dark gray ######*/\n\n', odd_tabs_css, '\n/*###### even tabs - light gray ######*/\n\n', even_tabs_css, '\n/*###### ALL tabs ######*/\n\n', all_tabs_css, '\n/*###### odd rows - dark gray ######*/\n\n', odd_rows_css, '\n\n/*###### even rows - light gray ######*/\n\n', even_rows_css, '\n', all_rows_inc_css,'\n', all_rows_css, '\n', all_panel_css, '\n', all_rows_panels_css, '\n','\n/*###### tool tip css ######*/\n\n', tool_tip, '\n')