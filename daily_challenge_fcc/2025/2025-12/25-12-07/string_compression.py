from collections import Counter 
def compress_string(sentence):
    words = sentence.split()
    counter = Counter(words)
    compressed = ' '.join(f'{word}({counter[word]})' if counter[word] > 1 else word for word in counter)
    return compressed