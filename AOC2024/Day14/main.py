SIMULATION_COUNT = 100

# Sample file configuration
# max_x = 11
# max_y = 7
# # with open("Day14/sample2", "r") as f:
# with open("Day14/sample", "r") as f:
#     lines = f.readlines()
max_x = 101
max_y = 103
# with open("Day14/sample2", "r") as f:
with open("Day14/input", "r") as f:
    lines = f.readlines()

# Parse input data
pv_list = []
for line in lines:
    content = line.strip().split(" ")
    position_text = content[0]
    velocity_text = content[1]
    position = tuple(map(int, position_text.split("=")[1].split(",")))
    velocity = tuple(map(int, velocity_text.split("=")[1].split(",")))
    pv_list.append((position, velocity))

# Initialize final positions list
final_positions = []

def print_map(position_list):
    # Corrected 2D matrix initialization
    position_map = [[" " for _ in range(max_x)] for _ in range(max_y)]

    for x, y in position_list:
        position_map[y][x] = 1

    for row in position_map:
        print(" ".join(map(str, row)))
    print("******************************************")

# Simulate movement function
def simulate_movement(pv):
    px, py = pv[0]
    vx, vy = pv[1]
    for _ in range(SIMULATION_COUNT):
        px = (px + vx + max_x) % max_x
        py = (py + vy + max_y) % max_y
    return px, py

# Simulate and store final positions
for pv in pv_list:
    x, y = simulate_movement(pv)
    final_positions.append((x, y))
print_map(final_positions)

# Print final positions
# print(final_positions)

# Quadrant counting
q1 = q2 = q3 = q4 = 0
mid_x = max_x // 2
mid_y = max_y // 2

for x, y in final_positions:
    if x == mid_x or y == mid_y:
        continue
    if 0 <= x < mid_x and 0 <= y < mid_y:
        q1 += 1
    elif mid_x < x < max_x and mid_y < y < max_y:
        q2 += 1
    elif mid_x < x < max_x and 0 <= y < mid_y:
        q3 += 1
    elif 0 <= x < mid_x and mid_y < y < max_y:
        q4 += 1

# Print quadrant counts and product
# print(q1, q2, q3, q4)
# print(q1 * q2 * q3 * q4)
