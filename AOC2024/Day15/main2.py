# with open("Day15/sample4", "r") as f:
# with open("Day15/sample3", "r") as f:
# with open("Day15/sample2", "r") as f:
with open("G:\\IdeaProjects\\AOC\\AOC2024\\Day15\\sample", "r") as f:
# with open("Day15/input", "r") as f:
    lines = f.readlines()

def print_map(map):
    for row in map:
        for element in row:
            print(element, end="")
        print()
    print()

warehouse_map = []
robot_movements = []
parse_second = False
# for line in lines:
#     if not parse_second:
#         if line.strip() == "":
#             parse_second = True
#         else:
#             warehouse_map.append(list(line.strip()))
#     else:
#         robot_movements += (list(line.strip()))
for line in lines:
    if not parse_second:
        if line.strip() == "":
            parse_second = True
        else:
            warehouse_map_list = []
            for letter in line.strip():
                if letter == ".":
                    warehouse_map_list += [".","."]
                elif letter == "#":
                    warehouse_map_list += ["#","#"]
                elif letter == "@":
                    warehouse_map_list += ["@","."]
                elif letter == "O":
                    warehouse_map_list += ["[","]"]
            warehouse_map.append(warehouse_map_list)
    else:
        robot_movements += (list(line.strip()))

# print_map(warehouse_map)
# print(robot_movements)


def find_robot_position(warehouse_map):
    for i in range(len(warehouse_map)):
        for j in range(len(warehouse_map[0])):
            if warehouse_map[i][j] == "@":
                return (i, j)

robot_position = find_robot_position(warehouse_map)
# print(robot_position)


def move_positions(warehouse_map, robot_position, direction):
    if direction in [(0, 1), (0, -1)]:
        initial_position = robot_position
        moveable_position_list = []
        while True:
            if warehouse_map[initial_position[0]][initial_position[1]] == ".":
                break
            if warehouse_map[initial_position[0]][initial_position[1]] == "#":
                moveable_position_list = []
                break
            moveable_position_list.append(initial_position)
            initial_position = (initial_position[0] + direction[0], initial_position[1] + direction[1])
    else:
        initial_positions = [robot_position]
        moveable_position_list = []
        while True:
            curr_moveable_position_list = []
            if all(warehouse_map[initial_position[0]][initial_position[1]] == "." for initial_position in initial_positions):
                break
            if any(warehouse_map[initial_position[0]][initial_position[1]] == "#" for initial_position in initial_positions):
                moveable_position_list = []
                break
            for initial_position in initial_positions:
                if warehouse_map[initial_position[0]][initial_position[1]] == "[" and (initial_position[0], initial_position[1] + 1) not in initial_positions:
                    curr_moveable_position_list.append(initial_position)
                    curr_moveable_position_list.append((initial_position[0], initial_position[1] + 1))
                elif warehouse_map[initial_position[0]][initial_position[1]] == "]" and (initial_position[0], initial_position[1] - 1) not in initial_positions:
                    curr_moveable_position_list.append(initial_position)
                    curr_moveable_position_list.append((initial_position[0], initial_position[1] - 1))
                elif warehouse_map[initial_position[0]][initial_position[1]] == ".":
                    continue
                else:
                    curr_moveable_position_list.append(initial_position)
            initial_positions = [(position[0] + direction[0], position[1] + direction[1]) for position in curr_moveable_position_list]
            moveable_position_list += curr_moveable_position_list

    for position in moveable_position_list[::-1]:
        temp = warehouse_map[position[0]][position[1]]
        warehouse_map[position[0]][position[1]] = warehouse_map[position[0] + direction[0]][position[1] + direction[1]]
        warehouse_map[position[0] + direction[0]][position[1] + direction[1]] = temp



def find_next_position(warehouse_map, robot_position, robot_movement):
    if robot_movement == "<":
        move_positions(warehouse_map, robot_position, (0, -1))
    elif robot_movement == ">":
        move_positions(warehouse_map, robot_position, (0, 1))
    elif robot_movement == "^":
        move_positions(warehouse_map, robot_position, (-1, 0))
    elif robot_movement == "v":
        move_positions(warehouse_map, robot_position, (1, 0))

for movement in robot_movements:
    find_next_position(warehouse_map, robot_position, movement)
    robot_position = find_robot_position(warehouse_map)
    # print(movement)
    print_map(warehouse_map)

# print_map(warehouse_map)

gps_total = 0
for i in range(len(warehouse_map)):
    for j in range(len(warehouse_map[0])):
        if warehouse_map[i][j] == "[":
            gps_total += (100 * i) + j
print(gps_total)

