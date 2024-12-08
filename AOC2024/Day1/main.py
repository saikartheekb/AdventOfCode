filename = r"Day1/input"

list1 = []
list2 = []

# Read the file and process its lines
with open(filename, "r") as aocfile:
    lines = aocfile.readlines()
    for line in lines:
        line = line.strip()  # Remove leading and trailing whitespace
        if not line:  # Skip blank lines
            continue

        # Split on any whitespace (spaces, tabs, etc.)
        wordlist = line.split()
        if len(wordlist) >= 2:  # Ensure there are at least two parts
            try:
                list1.append(int(wordlist[0]))
                list2.append(int(wordlist[1]))
            except ValueError:
                print(f"Skipping line due to invalid integer: {line}")
        else:
            print(f"Skipping line due to insufficient data: {line}")

# Check if lists have values
if not list1 or not list2:
    print("Error: No valid data found in the file.")
else:
    # Sort the lists
    list1.sort()
    list2.sort()

    # Calculate the sum of absolute differences
    total_sum = 0  # Rename 'sum' to avoid conflict with the built-in `sum` function

    for i in range(len(list1)):
        similar_count = list2.count(list1[i])
        total_sum += similar_count * list1[i]

    print(total_sum)
