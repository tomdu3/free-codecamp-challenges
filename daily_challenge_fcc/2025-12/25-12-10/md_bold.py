import re

def parse_bold(markdown):
    markdown = re.sub(r'\*\*(\S(?:.*?\S)?)\*\*', r'<b>\1</b>', markdown)
    markdown = re.sub(r'__(\S(?:.*?\S)?)__', r'<b>\1</b>', markdown)

    return markdown