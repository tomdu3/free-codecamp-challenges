def find_pawn_moves(position):
    col, row = position[0], int(position[1])
    if row == 2:
        return [f"{col}{row+1}", f"{col}{row+2}"]
    return [f"{col}{row+1}"]