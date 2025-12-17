import math

junction_boxes = []
distances: dict[tuple, list] = {}
CONNECTIONS = 10

with open('data\\test.txt') as file:
    for line in file:
        clean_line = tuple(map(int, line.strip().split(',')))
        junction_boxes.append(clean_line)


def calc(point1, point2):
    x1, y1, z1 = (point1)
    x2, y2, z2 = (point2)
    x = (x2 - x1) ** 2
    y = (y2 - y1) ** 2
    z = (z2 - z1) ** 2
    return math.sqrt(x + y + z)

# making list of all points connected to all other points


for i in range(len(junction_boxes)):
    for j in range(len(junction_boxes)):
        point1 = junction_boxes[i]
        point2 = junction_boxes[j]
        if i == j:
            continue
        if junction_boxes[i] not in distances.keys():
            distances[junction_boxes[i]] = [(
                junction_boxes[j], calc(point1, point2))]
        else:
            distances[junction_boxes[i]].append(
                (junction_boxes[j], calc(point1, point2)))
print(f'All Junction Boxes: {junction_boxes}\n, LENGTH: {len(junction_boxes)}')
print(f'All Point Distances: {distances}\n')

# list of all point distances (start point, end point, distance)
smallest_distances = []
for start, points in distances.items():
    point_distances = distances[start]
    for dist in point_distances:
        point, distance = dist
        smallest_distances.append((start, point, distance))
smallest_distances_sorted = sorted(smallest_distances, key=lambda t: t[2])
smallest_distances = smallest_distances_sorted[::2]
print(
    f'Cleaned point distances: {smallest_distances}, LENGTH: {len(smallest_distances)}\n')

circuits = [[smallest_distances[0][0], smallest_distances[0][1]]]
for item in smallest_distances:
    start, end, dist = item
    # print(f'Starting point: {start}, Ending point: {end}, distance: {dist}')

    for c in range(len(circuits)):
        if start in circuits[c] and end in circuits[c]:
            break
        elif start in circuits[c] and end not in circuits[c]:
            circuits[c].append(end)
            break
        elif end in circuits[c] and start not in circuits[c]:
            circuits[c].append(start)
            break
        if c == len(circuits) - 1:
            new_circuit = [start, end]
            circuits.append(new_circuit)
            break

merge = True
while merge:
    merge = False
    for c in range(len(circuits)):
        if c + 1 > len(circuits):
            break
        for p in range(len(circuits[c])):
            for c2 in range(c, len(circuits) - 2):
                if c == c2:
                    continue
                if circuits[c][p] in circuits[c2]:
                    merge = True
                    circuits[c] = list(set(circuits[c]) | set(circuits[c2]))
                    circuits.pop(c2)
# circuits = sorted(circuits, key=len, reverse=True)
print(circuits)

""" total = 1
for i in range(3):
    total *= len(circuits[i])

print(total) """
