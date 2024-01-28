""" c15_7.py """

import matplotlib.pyplot as plt
import networkx as nx

g = nx.Graph()
nodes = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
edges = [('a', 'b'), ('a', 'c'), ('a', 'd'), \
         ('b', 'd'), ('c', 'd'), \
         ('e', 'h'), ('f', 'g'), ('f', 'h'), ('g','h'), \
         ('h', 'i')]

g.add_nodes_from(nodes)
g.add_edges_from(edges)

print("connected: ", nx.is_connected(g))
cc = list(nx.connected_components(g))
print("components: ", cc)

mpos = nx.spring_layout(g, seed=101)
nx.draw_networkx(g, pos=mpos, \
                node_color='Cyan', \
                node_size=200, font_size=10)
plt.show()
