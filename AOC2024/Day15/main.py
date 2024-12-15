
# with open("Day15/sample2", "r") as f:
# with open("Day15/sample", "r") as f:
with open("Day15/input", "r") as f:
    lines = f.readlines()

def print_map(map):
    for row in map:
        for element in row:
            print(element, end="")
        print()
    print("****************************************")
    print()

warehouse_map = []
robot_movements = []
parse_second = False
for line in lines:
    if not parse_second:
        if line.strip() == "":
            parse_second = True
        else:
            warehouse_map.append(list(line.strip()))
    else:
        robot_movements += (list(line.strip()))

print_map(warehouse_map)
print(robot_movements)


def find_robot_position(warehouse_map):
    for i in range(len(warehouse_map)):
        for j in range(len(warehouse_map[0])):
            if warehouse_map[i][j] == "@":
                return (i, j)

robot_position = find_robot_position(warehouse_map)
print(robot_position)


def move_positions(warehouse_map, robot_position, direction):
    initial_position = robot_position
    moving_position_list = []
    while True:
        if warehouse_map[initial_position[0]][initial_position[1]] == ".":
            break
        if warehouse_map[initial_position[0]][initial_position[1]] == "#":
            moving_position_list = []
            break
        moving_position_list.append(initial_position)
        initial_position = (initial_position[0] + direction[0], initial_position[1] + direction[1])

    for position in moving_position_list[::-1]:
        temp = warehouse_map[position[0]][position[1]]
        warehouse_map[position[0]][position[1]] = warehouse_map[position[0] + direction[0]][position[1]+ direction[1]]
        warehouse_map[position[0] + direction[0]][position[1] + direction[1]] = temp

        # warehouse_map[position[0]][position[1]], warehouse_map[position[0] + direction[1]][position[1]+ direction[1]] = (
        #     warehouse_map[position[0] + direction[1]][position[1]+ direction[1]], warehouse_map[position[0]][position[1]]
        # )
        # print_map(warehouse_map)


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
    # print_map(warehouse_map)

print_map(warehouse_map)

gps_total = 0
for i in range(len(warehouse_map)):
    for j in range(len(warehouse_map[0])):
        if warehouse_map[i][j] == "O":
            gps_total += (100 * i) + j
print(gps_total)

