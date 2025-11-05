import sys

names = sys.argv[1].split(',')
instructions = sys.argv[2].split(',')
current_position = 0
for instruction in instructions:
    direction, *number = list(instruction)
    number = int(''.join(number))
    move = 0
    if direction == 'R':
        move += number
    else:
        move -= number

    temp_move = (current_position + move) % len(names)
    current_position = temp_move


print(names[current_position])
    


