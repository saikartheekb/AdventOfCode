import copy
from collections import defaultdict

# Read input file
# with open("Day10/sample2", "r") as f:
with open("Day10/sample", "r") as f:
# with open("Day10/input", "r") as f:
    lines = f.readlines()

trail_map = [list(map(int,line.strip())) for line in lines]

for row in trail_map:
    print(row)

trail_heads = [(x,y) for x in range(len(trail_map)) for y in range(len(trail_map[x])) if trail_map[x][y] == 0]


def is_eligible(x, y, curr_height, trail_map):
    if 0 <= x < len(trail_map) and 0 <= y < len(trail_map[0]) \
            and trail_map[x][y] - curr_height == 1:
        return True
    return False

#### PART1 #####
def calculate_trail_count(x, y, trail_map, visited):
    if trail_map[x][y] == 9:
        if (x,y) in visited:
            return 0
        visited.add((x,y))
        return 1

    count = 0
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if is_eligible(nx, ny, trail_map[x][y], trail_map):
            count += calculate_trail_count(nx, ny, trail_map, visited)
    if trail_map[x][y] == 0:
        print(x, y, count)
    return count

total_count = 0
for trail_head in trail_heads:
    visited = set()
    total_count += calculate_trail_count(trail_head[0], trail_head[1], trail_map, visited)

print(total_count)

#### PART2 #####
def calculate_trail_count2(x, y, trail_map):
    if trail_map[x][y] == 9:
        return 1

    count = 0
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if is_eligible(nx, ny, trail_map[x][y], trail_map):
            count += calculate_trail_count2(nx, ny, trail_map)
    if trail_map[x][y] == 0:
        print(x, y, count)
    return count

total_count2 = 0
for trail_head in trail_heads:
    total_count2 += calculate_trail_count2(trail_head[0], trail_head[1], trail_map)

print(total_count2)