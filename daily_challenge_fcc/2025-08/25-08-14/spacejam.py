def space_jam(s):
    s = s.replace(' ', '').upper()
    new_s = '  '.join(list(s))
    return new_s

if __name__ == '__main__':
    print(space_jam("freeCodeCamp"))
    print(space_jam("   free   Code   Camp   "))
    print(space_jam("Hello World?!"))
    print(space_jam("C@t$ & D0g$"))
    print(space_jam("allyourbase"))
