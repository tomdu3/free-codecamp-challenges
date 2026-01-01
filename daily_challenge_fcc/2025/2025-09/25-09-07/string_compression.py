def compress_string(sentence):
    words = sentence.split()
    result = []

    prev_word = None
    count = 0

    for word in words:
        if word == prev_word:
            count += 1
        else:
            if prev_word is not None:
                # Append the previous word with count if > 1
                if count > 1:
                    result.append(f"{prev_word}({count})")
                else:
                    result.append(prev_word)
            prev_word = word
            count = 1

    # Append the last word
    if prev_word is not None:
        if count > 1:
            result.append(f"{prev_word}({count})")
        else:
            result.append(prev_word)

    return " ".join(result)

if __name__ == '__main__':
    print(compress_string("yes yes yes please"))
    print(compress_string("I have have have apples"))
    print(compress_string("one one three and to the the the the"))
    print(compress_string("route route route route route route tee tee tee tee tee tee"))
