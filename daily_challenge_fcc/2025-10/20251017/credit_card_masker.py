def mask(card):
    delimiter = " "
    if not len(card_list := card.split()) == 4:
        delimiter = "-"
        card_list = card.split(delimiter)
        
    return delimiter.join(["****"] * 3 + [card_list[-1]])