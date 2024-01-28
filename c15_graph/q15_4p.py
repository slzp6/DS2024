""" q15_4p.py """

from matplotlib import pyplot as plt
import networkx as nx

g = nx.complete_graph(12)

mpos = nx.circular_layout(g)
nx.draw_networkx(g, pos=mpos, \
                 node_color='Cyan', \
                     node_size=1000, \
                         font_size=25)
plt.show()
plt.savefig("q15_4p.png")
