



def heuristic(state, goals):
    total_distance = 0

    for pos in state:
        min_distance = float('inf')
        for goal in goals:
            distance = abs(pos[0] - goal[0]) + abs(pos[1] - goal[1])
            min_distance = min(min_distance, distance)
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


def a_star(graph , start , goal):
    visited  =[]
    queue = [[(start,0)]]
    while queue :
        queue.sort(key=heuristic(start, goal))
        path = queue.pop(0)
        node = path[-1][0]
        if node in visited :
            continue
        visited.append(node)
        if node == goal:
            return path
        else:
            adjacent_nodes = graph.get(node,[])
            for (node2 ,cost )in adjacent_nodes:
                new_path =path.copy()
                new_path.append((node2,cost))
                queue.append(new_path)
        return visited