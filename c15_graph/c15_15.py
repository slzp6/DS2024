""" q15_15.py """

import networkx as nx

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

g = nx.from_dict_of_lists(graph_a)

f_dfs = nx.dfs_tree(g, 'a')
print('dfs edges')
print(f_dfs.edges())
print('dfs nodes')
print(f_dfs.nodes())
print('')

f_bfs = nx.bfs_tree(g, 'a')
print('bfs edges')
print(f_bfs.edges())
print('bfs nodes')
print(f_bfs.nodes())

mpos = nx.spring_layout(g, seed=2618586)
nx.draw_networkx(g, pos=mpos, \
                 node_color='Cyan', \
                 node_size=800, \
                 font_size=25)
