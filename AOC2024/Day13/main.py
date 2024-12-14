from sympy import symbols, Eq, solve

# with open("Day13/sample", "r") as f:
with open("Day13/input", "r") as f:
    lines = f.readlines()

eq_lists = []
eq_list = []
count = 0
for line in lines:
    text_line = line.strip()
    if text_line:
        contents = text_line.split(":")[1].split(", ")
    if count == 0 or count == 1:
        for content in contents:
            coeff = content.split("+")[1]
            eq_list.append(coeff)
        count += 1
    elif count == 2:
        for content in contents:
            ans = content.split("=")[1]
            eq_list.append(ans)
        count += 1
    elif count == 3:
        eq_lists.append(eq_list)
        eq_list = []
        count = 0
eq_lists.append(eq_list)

count1 = 0
for eq_list in eq_lists:
    x, y = symbols('x y')
    eq1 = Eq(int(eq_list[0]) * x + int(eq_list[2]) * y,  int(eq_list[4]))
    eq2 = Eq(int(eq_list[1]) * x + int(eq_list[3]) * y,  int(eq_list[5]))
    solution = solve((eq1, eq2), (x, y))
    three_tokens = solution[x]
    one_token = solution[y]
    if three_tokens % 1 == 0 and one_token % 1 == 0:
        count1 += (three_tokens * 3 + one_token * 1)
print(count1)

count2 = 0
for eq_list in eq_lists:
    x, y = symbols('x y')
    eq1 = Eq(int(eq_list[0]) * x + int(eq_list[2]) * y, 10000000000000 + int(eq_list[4]))
    eq2 = Eq(int(eq_list[1]) * x + int(eq_list[3]) * y, 10000000000000 + int(eq_list[5]))
    solution = solve((eq1, eq2), (x, y))
    three_tokens = solution[x]
    one_token = solution[y]
    if three_tokens % 1 == 0 and one_token % 1 == 0:
        count2 += (three_tokens * 3 + one_token * 1)
print(count2)