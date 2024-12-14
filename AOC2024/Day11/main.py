import functools
from collections import defaultdict

from timer import function_timer

blink_count = 25

# Read input file
# with open("Day11/sample", "r") as f:
with open("Day11/input", "r") as f:
    text = f.read()

stones_list = [int(i) for i in text.split(" ")]


@function_timer()
# @functools.cache
def naive(blink_count, stones_list):
    for _ in range(blink_count):
        operations = []
        for j in range(len(stones_list)):
            if stones_list[j] == 0:
                stones_list[j] = 1
            elif len(str(stones_list[j])) % 2 == 0:
                num_str = str(stones_list[j])
                length = len(num_str) // 2
                stones_list[j] = int(num_str[0:length])
                operations.append([int(num_str[length:]), j + len(operations) + 1])
            else:
                stones_list[j] *= 2024
        for operation in operations:
            stones_list.insert(operation[1], operation[0])
    return len(stones_list)

# print(naive(blink_count, stones_list))


@function_timer()
def optimised(blink_count, stones_list):
    stone_counter = defaultdict(int)
    for stone in stones_list:
        stone_counter[stone] += 1
    for _ in range(blink_count):
        next_stone_counter = defaultdict(int)
        for stone, count in stone_counter.items():
            if stone == 0:
                next_stone_counter[1] += count
            elif len(str(stone)) % 2 == 0:
                num_str = str(stone)
                length = len(num_str) // 2
                left = int(num_str[0:length])
                right = int(num_str[length:])
                next_stone_counter[left] += count
                next_stone_counter[right] += count
            else:
                next_stone_counter[stone * 2024] += count
        stone_counter = next_stone_counter
    return sum(stone_counter.values())

stones_list = [int(i) for i in text.split(" ")]

print(stones_list)
print(optimised(blink_count, stones_list))


