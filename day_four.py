paper_map = []
total = 0

with open('data\\day_four.txt') as file:
    for line in file:
        row = list(line.strip())
        row_len = len(row)
        row.insert(0, '.')
        row.append('.')
        paper_map.append(row)
    paper_map.insert(0, ['.'] * (row_len + 2))
    paper_map.append(['.'] * (row_len + 2))

keep_going = True
while keep_going:
    keep_going = False

    for r in range(1, len(paper_map) - 1):
        for c in range(1, len(paper_map[r]) - 1):
            count = 0
            if paper_map[r][c] != '@':
                continue
            # up left
            if paper_map[r - 1][c - 1] == '@':
                count += 1
            # up
            if paper_map[r - 1][c] == '@':
                count += 1
            # up right
            if paper_map[r - 1][c + 1] == '@':
                count += 1
            # left
            if paper_map[r][c - 1] == '@':
                count += 1
            # right
            if paper_map[r][c + 1] == '@':
                count += 1
            # dn left
            if paper_map[r + 1][c - 1] == '@':
                count += 1
            # dn
            if paper_map[r + 1][c] == '@':
                count += 1
            # dn right
            if paper_map[r + 1][c + 1] == '@':
                count += 1

            if count < 4:
                paper_map[r][c] = '.'
                keep_going = True
                total += 1

print(total)
