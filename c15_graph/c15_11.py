""" c15_11.py """

import networkx as nx

g = nx.Graph()

nodes = ['a', 'b', 'c', 'd', 'e']
w_edges = [('a', 'b', 40), ('a', 'c', 30), \
           ('a', 'e', 40), ('b', 'd', 80), \
           ('b', 'e', 40), ('c', 'e', 30), \
           ('d', 'e', 20)]

g.add_nodes_from(nodes)
g.add_weighted_edges_from(w_edges)
print(g.edges(data=True))

pos = nx.spring_layout(g, seed=2)
weights = nx.get_edge_attributes(g, 'weight')

nx.draw(g, pos, with_labels=True, \
        node_color="deepskyblue",
        node_size=1000, font_size=25)
nx.draw_networkx_edge_labels(g, pos, \
                             font_size=20, \
                             edge_labels=weights)
