

def path_cost(path):
    total_cost = 0
    for (node , cost ) in path:
        total_cost += cost
    return total_cost , path[-1][0]


def ucs(graph , start , goal):
    visited  =[]
    queue = [[(start,0)]]
    while queue :
        queue.sort(key=path_cost)
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