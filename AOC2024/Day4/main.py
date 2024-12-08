import re

from timer.decorator.benchmark import benchmark_timer

pattern1 = r"XMAS"
pattern2 = r"SAMX"

with open("Day4/input", "r") as file:
    lines = file.readlines()

def get_diagonal_str_list(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    diagonals = []
    for d in range(rows + cols - 1):
        diagonal_tl_br = []
        diagonal_tr_bl = []
        for row in range(max(0, d - cols + 1), min(rows, d + 1)):
            col_tl_br = d - row
            col_tr_bl = cols - 1 - (d - row)
            diagonal_tl_br.append(matrix[row][col_tl_br])
            diagonal_tr_bl.append(matrix[row][col_tr_bl])
        diagonals.append(''.join(diagonal_tl_br))
        diagonals.append(''.join(diagonal_tr_bl))
    return diagonals

@benchmark_timer
def part1():
    horizontal_str_list = [line.strip() for line in lines]
    vertical_str_list = [''.join(row) for row in zip(*horizontal_str_list)]
    diagonal_str_list = get_diagonal_str_list(horizontal_str_list)
    all_strings = horizontal_str_list + vertical_str_list + diagonal_str_list
    pattern1_compiled = re.compile(pattern1)
    pattern2_compiled = re.compile(pattern2)
    count = 0
    for string in all_strings:
        count += len(pattern1_compiled.findall(string))
        count += len(pattern2_compiled.findall(string))
    print(f"part1: {count}")

@benchmark_timer
def part1_alt():
    matrix = [list(line.strip()) for line in lines]
    rows = len(matrix)
    cols = len(matrix[0])
    count = 0
    target_patterns = {('X', 'M', 'A', 'S'), ('S', 'A', 'M', 'X')}
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] in ("X", "S"):
                if j <= cols - 4:
                    horizontal_pattern = (matrix[i][j], matrix[i][j + 1], matrix[i][j + 2], matrix[i][j + 3])
                    if horizontal_pattern in target_patterns:
                        count += 1
                if i <= rows - 4:
                    vertical_pattern = (matrix[i][j], matrix[i + 1][j], matrix[i + 2][j], matrix[i + 3][j])
                    if vertical_pattern in target_patterns:
                        count += 1
                if i <= rows - 4 and j <= cols - 4:
                    diagonal_down_pattern = (matrix[i][j], matrix[i + 1][j + 1], matrix[i + 2][j + 2], matrix[i + 3][j + 3])
                    if diagonal_down_pattern in target_patterns:
                        count += 1
                if i >= 3 and j <= cols - 4:
                    diagonal_up_pattern = (matrix[i][j], matrix[i - 1][j + 1], matrix[i - 2][j + 2], matrix[i - 3][j + 3])
                    if diagonal_up_pattern in target_patterns:
                        count += 1
    print(f"part1_alt: {count}")


@benchmark_timer
def part2():
    count = 0
    mat = [list(line.strip()) for line in lines]

    def find_pattern_in_matrix(matrix, pattern):
        rows = len(matrix)
        cols = len(matrix[0])
        pattern_count = 0
        pattern_positions = [(0, 0), (0, 2), (1, 1), (2, 0), (2, 2)]

        for i in range(rows - 2):
            for j in range(cols - 2):
                match = True
                for x, y in pattern_positions:
                    if pattern[x][y] != '?' and matrix[i + x][j + y] != pattern[x][y]:
                        match = False
                        break
                if match:
                    pattern_count += 1

        return pattern_count

    patterns = [
        ['M', '?', 'S'],
        ['?', 'A', '?'],
        ['M', '?', 'S']
    ], [
        ['M', '?', 'M'],
        ['?', 'A', '?'],
        ['S', '?', 'S']
    ], [
        ['S', '?', 'S'],
        ['?', 'A', '?'],
        ['M', '?', 'M']
    ], [
        ['S', '?', 'M'],
        ['?', 'A', '?'],
        ['S', '?', 'M']
    ]
    for pattern in patterns:
        count += find_pattern_in_matrix(mat, pattern)
    print("part2: " + str(count))


@benchmark_timer
def part2_alt():
    mat = [list(line.strip()) for line in lines]

    def find_pattern_in_matrix(matrix):
        rows = len(matrix)
        cols = len(matrix[0])
        pattern_count = 0
        eligible_patterns = {
            ('M', 'M', 'S', 'S'),
            ('M', 'S', 'M', 'S'),
            ('S', 'M', 'S', 'M'),
            ('S', 'S', 'M', 'M')
        }
        for i in range(1, rows - 1):
            for j in range(1, cols - 1):
                if matrix[i][j] == 'A':
                    top_left = matrix[i - 1][j - 1]
                    top_right = matrix[i - 1][j + 1]
                    bottom_left = matrix[i + 1][j - 1]
                    bottom_right = matrix[i + 1][j + 1]
                    current_pattern = (top_left, top_right, bottom_left, bottom_right)
                    if current_pattern in eligible_patterns:
                        pattern_count += 1
        return pattern_count

    count = find_pattern_in_matrix(mat)
    print(f"part2_alt: {count}")

part1()
part1_alt()
part2()
part2_alt()
