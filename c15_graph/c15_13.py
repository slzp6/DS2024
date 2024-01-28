""" c15_13.py """

import matplotlib.pyplot as plt
import networkx as nx
# import scipy

nodes = ['a', 'b', 'c', 'd']
edges = [('a', 'b'), ('a', 'c'), \
         ('b', 'c'), ('c', 'd') ]

g = nx.Graph()
g.add_nodes_from(nodes)
g.add_edges_from(edges)

print("\n adjacency list")
for line in nx.generate_adjlist(g):
    print(line)

a = nx.adjacency_matrix(g)
print("\n adjacency matrix")
print(a.todense())

# a.setdiag(a.diagonal() * 2.0, k=0)
# print("\n adjacency matrix (for self-loop edges)")
# print(a.todense())

mpos = nx.spring_layout(g, seed=2618586)
nx.draw_networkx(g, pos=mpos, \
                 node_color='Cyan', \
                 node_size=800, \
                 font_size=25)
plt.show()
