def parse_italics(markdown):
    i_tags = ['*', '_']
    italics = []
    is_open = False
    html = ''
    i = 0
    while True:
        if markdown == '':
            html = markdown
            break
        if i >= len(markdown) :
            break
        if markdown[i] in i_tags:
            if is_open:
                if markdown[i-1] == ' ':
                    html = markdown
                    break
                html +='</i>'
                is_open = False
            else:
                if markdown[i+1] != len(markdown):
                    if markdown[i+1] == ' ':
                        html = markdown
                        break

                    html += '<i>'
                    is_open = True
        else:
            html += markdown[i]
        i += 1
    return html

                

