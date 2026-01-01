def dive(map, coordinates):

    x, y = coordinates
    dive_result = map[x][y]
    count_o = sum(row.count("O") for row in map)

    
    if dive_result == "-":
        return "Empty"
    
    if dive_result == "X":
        return "Found" if count_o > 0 else "Recovered"
    
    if dive_result == "O":
        return 'Found' if count_o > 1 else 'Recovered'