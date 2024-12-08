from itertools import product

# Read input file
with open("Day7/sample", "r") as f:
# with open("Day7/input", "r") as f:
    lines = f.readlines()

count = 0
operators = ["+", "*", "||"]


def is_valid_eq(ans, operands):
    # Generate all operator combinations
    all_combinations = product(operators, repeat=len(operands) - 1)

    for combination in all_combinations:
        res = int(operands[0])
        print(res, end="")

        for i in range(len(combination)):
            if combination[i] == "+":
                print(" + " + operands[i + 1], end="")
                res += int(operands[i + 1])
            elif combination[i] == "*":
                print(" * " + operands[i + 1], end="")
                res *= int(operands[i + 1])
            elif combination[i] == "||":
                print(" || " + operands[i + 1], end="")
                res = int(str(res) + str(operands[i + 1]))

        print(" = " + str(res))

        if ans == res:
            print("MATCHED!!!!")
            return True

    return False


# Process each line from the input
for line in lines:
    eq = line.strip().split(":")
    ans = int(eq[0])
    operands = eq[1].strip().split(" ")

    if is_valid_eq(ans, operands):
        count += ans

print(count)
