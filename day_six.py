total = 0
worksheet = []

with open('data\\day_six.txt') as file:
    for line in file:
        worksheet.append(line.strip('\n'))

""" 
PART ONE

mult = False
for col in range(len(worksheet[0])):
    value = 1
    if '*' in worksheet[len(worksheet) - 1][col]:
        mult = True
    else:
        mult = False
    for row in range(len(worksheet) - 1):
        if mult:
            value *= worksheet[row][col]
        else:
            value += worksheet[row][col]
    if not mult:
        value -= 1
    total += value

print(total)
"""

new_sheet = []
for col in range(len(worksheet[0])):
    num = ''
    for row in range(len(worksheet)):
        num += worksheet[row][col]
    if num.strip():
        new_sheet.append(num)

value = new_sheet[0]
final_sheet = []
math_problem = [value]
for i in range(1, len(new_sheet)):
    current_item = new_sheet[i]
    if '+' not in current_item and '*' not in current_item:
        math_problem.append(current_item)
    else:
        final_sheet.append(math_problem)
        value = new_sheet[i]
        math_problem = [value]
final_sheet.append(math_problem)

row, col = 0, 0
row_total = 1
mult = False
for row in range(len(final_sheet)):
    for col in range(len(final_sheet[row])):
        if col == 0:
            first = final_sheet[row][0]
            if '*' in first:
                final_sheet[row][0] = first.replace('*', '')
                mult = True
            else:
                final_sheet[row][0] = first.replace('+', '')
                mult = False
        if mult:
            row_total *= int(final_sheet[row][col])
        else:
            row_total += int(final_sheet[row][col])
    total += row_total if mult else row_total - 1
    row_total = 1

print(total)
