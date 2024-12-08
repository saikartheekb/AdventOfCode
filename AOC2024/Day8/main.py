from collections import defaultdict

# Read input file
# with open("Day8/sample2", "r") as f:
# with open("Day8/sample", "r") as f:
with open("Day8/input", "r") as f:
    lines = f.readlines()

for line in lines:
    map = [list(line.strip()) for line in lines]

def print_map(map):
    for row in map:
        for element in row:
            print(element, end=" ")
        print()
    print("****************************************")
    print()
antenna_locations_list = []
antenna_locations_set = defaultdict(list)
for i in range(len(map)):
    for j in range(len(map[0])):
        if map[i][j] != ".":
            antenna_locations_set[map[i][j]].append((i, j))
            antenna_locations_list.append((i, j))
print_map(map)

eligible_anti_node_locations_part1 = set()
eligible_anti_node_locations_part2 = set()

def is_eligible(anti_node_location):
    if anti_node_location[0] < 0 or anti_node_location[1] < 0:
        return False
    if anti_node_location[0] >= len(map) or anti_node_location[1] >= len(map[0]):
        return False
    return True

for frequency in antenna_locations_set:
    antenna = antenna_locations_set[frequency]
    for i in range(len(antenna) - 1):
        for j in range(i + 1, len(antenna)):
            x = antenna[i][0] - antenna[j][0]
            y = antenna[i][1] - antenna[j][1]

            ### PART1 #####
            anti_node_location_1 = (antenna[i][0] + x, antenna[i][1] + y)
            anti_node_location_2 = (antenna[j][0] - x, antenna[j][1] - y)
            if is_eligible(anti_node_location_1):
                eligible_anti_node_locations_part1.add(anti_node_location_1)
            if is_eligible(anti_node_location_2):
                eligible_anti_node_locations_part1.add(anti_node_location_2)

### PART2 ###
eligible_anti_node_locations_part2 = set(antenna_locations_list)
for frequency in antenna_locations_set:
    antenna = antenna_locations_set[frequency]
    for i in range(len(antenna) - 1):
        for j in range(i + 1, len(antenna)):
            x = antenna[i][0] - antenna[j][0]
            y = antenna[i][1] - antenna[j][1]

            antenna1 = (antenna[i][0], antenna[i][1])
            while(True):
                anti_node_location_1 = (antenna1[0] + x, antenna1[1] + y)
                if is_eligible(anti_node_location_1):
                    eligible_anti_node_locations_part2.add(anti_node_location_1)
                else:
                    break
                antenna1 = anti_node_location_1

            antenna2 = (antenna[j][0], antenna[j][1])
            while(True):
                anti_node_location_2 = (antenna2[0] - x, antenna2[1] - y)
                if is_eligible(anti_node_location_2):
                    eligible_anti_node_locations_part2.add(anti_node_location_2)
                else:
                    break
                antenna2 = anti_node_location_2

print(len(eligible_anti_node_locations_part1))
print(len(eligible_anti_node_locations_part2))

for location in eligible_anti_node_locations_part2:
    if map[location[0]][location[1]] == ".":
        map[location[0]][location[1]] = "#"
print_map(map)




