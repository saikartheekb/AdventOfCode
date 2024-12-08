from collections import defaultdict

from timer.decorator.benchmark import benchmark_timer

with open("Day5/input", "r") as file:
    input_data = file.readlines()

def parse_rules_updates(input_data):
    rules = []
    updates = []
    flip = True
    for line in input_data:
        if line.strip() == "":
            flip = False
            continue
        if flip:
            rules.append(line.strip().split("|"))
        else:
            updates.append(line.strip())
    return rules, updates

def create_update_graph(rules):
    update_dict = defaultdict(set)
    for x, y in rules:
        update_dict[x].add(y)
    return update_dict

def check_order(page, checked_pages, update_dict):
    if not checked_pages:
        return True
    for checked_page in checked_pages:
        if checked_page in update_dict.get(page):
            return False
    return True

def rectify_order(pages, update_order_graph):
    new_pages = []
    for page in pages:
        inserted = False
        for new_page in new_pages:
            if new_page in update_order_graph.get(page):
                new_pages.insert(new_pages.index(new_page), page)
                inserted = True
                break
        if not inserted:
            new_pages.append(page)
    return new_pages


@benchmark_timer
def part1and2():
    rules, updates = parse_rules_updates(input_data)
    update_order_graph = create_update_graph(rules)
    count1 = 0
    count2 = 0
    for update in updates:
        pages = update.split(",")
        middle_index = len(pages) // 2
        correct_order = True
        checked_pages = []
        for page in pages:
            if not check_order(page, checked_pages, update_order_graph):
                correct_order = False
                break
            checked_pages.append(page)
        if correct_order:
            count1 += int(pages[middle_index])
        else:
            new_pages = rectify_order(pages, update_order_graph)
            count2 += int(new_pages[middle_index])
    print("part1: " + str(count1))
    print("part2: " + str(count2))

part1and2()


