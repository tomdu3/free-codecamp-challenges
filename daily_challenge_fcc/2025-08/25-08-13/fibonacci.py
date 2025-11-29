def fibonacci_sequence(start_sequence, length):
    sequence = start_sequence[:]
    while len(sequence) < length:
        next_value = sequence[-1] + sequence[-2]
        sequence.append(next_value)
    return sequence[:length]