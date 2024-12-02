def hill_climbing_heuristic(current_position, goal_positions):
    min_distance = float('inf')
    for goal in goal_positions:
        distance = abs(current_position[0] - goal[0]) + abs(current_position[1] - goal[1])
        min_distance = min(min_distance, distance)
    return min_distance


def hill_climbing(graph, start_positions, goals):
    current_positions = start_positions
    path = [start_positions]

    while True:
        next_move = None
        current_heuristic = hill_climbing_heuristic(current_positions, goals)

        for current_position in current_positions:
            adjacent_nodes = graph.get(current_position, [])

            for (node, cost) in adjacent_nodes:
                new_positions = [p for p in current_positions if p != current_position] + [node]
                heuristic = hill_climbing_heuristic(new_positions, goals)

                if heuristic < current_heuristic:
                    current_heuristic = heuristic
                    next_move = new_positions

        if next_move is None:
            break

        current_positions = next_move
        path.append(current_positions)

    return path
