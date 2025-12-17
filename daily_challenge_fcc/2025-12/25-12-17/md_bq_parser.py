def parse_blockquote(markdown):
    bq_part = ''
    if '>' in markdown:
        tag = markdown.index('>')
        tag_part = markdown[:tag+1]
        if len(tag_part) + 2 < len(markdown) and '<' not in tag_part:
            bq_part = f"<blockquote>{markdown[tag+2:].strip()}</blockquote>"

    return bq_part