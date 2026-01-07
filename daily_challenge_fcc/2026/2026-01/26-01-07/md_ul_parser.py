def parse_unordered_list(markdown):
    lines = markdown.split("\n")
    items = []

    for line in lines:
        line = line.strip()
        if line.startswith("- "):
            item_text = line[2:].strip()
            items.append(f"<li>{item_text}</li>")

    return "<ul>" + "".join(items) + "</ul>"
