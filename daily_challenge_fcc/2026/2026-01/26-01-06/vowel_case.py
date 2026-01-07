def vowel_case(s):
    vowels = "aeiou"
    res = ""
    for ch in s:
        if ch.lower() in vowels:
            res += ch.upper()
        else:
            res += ch.lower()

    return res

if __name__ == '__main__':
    print(vowel_case("vowelcase"))
    print(vowel_case("coding is fun"))
    print(vowel_case("HELLO, world!"))
    print(vowel_case("git cherry-pick"))
    print(vowel_case("HEAD~1"))
