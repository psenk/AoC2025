from functools import cache


total_splits = 0
diagram = []

with open('data\\day_seven.txt') as file:
    for line in file:
        diagram.append(line)

start_index = diagram[0].index('S')

"""
PART ONE

current_beams = set()
current_beams.add(start_index)

for row in range(2, len(diagram), 2):
    beams = set()
    for ind in current_beams:
        if diagram[row][ind] == '^':
            total_splits += 1
            beams.add(ind - 1)
            beams.add(ind + 1)
        else:
            beams.add(ind)
    current_beams = beams
"""

"""
Got help from YouTube video - https://www.youtube.com/watch?v=UiV7V1dTwZ8

Memoization - type of caching, stores results of function calls
so they can be returned quickly

functools module, cache function used
e.g
1. factorial(10) called, not cached
 - factorial(1) thru factorial(10) results now cached
3. factorial(5) called, result cached already so returned, no computation needed
"""

total = 0


@cache
def delve(row, col):
    if row >= len(diagram):
        return 1
    if diagram[row][col] == '.' or diagram[row][col] == 'S':
        return delve(row + 1, col)
    elif diagram[row][col] == '^':
        return delve(row, col - 1) + delve(row, col + 1)


print(delve(0, start_index))
