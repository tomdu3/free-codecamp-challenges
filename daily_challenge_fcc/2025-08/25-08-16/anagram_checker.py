def are_anagrams(str1, str2):
    return sorted(str1.replace(' ', '').lower()) == sorted(str2.replace(' ', '').lower())


if __name__ == '__main__':
    print(are_anagrams("listen", "silent"))
    print(are_anagrams("School master", "The classroom"))
    print(are_anagrams("A gentleman", "Elegant man"))
    print(are_anagrams("Hello", "World"))
    print(are_anagrams("apple", "banana"))
    print(are_anagrams("cat", "dog"))
