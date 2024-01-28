""" q15_3.py """

import matplotlib.pyplot as plt
import networkx as nx

g = nx.cycle_graph(12)

mpos = nx.spring_layout(g)
nx.draw_networkx(g, pos=mpos, \
                 node_color='Cyan', \
                     node_size=1000, \
                         font_size=25)
plt.show()
