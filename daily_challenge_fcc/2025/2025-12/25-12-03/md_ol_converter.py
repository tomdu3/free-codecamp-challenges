import re
def convert_list_item(markdown):
    pattern = r'^\s*\d+\.\s+(.*)$'
    match = re.match(pattern, markdown)
    if match:
        return f"<li>{match.group(1)}</li>"
    return "Invalid format"