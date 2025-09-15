def tribonacci_sequence(start_sequence, length):
    if length == 0:
        return []
    elif length <=3:
        return start_sequence[:length]
    new_sequence = start_sequence.copy()
    for i in range(length-3):
        new_sequence.append(sum([new_sequence[i], new_sequence[i+1], new_sequence[i+2]]))
    return new_sequence