def manhattan_heuristic(start_positions, goal_positions):
    total_distance = 0
    for start in start_positions:
        min_distance = float('inf')
        for goal in goal_positions:
            if isinstance(start, tuple) and isinstance(goal, tuple):
                distance = abs(start[0] - goal[0]) + abs(start[1] - goal[1])
                min_distance = min(min_distance, distance)
            else:
                raise ValueError("Expected tuple for start and goal positions")
        total_distance += min_distance
    return total_distance



def path_f_const(path , total_distance):
    g_cost = 0
    for (node, cost) in path:
        g_cost += cost
        last_node = path[-1][0]
        h_cost = total_distance
        f_cost = g_cost + h_cost
        return f_cost, last_node
# def path_f_const(path, heuristic):
#
#     # Calculate the cumulative cost (g_cost) from the path
#     g_cost = sum(cost for _, cost in path)
#
#     # Get the last node in the path
#     last_node = path[-1][0]
#
#     # Retrieve the heuristic cost for the last node
#     h_cost = heuristic.get(last_node, float('inf'))  # Default to infinity if not found
#
#     # Calculate the total cost (f_cost)
#     f_cost = g_cost + h_cost
#
#     return f_cost, last_node


def a_star(graph, start_positions, goals):
    visited = set()
    queue = [[(start, 0)] for start in start_positions]

    while queue:
        queue.sort(key=lambda path: sum(node[1] for node in path) + manhattan_heuristic([path[-1][0]], goals))
        path = queue.pop(0)
        node = path[-1][0]

        if node in visited:
            continue

        visited.add(node)

        if node in goals:
            return path

        adjacent_nodes = graph.get(node, [])

        for (node2, cost) in adjacent_nodes:
            new_path = path.copy()
            new_path.append((node2, cost))
            queue.append(new_path)

    return visited
