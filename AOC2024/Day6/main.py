import copy
from collections import defaultdict


def map_factory():
    with open("Day6/input", "r") as file:
    # with open("Day6/sample", "r") as file:
        lines = file.readlines()
    map = [list(line.strip()) for line in lines]
    return map

def turn_direction(map, x, y, direction):
    if direction == "^":
        map[x][y] = ">"
    elif direction == ">":
        map[x][y] = "v"
    elif direction == "v":
        map[x][y] = "<"
    else:
        map[x][y] = "^"
    return map[x][y]

def find_guard_idx(map):
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] in {"^", ">", "v", "<"}:
                return i, j, map[i][j]

x, y, direction = find_guard_idx(map_factory())

# def print_map(map):
#     for row in map:
#         for element in row:
#             print(element, end=" ")
#         print()
#     print("****************************************")
#     print()

# def print_map(map_data):
#     map_queue.put(map_data)

def is_valid_obstacle(px, py, x3, y3, curr_direction):
    if curr_direction == "^":
        for i in range(x3 - 1, px - 1, -1):
            if map[i][y3] == "#":
                return False
    elif curr_direction == ">":
        for j in range(y3 + 1, py + 1):
            if map[x3][j] == "#":
                return False
    elif curr_direction == "v":
        for i in range(x3 + 1, px + 1):
            if map[i][y3] == "#":
                return False
    elif curr_direction == "<":
        for j in range(y3 - 1, py - 1, -1):
            if map[x3][j] == "#":
                return False
    return True

def check_loop(map, x, y, direction):
    sim_map = copy.deepcopy(map)
    visited_positions = set()
    while True:
        state = (x, y, direction)
        if state in visited_positions:
            return True  # Loop detected
        visited_positions.add(state)
        # Check for boundary conditions
        if (x == len(sim_map) - 1 and direction == "v") or (y == len(sim_map[0]) - 1 and direction == ">") \
                or (x == 0 and direction == "^") or (y == 0 and direction == "<"):
            break
        if direction == "v":
            if sim_map[x + 1][y] in {".", "X"}:  # Open path or already visited
                sim_map[x][y] = "X"
                x += 1
            else:
                direction = turn_direction(sim_map, x, y, direction)
        elif direction == ">":
            if sim_map[x][y + 1] in {".", "X"}:
                sim_map[x][y] = "X"
                y += 1
            else:
                direction = turn_direction(sim_map, x, y, direction)
        elif direction == "^":
            if sim_map[x - 1][y] in {".", "X"}:
                sim_map[x][y] = "X"
                x -= 1
            else:
                direction = turn_direction(sim_map, x, y, direction)
        elif direction == "<":
            if sim_map[x][y - 1] in {".", "X"}:
                sim_map[x][y] = "X"
                y -= 1
            else:
                direction = turn_direction(sim_map, x, y, direction)
    return False  # No loop detected

obstacle_positions = []
def simulate_guard_movement(map, x, y, direction):
    while True:
        # Check for boundary conditions
        if (x == len(map) - 1 and direction == "v") or (y == len(map[0]) - 1 and direction == ">") \
                or (x == 0 and direction == "^") or (y == 0 and direction == "<"):
            map[x][y] = "X"
            break

        if direction == "v":
            if map[x + 1][y] in {".", "X"}:  # Open path or already visited
                map[x][y] = "X"
                x += 1
                map[x][y] = "v"
            else:
                direction = turn_direction(map, x, y, direction)
                obstacle_positions.append((x + 1, y, direction))
        elif direction == ">":
            if map[x][y + 1] in {".", "X"}:
                map[x][y] = "X"
                y += 1
                map[x][y] = ">"
            else:
                direction = turn_direction(map, x, y, direction)
                obstacle_positions.append((x, y + 1, direction))
        elif direction == "^":
            if map[x - 1][y] in {".", "X"}:
                map[x][y] = "X"
                x -= 1
                map[x][y] = "^"
            else:
                direction = turn_direction(map, x, y, direction)
                obstacle_positions.append((x - 1, y, direction))
        elif direction == "<":
            if map[x][y - 1] in {".", "X"}:
                map[x][y] = "X"
                y -= 1
                map[x][y] = "<"
            else:
                direction = turn_direction(map, x, y, direction)
                obstacle_positions.append((x, y - 1, direction))
    return map

final_map = simulate_guard_movement(map_factory(), x, y , direction)
# print_map(final_map)
print(sum(row.count("X") for row in final_map))

############### SECOND PART ###################
path_positions = []
for i in range(len(final_map)):
    for j in range(len(final_map[0])):
        if final_map[i][j] in {"X"}:
            path_positions.append((i, j))
# print(path_positions)

x, y, direction = find_guard_idx(map_factory())
# print(path_positions)
path_positions.remove((x,y))


def is_there_a_loop(map, x, y, direction):
    visited_dict = defaultdict(list)
    # print(visited_dict)
    while True:
        if direction in visited_dict[(x, y)]:
            return True
        visited_dict[(x, y)].append(direction)
        # print(visited_dict[(x, y)])
        # Check for boundary conditions
        if (x == len(map) - 1 and direction == "v") or (y == len(map[0]) - 1 and direction == ">") \
                or (x == 0 and direction == "^") or (y == 0 and direction == "<"):
            # print_map(map)
            # print(visited_dict)
            return False

        if direction == "v":
            if map[x + 1][y] in {".", "X"}:  # Open path or already visited
                map[x][y] = "X"
                x += 1
                map[x][y] = "v"
            else:
                direction = turn_direction(map, x, y, direction)
                obstacle_positions.append((x + 1, y, direction))
        elif direction == ">":
            if map[x][y + 1] in {".", "X"}:
                map[x][y] = "X"
                y += 1
                map[x][y] = ">"
            else:
                direction = turn_direction(map, x, y, direction)
                obstacle_positions.append((x, y + 1, direction))
        elif direction == "^":
            if map[x - 1][y] in {".", "X"}:
                map[x][y] = "X"
                x -= 1
                map[x][y] = "^"
            else:
                direction = turn_direction(map, x, y, direction)
                obstacle_positions.append((x - 1, y, direction))
        elif direction == "<":
            if map[x][y - 1] in {".", "X"}:
                map[x][y] = "X"
                y -= 1
                map[x][y] = "<"
            else:
                direction = turn_direction(map, x, y, direction)
                obstacle_positions.append((x, y - 1, direction))
        # print_map(map)
        # capture_map_state(map)
        # if check_loop(map, x, y, direction):
        #     possible_obstructions.add((x, y))
        #     capture_map_state(map)


counter = 0
for position in path_positions:
    temp_map = map_factory()
    temp_map[position[0]][position[1]] = "#"
    counter += 1 if is_there_a_loop(temp_map, x, y, direction) else 0

print(f"Number of possible looping obstructions: {counter}")
