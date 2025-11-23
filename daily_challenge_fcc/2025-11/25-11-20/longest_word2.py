def longest_word(sentence):
    words =[word.strip('?').strip('.').strip(',').strip('!').replace("'", '') for word in sentence.split()]
    lenghts = [len(word) for word in words]
    max_index = lenghts.index(max(lenghts))
    
    return words[max_index]