def knight_moves(position):
    col, row = ord(position[0])-65, int(position[1])-1
    positions = [
        (-1,2),
        (-1,-2),
        (1,2),
        (1,-2),
        (2,1),
        (2,-1),
        (-2,1),
        (-2,-1)
    ]
    moves = 0
    for c, r in positions:
        if 0<=col+c<=7 and 0<=row+r<=7:
            moves +=1
    return moves

if __name__ == '__main__':
    print(knight_moves("A1"), 2)
    print(knight_moves("D4"), 8)
    print(knight_moves("G6"), 6)
    print(knight_moves("B8"), 3)
    print(knight_moves("H3"), 4)
