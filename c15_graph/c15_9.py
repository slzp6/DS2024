""" c15_9.py """

import matplotlib.pyplot as plt
import networkx as nx

g = nx.DiGraph()

nodes = ['a', 'b', 'c', 'd', 'e']
edges = [('a', 'b'), ('a', 'c'), ('a', 'e'),\
         ('b', 'd'), ('b', 'e'),\
         ('c', 'e'), ('d', 'e')]

g.add_nodes_from(nodes)
g.add_edges_from(edges)

N = 'b'
print(f"dgree [{N}]:     ", g.degree(N))
print(f"in-dgree [{N}]:  ", g.in_degree(N))
print(f"out-dgree [{N}]: ", g.out_degree(N))

mpos = nx.spring_layout(g, seed=42)
nx.draw_networkx(g, pos=mpos, \
                node_color='Cyan', \
                node_size=1000, font_size=25)
plt.show()
