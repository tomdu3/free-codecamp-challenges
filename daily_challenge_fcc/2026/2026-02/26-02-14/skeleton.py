def get_difficulty(track):
    prev = None
    points = 0

    for direction in track:
        if direction == "S" or not prev:
            prev = direction
            continue

        points += (
            15
            if (prev == "L" and direction == "R") or (prev == "R" and direction == "L")
            else 5
        )
        prev = direction

    if points > 200:
        return "Hard"
    elif points > 100:
        return "Medium"
    else:
        return "Easy"


if __name__ == "__main__":

    print(get_difficulty("SLSLLSRRLSRLRL"))
    print(get_difficulty("LLRSLRLRSLLRLRSLRRLRSRLLS"))
    print(get_difficulty("SRRRRLSLLRLRSSRLSRL"))
    print(get_difficulty("LSRLRLSRLRLSLRSLRLLRLSRLRLRSL"))
    print(get_difficulty("SLLSSLRLSLSLRSLSSLRL"))
    print(get_difficulty("SRSLSRSLSRRSLSRSRSLSRLSRSR"))
