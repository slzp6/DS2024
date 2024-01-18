""" c15_12.py """

import networkx as nx

g = nx.complete_graph(5)

mpos = nx.spring_layout(g)
nx.draw_networkx(g, pos=mpos, \
                 node_color='Cyan', \
                     node_size=1000, \
                         font_size=30)
