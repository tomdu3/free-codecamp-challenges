def parse_bold(markdown):
    bold = ['**', '__']
    splitted = markdown.split()
    is_bold = not (True in [b in splitted for b in bold])
    if is_bold:
        for b in bold:
            count = 0
            while True:
                if b not in markdown:
                    break
                count+=1
                index = markdown.index(b)
                if count % 2:
                    markdown = markdown[:index] + '<b>' + markdown[index+len(b):]
                else:
                    markdown = markdown[:index] + '</b>' + markdown[index+len(b):]
    return markdown


if __name__ == '__main__':
    print(parse_bold("**This is bold**"))
    print(parse_bold("__This is also bold__"))
    print(parse_bold("**This is not bold **"))
    print(parse_bold("__ This is also not bold__"))
    print(parse_bold("The **quick** brown fox __jumps__ over the **lazy** dog."))