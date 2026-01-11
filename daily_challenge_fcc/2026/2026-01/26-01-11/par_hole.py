def golf_score(par, strokes):
    if strokes == 1:
        return "Hole in one!"
    strokes_dict = {
        2: "Eagle",
        1: "Birdie",
        0: "Par",
        -1: "Bogey",
        -2: "Double bogey"
            }
    if response := strokes_dict.get(par - strokes):
        return response
    return "Error"

if __name__ == '__main__':
    print(golf_score(3, 3))
    print(golf_score(4, 3))
    print(golf_score(3, 1))
    print(golf_score(5, 7))
    print(golf_score(4, 5))
    print(golf_score(5, 3))
