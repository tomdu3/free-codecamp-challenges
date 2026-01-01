def get_longest_word(sentence):
    words = [word.replace('.', '') for word in sentence.split()]
    word_lengths = [len(word) for word in words]
    return words[word_lengths.index(max(word_lengths))]