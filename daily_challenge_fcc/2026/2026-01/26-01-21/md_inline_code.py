def parse_inline_code(markdown):
    tag_open = False
    html = ""
    for char in markdown:
        if char == "`":
            if tag_open:
                html += "</code>"
                tag_open = False
            else:
                html += "<code>"
                tag_open = True
        else:
            html += char

    return html
