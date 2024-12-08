import re
from timer import benchmark_timer

with open("Day3/input", "r") as file:
    text = file.read()
pattern1 = r"mul\(\d{1,3},\d{1,3}\)"
pattern2 = r"mul\(\d{1,3},\d{1,3}\)|don't\(\)|do\(\)"

@benchmark_timer
def main():
    matches = re.finditer(pattern1, text)
    sum1 = 0
    for match in matches:
        nums = match.group()[4:-1]
        arr = nums.split(",")
        mul = int(arr[0]) * int(arr[1])
        sum1 += mul
    print("part1: " + str(sum1))
    matches = re.finditer(pattern2, text)
    sum2 = 0
    execute = True
    for match in matches:
        if match.group() == "do()":
            execute = True
        elif match.group() == "don't()":
            execute = False
        elif execute:
            nums = match.group()[4:-1]
            arr = nums.split(",")
            mul = int(arr[0]) * int(arr[1])
            sum2 += mul
    print("part2: " + str(sum2))

@benchmark_timer
def main2():
    matches = re.findall(pattern1, text)
    sum1 = 0
    for match in matches:
        nums = match[4:-1]
        arr = nums.split(",")
        mul = int(arr[0]) * int(arr[1])
        sum1 += mul
    print("part1: " + str(sum1))
    matches = re.findall(pattern2, text)
    sum2 = 0
    execute = True
    for match in matches:
        if match == "do()":
            execute = True
        elif match == "don't()":
            execute = False
        elif execute:
            nums = match[4:-1]
            arr = nums.split(",")
            mul = int(arr[0]) * int(arr[1])
            sum2 += mul
    print("part2: " + str(sum2))

main()
main2()