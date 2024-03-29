""" c15_2.py """


def bfs(graph, node):
    """ breadth-first search """
    visited = []
    queue = []
    visited.append(node)
    queue.append(node)
    print(f"push: {node} {queue} @")
    while queue:
        item = queue.pop(0)
        print(f"pop:  {item} {queue}")
        for curr in graph[item]:
            if curr not in visited:
                visited.append(curr)
                queue.append(curr)
                print(f"push: {curr} {queue} @")
    return visited


graph_a = {
    'a': ['b', 'c'],
    'b': ['d', 'e'],
    'c': [],
    'd': ['f'],
    'e': ['g', 'h'],
    'f': [],
    'g': ['h'],
    'h': []
}

print("BFS (Breadth-First Search)")
print(bfs(graph_a, 'a'))
