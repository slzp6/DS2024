""" c15_14.py """

import networkx as nx

g = nx.DiGraph()

nodes = ['a', 'b', 'c', 'd', 'e']
w_edges = [('a', 'b', 15), ('a', 'c', 79), \
           ('a', 'd', 4), ('a', 'e',  52), \
           ('c', 'd', 20), ('c', 'e', 24), \
           ('e', 'd', 386)]

g.add_nodes_from(nodes)
g.add_weighted_edges_from(w_edges)
print(g.edges(data=True))

a = nx.adjacency_matrix(g)
print("\n adjacency matrix")
print(a.todense())

pos = nx.circular_layout(g)
weights = nx.get_edge_attributes(g, 'weight')

nx.draw(g, pos, with_labels=True, \
        node_color="deepskyblue",
        node_size=1000, font_size=25)
nx.draw_networkx_edge_labels(g, pos, \
                             font_size=20, \
                             edge_labels=weights)
