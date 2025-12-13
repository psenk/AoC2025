ing_ranges = []
ing_ids = []
total = 0

with open('data\\day_five.txt') as file:

    for line in file:
        item = line.strip()
        if not item:
            continue
        if '-' in item:
            item_list = [int(x) for x in item.split('-')]
            ing_ranges.append(item_list)
        else:
            ing_ids.append(int(item))

"""
PART ONE

for id in ing_ids:
    for range in ing_ranges:
        low = range[0]
        hi = range[1]
        if low <= id <= hi:
            total += 1
            break
 """

"""
Used AI help for pt 2
Step one, merge the ranges together
Step two, add the final range lengths
1. Sort the ranges
2. Initialize active range as the first range
3. Loop through remaining ranges
4. Check for overlap (is the start value less than the current end?)
5. If no, add current range to final list, save new current range
6. If yes, merge ranges (current end changes to new end)
7. Add final range to list
"""

ing_ranges.sort()  # 1
merged_ranges = []
curr_start, curr_end = ing_ranges[0][0], ing_ranges[0][1]  # 2

for i in range(1, len(ing_ranges)):  # 3
    start = ing_ranges[i][0]
    end = ing_ranges[i][1]
    if start <= curr_end + 1:  # 4
        curr_end = max(curr_end, end)  # 6
    else:  # 5
        merged_ranges.append([curr_start, curr_end])
        curr_start, curr_end = start, end

merged_ranges.append([curr_start, curr_end])  # 7

for i in range(len(merged_ranges)):
    total += (merged_ranges[i][1] - merged_ranges[i][0])

print(total + len(merged_ranges))
