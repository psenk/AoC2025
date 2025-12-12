banks = []
total = 0

with open('data\\day_three.txt') as file:
    for line in file:
        bank = line.strip()
        bank_list = []
        for i in range(len(bank)):
            bank_list.append((i, int(bank[i])))
        banks.append(bank_list)

"""
PART ONE

for bank in banks:
    bank_size = len(bank)
    max_value = 0
    for i in range(bank_size):
        for j in range(i + 1, bank_size):
            num = (bank[i] * 10) + bank[j]
            if num > max_value:
                max_value = num
    total += max_value
"""

for battery_bank in banks:  # [(0, '9'), (1, '8'), (2, '7'), (3, '6'), (4, '5'), (5, '4'), (6, '3'), (7, '2'), (8, '1'), (9, '1'), (10, '1'), (11, '1'), (12, '1'), (13, '1'), (14, '1')]
    bank_size = len(battery_bank)
    value = ''
    lp = 0
    rp = bank_size - 11
    buffer = -1
    while rp <= bank_size:
        slice = battery_bank[lp:rp]
        max_battery = 0
        for ind, val in slice:
            if ind <= buffer:
                continue
            if val > max_battery:
                max_battery = val
                buffer = ind
        value += str(max_battery)
        lp += 1
        rp += 1

    print(f'Final value: {value}')
    total += int(value)
print(total)
