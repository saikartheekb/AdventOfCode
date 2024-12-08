def is_safe(report):
    if len(report) < 2:
        return True
    trend = report[1] - report[0]
    if trend > 0:
        return all(1 <= report[i + 1] - report[i] <= 3 for i in range(len(report) - 1))
    elif trend < 0:
        return all(-3 <= report[i + 1] - report[i] <= -1 for i in range(len(report) - 1))
    else:
        return False


def is_safe_with_dampener(report):
    for i in range(len(report)):
        mod_report = report[:i] + report[i + 1:]
        if is_safe(mod_report):
            return True
    return False


def check_report1(report):
    if is_safe(report):
        return 1
    else:
        return 0


def check_report2(report):
    if is_safe(report) or is_safe_with_dampener(report):
        return 1
    else:
        return 0


with open("Day2/input", "r") as file:
    lines = file.readlines()

valid_reports1 = 0
valid_reports2 = 0
for line in lines:
    report = line.strip().split(" ")
    valid_reports1 += check_report1([int(i) for i in report])
    valid_reports2 += check_report2([int(i) for i in report])
print("part1: " + str(valid_reports1))
print("part2: " + str(valid_reports2))
