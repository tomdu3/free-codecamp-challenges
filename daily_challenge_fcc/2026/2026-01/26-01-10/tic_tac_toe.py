def tic_tac_toe(board):
    row_wins = [board[0], board[1], board[2]]
    col_wins = [[x, y, z] for x, y, z in zip(*board)]
    diag_wins = [
        [board[0][0], board[1][1], board[2][2]],
        [board[0][2], board[1][1], board[2][0]]
    ]

    wins = row_wins + col_wins + diag_wins

    for combination in wins:
        if all(x == "X" for x in combination):
            return "X wins"
        elif all(x == "O" for x in combination):
            return "O wins"

    return "Draw"