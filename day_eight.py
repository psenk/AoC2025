import math

junction_boxes = []
distances: dict[tuple, list] = {}
CONNECTIONS = 10


"""
Used AI help.
- distance is also the WEIGHT of an edge
1. get input
2. generate all possible edges
3. sort edges by distance, shortest connections to longest
4. union-find setup (making parent/rank dicts)
- every junction box is its own circuit (parent[x] = x)
- components tracks how many circuits exist
5. find which circuit a box belongs to
6. connect two circuits
7. kruskals algorithm loop - find the cheapest (shortest) way to connect everything without cycles
"""

# read input


with open('data\\day_eight.txt') as file:
    for line in file:
        clean_line = tuple(map(int, line.strip().split(',')))
        junction_boxes.append(clean_line)

# distance between points function (euclidean)


def distance(point1, point2):
    x1, y1, z1 = (point1)
    x2, y2, z2 = (point2)
    x = (x2 - x1) ** 2
    y = (y2 - y1) ** 2
    z = (z2 - z1) ** 2
    return math.sqrt(x + y + z)


"""
# making list of all points connected to all other points
for i in range(len(junction_boxes)):
    for j in range(len(junction_boxes)):
        point1 = junction_boxes[i]
        point2 = junction_boxes[j]
        if i == j:
            continue
        if junction_boxes[i] not in distances.keys():
            distances[junction_boxes[i]] = [(
                junction_boxes[j], distance(point1, point2))]
        else:
            distances[junction_boxes[i]].append(
                (junction_boxes[j], distance(point1, point2)))
# print(f'All Junction Boxes: {junction_boxes}\n, LENGTH: {len(junction_boxes)}')
# print(f'All Point Distances: {distances}\n')

 # list of all point distances (start point, end point, distance)
smallest_distances = []
for start, points in distances.items():
    point_distances = distances[start]
    for dist in point_distances:
        point, distance = dist
        smallest_distances.append((start, point, distance))
smallest_distances_sorted = sorted(smallest_distances, key=lambda t: t[2])
smallest_distances = smallest_distances_sorted[::2]
# print(f'Cleaned point distances: {smallest_distances}, LENGTH: {len(smallest_distances)}\n')


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

total = 1
for i in range(3):
    total *= len(circuits[i])

print(total)
"""

# build all possible edges


edges = []
n = len(junction_boxes)

for i in range(n):
    for j in range(i + 1, n):
        a = junction_boxes[i]
        b = junction_boxes[j]
        edges.append((distance(a, b), a, b))

# sort by distance
edges.sort(key=lambda x: x[0])

# union find #4


parent = {p: p for p in junction_boxes}
rank = {p: 0 for p in junction_boxes}
components = n

# walk "up" tree to find root of circuit


def find(x):  # 5
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

# connect two circuits


def union(a, b):  # 6
    global components
    root_a = find(a)
    root_b = find(b)

    # if boxes in same circuit do nothing
    if root_a == root_b:
        return False

    # connect smaller trees to larger ones
    if rank[root_a] < rank[root_b]:
        parent[root_a] = root_b
    elif rank[root_a] > rank[root_b]:
        parent[root_b] = root_a
    else:
        parent[root_b] = root_a
        rank[root_a] += 1

    # circuits combined
    components -= 1
    return True

# kruskals algorithm #7


last_edge = None
# try edges from shortest to longest
for dist, a, b in edges:
    # if succeed, circuits were connected
    if union(a, b):
        # save as last edge
        last_edge = (a, b)
        # stop at last possible edge
        if components == 1:
            break

# final answer


x1 = last_edge[0][0]
x2 = last_edge[1][0]

print(f'Last connected edge: {last_edge}')
print(f'Answer: {x1 * x2}')
