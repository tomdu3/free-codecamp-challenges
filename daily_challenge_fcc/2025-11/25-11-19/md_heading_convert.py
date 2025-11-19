def convert(heading):
    heading = heading.strip().split()
    if len(heading[0].strip('#')) > 0:
        return 'Invalid format'
    elif len(heading[0]) > 6:
        return 'Invalid format'
    
    h_tag = 'h' + str(len(heading[0]))

    return f"<{h_tag}>{' '.join(heading[1:])}</{h_tag}>"