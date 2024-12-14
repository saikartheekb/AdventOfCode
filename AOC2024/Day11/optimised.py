from collections import Counter

with open("Day11/sample", "r") as f:
# with open("Day11/input", "r") as f:
    text = f.read()
stones_list = [int(i) for i in text.split(" ")]

def count_stones_after_blinks(initial_stones, blinks):
    stone_counts = Counter(initial_stones)

    for _ in range(blinks):
        next_counts = Counter()

        for stone, count in stone_counts.items():
            if stone == 0:
                next_counts[1] += count  # Rule 1
            elif len(str(stone)) % 2 == 0:  # Rule 2
                # Split the stone into two parts
                digits = str(stone)
                mid = len(digits) // 2
                left = int(digits[:mid])
                right = int(digits[mid:])
                next_counts[left] += count
                next_counts[right] += count
            else:
                next_counts[stone * 2024] += count  # Rule 3

        # Update the stone counts for the next blink
        stone_counts = next_counts

    # Return the total number of stones
    return sum(stone_counts.values())

initial_stones = stones_list
blinks = 5
result = count_stones_after_blinks(initial_stones, blinks)
print(f"Number of stones after {blinks} blinks: {result}")

