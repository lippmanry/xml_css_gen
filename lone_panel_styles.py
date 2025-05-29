def lone_panel_css(num_rows, num_panels):
    e = 0
    o = 0
    x = 0
    y= 0
    odd_panels_classes_first = ""
    odd_panels_classes_mid = ""
    odd_panels_classes_last = ""

    even_panels_classes_first = ""
    even_panels_classes_mid = ""
    even_panels_classes_last = ""

    even_rows = 0
    odd_rows = 0
    num_rows = num_rows
    num_panels = num_panels
    for i in range(num_rows):
        i = i + 1
        j = i - 1
        if i % 2 == 0:
            even_rows += 1
        else:
            odd_rows += 1


    for i in range(num_rows):
        odd_mid_panels = (num_panels * odd_rows) - (odd_rows * 2)
        even_mid_panels= (num_panels * even_rows) - (even_rows * 2)
        i = 1 + i
        j = i % 2
        if j == 0:
            e += 1
        else:
            o += 1  
        for k in range(num_panels):
            k = k + 1

            if j != 0:
                if k == 1:
                    if j != 0 and o == odd_rows:
                        last_count = ""
                    elif j != 0 and o < odd_rows:
                        last_count = ",\n"
                    odd_panels_classes_first = odd_panels_classes_first + f'\t#row{i}Panel{k}{last_count}'
                        
                elif k == num_panels:
                    if j != 0 and o == odd_rows:
                        last_count = ""
                    elif j != 0 and o < odd_rows:
                        last_count = ",\n"
                    odd_panels_classes_last = odd_panels_classes_last + f'\t#row{i}Panel{k}{last_count}'
                else:
                    x = x + 1
                    if j != 0 and x == odd_mid_panels:
                        last_count = ""
                    elif j != 0 and x < odd_mid_panels:
                        last_count = ",\n"                
                    odd_panels_classes_mid = odd_panels_classes_mid + f'\t#row{i}Panel{k}{last_count}'
            
            if j == 0:
                if k == 1:
                    if j == 0 and e == even_rows:
                        last_count = ""
                    elif j == 0 and e < even_rows:
                        last_count = ",\n"
                    even_panels_classes_first = even_panels_classes_first + f'\t#row{i}Panel{k}{last_count}'
                        
                elif k == num_panels:
                    if j == 0 and e == even_rows:
                        last_count = ""
                    elif j == 0 and e < even_rows:
                        last_count = ",\n"
                    even_panels_classes_last = even_panels_classes_last + f'\t#row{i}Panel{k}{last_count}'
                else:
                    y = y + 1
                    if j == 0 and y == even_mid_panels:
                        last_count = ""
                    elif j == 0 and y < even_mid_panels:
                        last_count = ",\n"                
                    even_panels_classes_mid = even_panels_classes_mid + f'\t#row{i}Panel{k}{last_count}'        
            
    if odd_mid_panels == 0:
        odd_mid_css = ""
    elif odd_mid_panels != 0:
        odd_mid_css = f'{odd_panels_classes_mid} {{\n\t margin: 0.6em 0.3em .6em .3em !important;\n\t border: 2px solid white !important;\n\t border-radius: 10px;\n\t background-color: #000000;\n\t}}'
    if even_mid_panels == 0:
        even_mid_css = ""
    elif even_mid_panels != 0:
        even_mid_css = f'{even_panels_classes_mid} {{\n\t margin: 0.6em 0.3em .6em .3em !important;\n\t border: 2px solid white !important;\n\t border-radius: 10px;\n\t background-color: #000000;\n\t}}'
        
    odd_panels_alone = f'\n/*###### DARK gray panels ######*/\n\n\n\t/*###### first panel has different margins ######*/\n\n{odd_panels_classes_first} {{\n\t margin: .6em 0.3em .6em .6em !important;\n\t border: 2px solid white !important;\n\t border-radius: 10px;\n\t background-color: #000000;\n\t}}\n\n{odd_mid_css} \n\n\t/*###### last panel has different margins ######*/\n\n{odd_panels_classes_last} {{\n\t margin: .6em 0.6em .6em .3em !important;\n\t border: 2px solid white !important;\n\t border-radius: 10px;\n\t background-color: #000000;\n\t}}\n\n'
    even_panels_alone = f'\n/*###### LIGHT gray panels ######*/\n\n\n\t/*###### first panel has different margins ######*/\n\n{even_panels_classes_first} {{\n\t margin: .6em 0.3em .6em .6em !important;\n\t border: 2px solid white !important;\n\t border-radius: 10px;\n\t background-color: #000000;\n\t}}\n\n{even_mid_css}\n\n\t/*###### last panel has different margins ######*/\n\n{even_panels_classes_last} {{\n\t margin: .6em 0.6em .6em .3em !important;\n\t border: 2px solid white !important;\n\t border-radius: 10px;\n\t background-color: #000000;\n\t}}\n\n'
    print(odd_panels_alone,even_panels_alone)   