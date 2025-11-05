import sys

names = sys.argv[1].split(',')
instructions = sys.argv[2].split(',')
current_position = 0
for instruction in instructions:
    direction, number = list(instruction)
    number = int(number)
    move = 0
    if direction == 'R':
        temp_move = current_position + number
        move = temp_move if temp_move < len(names) else len(names)
    elif direction == 'L':
        temp_move = current_position - number
        move = temp_move if temp_move >= 0 else 0
    current_position = move
    print(instruction, names[current_position])


print(names[current_position])
    

