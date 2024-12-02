def bfs(graph, start, goals):
    visited = set()
    queue = [[start]]
    while queue:
        path = queue.pop(0)
        node = path[-1]

        if node in visited:
            continue

        visited.add(node)


        if all(pos in goals for pos in node):
            return path


        adjacent_nodes = graph.get(node, [])
        for direction, (next_x, next_y), cost in adjacent_nodes:
            new_path = path.copy()
            new_path.append((next_x, next_y))
            queue.append(new_path)

    return None


def dfs(graph, start, goals):
    visited = set()
    stack = [[start]]
    while stack:
        path = stack.pop()
        node = path[-1]

        if node in visited:
            continue

        visited.add(node)


        if all(pos in goals for pos in node):
            return path  # Return the solution path if all goals are reached


        adjacent_nodes = graph.get(node, [])
        for direction, (next_x, next_y), cost in adjacent_nodes:
            new_path = path.copy()
            new_path.append((next_x, next_y))
            stack.append(new_path)

    return None

