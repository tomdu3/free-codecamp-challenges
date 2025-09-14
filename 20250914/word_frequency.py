def get_words(paragraph):
    words = [word.lower().replace('.', '').replace(',', '').replace('!', '') for word in paragraph.split()]
    words_dict = {}
    for word in words:
        words_dict[word] = words_dict.get(word, 0) + 1
    sorted_words = sorted(words_dict, key=words_dict.get, reverse=True)
    return sorted_words[:3]