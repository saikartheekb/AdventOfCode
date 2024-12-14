import functools
from collections import defaultdict

from timer import function_timer

# 13069220

# Read input file
# with open("Day12/sample3", "r") as f:
with open("Day12/sample2", "r") as f:
# with open("Day12/sample", "r") as f:
# with open("Day12/input", "r") as f:
    lines = f.readlines()

farm_map = [list(line.strip()) for line in lines]


def check_perimeter(x, y, farm_map):
    count = []
    rows, cols = len(farm_map), len(farm_map[0])
    if x == 0 or farm_map[x - 1][y] != farm_map[x][y]:
        count += ["UP"]
    if x == rows - 1 or farm_map[x + 1][y] != farm_map[x][y]:
        count += ["DOWN"]
    if y == 0 or farm_map[x][y - 1] != farm_map[x][y]:
        count += ["LEFT"]
    if y == cols - 1 or farm_map[x][y + 1] != farm_map[x][y]:
        count += ["RIGHT"]
    return count


def get_cost_matrix(x, y, farm_map, visited):
    if (x, y) in visited or farm_map[x][y] == 0:
        return []
    # print(farm_map[x][y])
    visited.add((x, y))
    perimeter = check_perimeter(x, y, farm_map)
    curr_visit = [((x, y), perimeter)]
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(farm_map) and 0 <= ny < len(farm_map[0]) and farm_map[nx][ny] == farm_map[x][y]:
            curr_visit += get_cost_matrix(nx, ny, farm_map, visited)

    return curr_visit


def count_edges(cost_dict):
    convex_edges = 0
    concave_edges = 0
    if cost_dict:
        print(cost_dict)
    for cell_loc, edge_list in cost_dict.items():
        if len(edge_list) == 4:
            convex_edges += 4
        elif len(edge_list) == 3:
            convex_edges += 2
        elif (len(edge_list) == 2 and
              (("UP" in edge_list and "DOWN" in edge_list) or ("RIGHT" in edge_list and "LEFT" in edge_list))):
            convex_edges += 0
        else:
            x, y = cell_loc
            if len(edge_list) == 2:
                convex_edges += 1
                if "UP" in edge_list and "LEFT" in edge_list and (x + 1, y + 1) not in cost_dict:
                    concave_edges += 1
                elif "UP" in edge_list and "RIGHT" in edge_list and (x + 1, y - 1) not in cost_dict:
                    concave_edges += 1
                elif "DOWN" in edge_list and "LEFT" in edge_list and (x - 1, y + 1) not in cost_dict:
                    concave_edges += 1
                elif "DOWN" in edge_list and "RIGHT" in edge_list and (x - 1, y - 1) not in cost_dict:
                    concave_edges += 1
            elif len(edge_list) == 1:
                if "UP" in edge_list:
                    if (x - 1, y + 1) in cost_dict and (x + 1, y + 1) in cost_dict:
                        concave_edges += 2
                elif "DOWN" in edge_list:
                    if (x - 1, y - 1) in cost_dict and (x + 1, y - 1) in cost_dict:
                        concave_edges += 2
                elif "LEFT" in edge_list:
                    if (x - 1, y - 1) in cost_dict and (x - 1, y + 1) in cost_dict:
                        concave_edges += 2
                elif "RIGHT" in edge_list:
                    if (x + 1, y - 1) in cost_dict and (x + 1, y + 1) in cost_dict:
                        concave_edges += 2
            elif len(edge_list) == 0:
                if (x - 1, y + 1) in cost_dict:
                    concave_edges += 1
                if (x + 1, y + 1) in cost_dict:
                    concave_edges += 1
                if (x - 1, y - 1) in cost_dict:
                    concave_edges += 1
                if (x - 1, y + 1) in cost_dict:
                    concave_edges += 1

    total_edges = convex_edges + concave_edges
    # print(total_edges)
    return total_edges


total_cost1, total_cost2 = 0, 0
visited = set()

for i in range(len(farm_map[0])):
    for j in range(len(farm_map)):
        cost_matrix = get_cost_matrix(i, j, farm_map, visited)
        total_cost1 += len(cost_matrix) * sum([len(y) for x, y in cost_matrix])
        cost_dict = {k: val for k, val in cost_matrix}
        total_cost2 += len(cost_matrix) * count_edges(cost_dict)

print(total_cost1)
print(total_cost2)
