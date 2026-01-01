import copy
def check_neighbors(grid, row, col):
    check_grid = [
        [-1, -1], [-1, 0], [-1, 1],
        [0, -1], [0, 1],
        [1, -1], [1, 0], [1, 1]
     ]
    neighbours = 0
    for r,c in check_grid:
        if row + r < 0 or row + r >= len(grid) or col + c < 0 or col + c >= len(grid[row]):
            continue
        neigbour = grid[row + r][col + c]
        neighbours += 0 if neigbour == 0 else 1
    return neighbours
def game_of_life(grid):
    new_grid = copy.deepcopy(grid)
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == 1:
                if check_neighbors(grid, row, col) < 2 or check_neighbors(grid, row, col) > 3:
                    new_grid[row][col] = 0
            else:
                if check_neighbors(grid, row, col) == 3:
                    new_grid[row][col] = 1

    return new_grid


if __name__ == "__main__":
    print(game_of_life([[0, 1, 0], [0, 0, 1], [1, 1, 1]]))
    print(game_of_life([[1, 1, 0, 0], [1, 0, 1, 0], [0, 1, 1, 1], [0, 0, 1, 0]]))
    print(game_of_life([[1, 0, 0], [0, 1, 0], [0, 0, 1]]))
    print(game_of_life([[0, 1, 1, 0], [1, 1, 0, 1], [0, 1, 1, 0], [0, 0, 1, 0]]))
