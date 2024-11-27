


def re_dfs(graph, start, visited=None):
    if visited is None:  # Initialize the visited set if it's not provided
        visited = set()
    visited.add(start)  # Mark the current vertex as visited
    print(start)  # Perform any operation, e.g., print the vertex
    for neighbor in graph[start]:  # Iterate through neighbors of the vertex
        if neighbor not in visited:  # Visit only unvisited neighbors
            re_dfs(graph, neighbor, visited)  # Recursively call re_dfs
    return visited