import sys

names = sys.argv[1].split(",")
instructions = sys.argv[2].split(",")
current_position = 0
for instruction in instructions:
    direction, *number = list(instruction)
    number = int("".join(number))
    move = 0
    if direction == "R":
        move += number
    else:
        move -= number

    temp_move = (current_position + move) % len(names)
    names[current_position], names[temp_move] = (
        names[temp_move],
        names[current_position],
    )


print(names[current_position])
