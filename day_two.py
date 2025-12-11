ranges = []
# getting input
with open('data\\day_two.txt') as file:
    for line in file:
        ranges = line.strip().split(',')

new_ranges = []
# sanitizing data
for input_range in ranges:
    item = input_range.split('-')
    new_ranges.append((int(item[0]), int(item[1])))

"""
PART ONE

total_ids = 0
# solve problem
for start, end in new_ranges:
    # 11 - 22
    for id in range(start, end + 1):
        value = str(id)
        if len(value) % 2 != 0:
            continue
        l = 0
        r = len(value) // 2
        while r < len(value):
            if value[l] != value[r]:
                break
            else:
                if r == len(value) - 1:
                    total_ids += id
                    break
                l += 1
                r += 1

print(total_ids)
"""


"""
AI help on this one
is_invalid function:
1. get the ID as a string
2. consider all possible block sizes
   - from 1 to half of the ID size
   - pattern sequences larger than half the size are not possible e.g 11885611885 -> [118856]11885
3. skip block sizes that are not divisible by full ID len
   - 4 pattern block cannot repeat in a 5 length ID
4. extract the block as splice e.g 123123123 -> val[0:3]
5. reconstruct ID using block e.g 123 * 3 = 123123123
6. compare reconstructed ID to original
"""
 
total_ids = 0
bad_ids = set()


def is_invalid(value):
    value_len = len(value)  # 1
    for i in range(1, value_len // 2 + 1):  # 2
        if value_len % i != 0:  # 3
            continue
        block = value[:i]  # 4
        if block * (value_len // i) == value:  # 5, 6
            return True
    return False


# solve problem
for start, end in new_ranges:
    for id in range(start, end + 1):
        value = str(id)

        if is_invalid(value):
            total_ids += id
            bad_ids.add(value)
            print(f'Invalid ID: {value}')

print(total_ids)
