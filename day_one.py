instructions = []
with open('data\\day_one.txt') as file:

    for line in file:
        ins = (line[0], int(line[1:].strip()))
        instructions.append(ins)

"""
STAR ONE

dial_point = 50
zero_count = 0

for rotation in instructions:
    if rotation[0] == 'L':
        dial_point -= rotation[1]
        if dial_point < 0:
            dial_point %= 100
    else:
        dial_point += rotation[1]
        if dial_point > 99:
            dial_point %= 100

    if dial_point == 0:
        zero_count += 1

print('Zero Count: ', zero_count)
 """

dial_point = 50
zero_count = 0

for direction, amount in instructions:

    while amount > 0:
        amount -= 1
        if dial_point == 0:
            zero_count += 1
        if direction == 'L':
            dial_point -= 1
            if dial_point < 0:
                dial_point = 99
        else:
            dial_point += 1
            if dial_point > 99:
                dial_point = 0

print('Zero Count: ', zero_count)
