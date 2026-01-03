def find_left_handed_seats(table):
    available_seats = 0
    for r_idx, row in enumerate(table):
        for c_idx, seat in enumerate(row):
            if seat == "U":
                if r_idx % 2 == 0:
                    if c_idx < len(row) - 1:
                        if row[c_idx + 1] != "R":
                            available_seats += 1
                    else:
                        available_seats += 1
                else:
                    if c_idx > 0:
                        if row[c_idx - 1] != "R":
                            available_seats += 1
                    else:
                        available_seats += 1
    return available_seats


