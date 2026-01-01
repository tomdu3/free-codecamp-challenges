def create_board(dimensions: list) -> list:

    board = []
    for i in range(dimensions[0]):
        row = []
        for j in range(dimensions[1]):
            if (i + j) % 2 == 0:
                row.append("X")
            else:
                row.append("O")
        board.append(row)
    return board

if __name__ == "__main__":
    print(create_board([3, 3]))
    print(create_board([6, 1]))
    print(create_board([2, 10]))
    print(create_board([5, 4]))

