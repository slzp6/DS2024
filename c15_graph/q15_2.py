""" q15_2.py """

import matplotlib.pyplot as plt
import networkx as nx

g = nx.Graph()

nodes = [0, 1, 2, 3, 4]
g.add_nodes_from(nodes)

edges = [(0, 1), (0, 2), \
         (1, 3), (1, 4), \
             (3, 4)]

g.add_edges_from(edges)

mpos = nx.spring_layout(g, seed=2024)
nx.draw_networkx(g, pos=mpos, \
                node_color='Cyan', \
                node_size=1000, font_size=25)
plt.show()
