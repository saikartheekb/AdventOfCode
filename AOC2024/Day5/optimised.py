from collections import defaultdict, deque
from timer.decorator.benchmark import benchmark_timer

def parse_input(input_data):
    rules, updates = [], []
    flip = True
    for line in input_data:
        line = line.strip()
        if not line:
            flip = False
            continue
        (rules if flip else updates).append(line.split("|" if flip else ","))
    return rules, updates

def build_graph(rules):
    graph = defaultdict(set)
    for x, y in rules:
        graph[x].add(y)
    return graph

def topological_sort(update, graph):
    # Build applicable graph and calculate in-degrees
    applicable_rules = {x: set() for x in update}
    in_degree = {x: 0 for x in update}
    for x in update:
        for y in graph[x]:
            if y in update:
                applicable_rules[x].add(y)
                in_degree[y] += 1

    # Perform Kahn's algorithm
    queue = deque([x for x in update if in_degree[x] == 0])
    sorted_order = []
    while queue:
        node = queue.popleft()
        sorted_order.append(node)
        for neighbor in applicable_rules[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return sorted_order

def validate_and_fix(update, graph):
    sorted_order = topological_sort(update, graph)
    return sorted_order == update, sorted_order

@benchmark_timer
def process_updates(rules, updates):
    graph = build_graph(rules)
    ordered_middle_sum = 0
    fixed_middle_sum = 0

    for update in updates:
        is_valid, sorted_order = validate_and_fix(update, graph)

        if is_valid:
            # Compute middle sum for already ordered updates
            middle_index = len(update) // 2
            ordered_middle_sum += int(update[middle_index])
        else:
            # Compute middle sum for fixed updates
            middle_index = len(sorted_order) // 2
            fixed_middle_sum += int(sorted_order[middle_index])

    return ordered_middle_sum, fixed_middle_sum

# Main execution
if __name__ == "__main__":
    with open("Day5/input", "r") as file:
        input_data = file.readlines()

    rules, updates = parse_input(input_data)

    # Process updates
    ordered_sum, fixed_sum = process_updates(rules, updates)

    # Print results
    print("Sum of middle pages (already ordered):", ordered_sum)
    print("Sum of fixed middle pages:", fixed_sum)
