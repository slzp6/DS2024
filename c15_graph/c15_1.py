""" c15_1.py """


def dfs(graph, node):
    """ depth-first search """
    dfs_list = []
    visited = []
    stack = []
    stack.append(node)
    visited.append(node)
    print(f"push: {node} {stack}")
    while stack:
        item = stack.pop()
        dfs_list.append(item)
        print(f"pop:  {item} {stack} @")
        for curr in graph[item][::-1]:
            if curr not in visited:
                visited.append(curr)
                stack.append(curr)
                print(f"push: {node} {stack}")
    return dfs_list


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

print("DFS (Depth-First Search)")
print(dfs(graph_a, 'a'))
