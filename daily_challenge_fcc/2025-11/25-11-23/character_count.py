from collections import Counter
def count_characters(sentence):
    sentence = [letter for letter in sentence.lower() if letter.isalpha()]
    counter = Counter(sentence)
    result = [ f"{letter} {count}" for letter, count in counter.items()]
    return sorted(result)


if __name__ == "__main__":
    print(count_characters("hello world"))
    print(count_characters("I love coding challenges!"))
    print(count_characters("// TODO: Complete this challenge ASAP!"))