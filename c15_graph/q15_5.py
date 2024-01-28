""" q15_5.py """

import matplotlib.pyplot as plt
import networkx as nx

g = nx.Graph()

nodes = [0, 1, 2, 3, 4]
g.add_nodes_from(nodes)

edges = [(0, 1, {
    'weight': 2
}), (0, 2, {
    'weight': 2
}), (1, 3, {
    'weight': 3
}), (1, 4, {
    'weight': 4
}), (3, 4, {
    'weight': 8
})]
g.add_edges_from(edges)

edge_labels = {(0, 1): 2, (0, 2): 2, (1, 3): 3, (1, 4): 4, (3, 4): 8}

n0 = nx.shortest_path(g, \
        source=0, weight='weight')
print("All shortest paths from 0:")
print(n0)

n0_n4 = nx.shortest_path(g, \
        source=0, target=4, weight='weight')
print("\nShortest path from 0 to 4:")
print(n0_n4)

len_sp = nx.shortest_path_length(g, \
        source=0, target=4, weight='weight')
print("\nLength of the shortest path:")
print(len_sp)

mpos = nx.spring_layout(g, seed=2024)
nx.draw_networkx(g, pos=mpos, \
    node_color='Cyan', \
    node_size=400, font_size=20)
nx.draw_networkx_edge_labels(g, pos=mpos, \
        edge_labels=edge_labels,font_size=15)
plt.show()
