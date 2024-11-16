def bfs(graph,start,goals):
    visited =[]
    queue = [[start]]
    while queue :
        path = queue.pop(0)
        node = path[-1]
        if node in visited:
            continue
        visited.append(node)
        if all(pos in goals for pos in node):
            solution_path = path
            break
        else:
            adjacent_nodes = graph.get(node,[])
            for node2 in adjacent_nodes:
                new_path = path.copy()
                new_path.append(node2)
                queue.append(new_path)
    return visited,path



def dfs(graph,start,goals):
    visited =[]
    stack = [[start]]
    while stack :
        path=stack.pop()
        node = path[-1]
        if node in visited:
            continue
        visited.append(node)
        if all(pos in goals for pos in node):
            solution_path = path
            break
        else:
            adjacent_nodes = graph.get(node,[])
            for node2 in adjacent_nodes:
                new_path = path.copy()
                new_path.append(node2)
                stack.append(new_path)
    return visited,path
