def xml_skeleton(num_rows, num_panels):
    num_rows = num_rows
    num_panels = num_panels
    max_buff = num_rows - 1
    for i in range(num_rows):
        i = 1 + i
        tab_builder = f'<row id="row{i}Tab">\n <panel id="r{i}Tab">\n  <html>\n   <H1>Header Text</H1>\n    <p style="line-height: 0;">subheading</p>\n   </html>\n  </panel>\n </row>'
        row_xml_start = f'<row id="row{i}">' 
        row_xml_end = f'</row>'
        if i <= max_buff:
            buffer_row = f'<row>\n <panel id="bufferRow{i}">\n  <html>\n   <style>\n    #bufferRow{i} {{\n     height: 1vw !important;\n     width: 0vw !important;\n     background-color: #171D21 !important\n     color: #171D21 !important;\n     }}\n    </style>\n   </html>\n  </panel>\n</row>'
        else:
            buffer_row = ""    
        print(tab_builder)
        print(row_xml_start)
        for k in range(num_panels):
            k = 1 + k
            
            panel_xml = f'<panel id="row{i}Panel{k}"> \n  <single>\n   <title></title>\n    <search>\n     <query>\n      | makeresults\n      | eval high = 100, low = 1, value = round(((random() % high)/(high)) * (high - low) + low)\n      | table value\n     </query>\n    </search>\n<!-- edit options as needed -->\n    <option name="colorBy">value</option>\n    <option name="colorMode">none</option>\n    <option name="numberPrecision">0</option>\n    <option name="rangeColors">["0xFF5662","0xFFE17A","0xADD2AD"]</option>\n    <option name="rangeValues">[80,90]</option>\n    <option name="trendColorInterpretation">inverse</option>\n    <option name="unit">%</option>\n    <option name="useColors">1</option>\n   </single>\n  </panel>'
            
            print(panel_xml)
        print(row_xml_end)
        print(buffer_row)
        