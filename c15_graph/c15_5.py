""" c15_5.py """

import matplotlib.pyplot as plt
import networkx as nx

g = nx.Graph()
nodes = ['a', 'b', 'c', 'd']
edges = [('a', 'b'), ('a', 'c'), \
         ('a', 'd'), ('c', 'd')]

g.add_nodes_from(nodes)
g.add_edges_from(edges)

print("a - b : ", g.has_edge('a', 'b'))
print("b - d : ", g.has_edge('b', 'd'))

nh_a = list(g.neighbors('a'))
print("neighbors('a'): ", nh_a)

mpos = nx.spring_layout(g, seed=42)
nx.draw_networkx(g, pos=mpos, \
                node_color='Cyan', \
                node_size=1000, font_size=25)
plt.show()
