import copy
from collections import defaultdict

# Read input file
# with open("Day9/sample2", "r") as f:
# with open("Day9/sample", "r") as f:
# with open("Day9/input", "r") as f:
with open("Day9/input2", "r") as f:
    text = f.read().strip()

file_id = 0
disk_map = []

for i in range(0, len(text), 2):
    for j in range(int(text[i])):
        disk_map.append(file_id)
    if i < len(text) - 1:
        for j in range(int(text[i + 1])):
            disk_map.append("")
    file_id += 1

# print(disk_map)
disk_map2 = copy.deepcopy(disk_map)
disk_map3 = copy.deepcopy(disk_map)

###### PART1 ######
i = 0
j = len(disk_map) - 1
while i < len(disk_map) and j >= 0:
    while disk_map[i] != "":
        i += 1
    while disk_map[j] == "":
        j -= 1
    if i < j:
        disk_map[i], disk_map[j] = disk_map[j], disk_map[i]
    i += 1
    j -= 1

# print(disk_map)

counter = 0

for i in range(len(disk_map)):
    if disk_map[i] != "":
        counter += disk_map[i] * i
    else:
        break
print(disk_map)
print(counter)

### PART2 ###

file_id = disk_map2[len(disk_map2) - 1]

while file_id >= 0:
    # Find the file's starting and ending indices
    try:
        file_start_idx = next(i for i, x in enumerate(disk_map2) if x == file_id)
        file_end_idx = len(disk_map2) - 1 - next(i for i, x in enumerate(reversed(disk_map2)) if x == file_id)
        file_length = file_end_idx - file_start_idx + 1

        # Look for the leftmost free space only to the left of the file
        leftmost_free_start = -1
        max_free_length = 0

        i = 0
        while i < file_start_idx:
            # Find next free block
            if disk_map2[i] == "":
                start = i
                while i < file_start_idx and disk_map2[i] == "":
                    i += 1
                free_length = i - start

                if free_length >= file_length:
                    leftmost_free_start = start
                    max_free_length = free_length
                    break  # Found the best fit
            i += 1

        # If a valid space found, move the file
        if leftmost_free_start != -1:
            for j in range(file_length):
                disk_map2[leftmost_free_start + j] = file_id
                disk_map2[file_start_idx + j] = ""

    except StopIteration:
        pass  # Skip files that don't exist

    file_id -= 1

# Calculate checksum
checksum = sum(idx * file_id for idx, file_id in enumerate(disk_map2) if file_id != "")
print(checksum)

### PART2 Alternative ###

file_id = disk_map3[len(disk_map3) - 1]
print(file_id)
print(disk_map3)
def find_space_location_details(disk_map3):
    spaces = []
    i = 0
    while i < len(disk_map3):
        x = -1
        y = -1
        if disk_map3[i] == "":
            x = i
            while i < len(disk_map3) and disk_map3[i] == "":
                i += 1
            y = i - 1
        if x != -1:
            spaces.append((x, y))
        else:
            i += 1
    # print(spaces)
    return spaces


def find_file_id_loc_details(file_id, disk_map3):
    i = len(disk_map3)-1
    x = -1
    y = -1
    while i >= 0:
        if disk_map3[i] == file_id:
            y = i
            while i < len(disk_map3) and disk_map3[i] == file_id:
                i -= 1
            x = i+1
            break
        i -= 1
    return [x,y]

def swap(location1, location2, disk_map3, space_location_details):
    i, j = location1[0], location1[1]
    x, y = location2[0], location2[1]
    # print(disk_map3)
    while x <= y:
        # print(f"moving from {x} to {i}" )
        disk_map3[x], disk_map3[i] = disk_map3[i], disk_map3[x]
        x += 1
        i += 1
        # print(disk_map3)



# space_location_details = find_space_location_details(disk_map3)
while file_id > 0:
    space_location_details = find_space_location_details(disk_map3)
    file_id_loc_detail = find_file_id_loc_details(file_id, disk_map3)
    for space_location_detail in space_location_details:
        if space_location_detail[1] - space_location_detail[0] >= file_id_loc_detail[1] - file_id_loc_detail[0]\
                and space_location_detail[1] < file_id_loc_detail[1]:
            swap(space_location_detail, file_id_loc_detail, disk_map3, space_location_details)
            break
    file_id -= 1

# Calculate checksum
checksum3 = sum(idx * file_id for idx, file_id in enumerate(disk_map3) if file_id != "")
print(checksum3)
