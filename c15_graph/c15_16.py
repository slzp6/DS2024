""" c15_16.py """

import pprint

import matplotlib.pyplot as plt
import networkx as nx

G_a = nx.complete_graph(6)

G_b = nx.complete_graph(6)
G_b = nx.relabel_nodes(G_b, {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f'})

G_c = nx.from_edgelist([(0, 'z'), ('a', 'z')])
G = nx.compose_all([G_a, G_b, G_c])

pos = nx.spring_layout(G, seed=80586)
nx.draw_networkx(G, pos, with_labels=True, node_size=1000, \
        font_size=25, node_color="deepskyblue")
plt.show()

dc = nx.degree_centrality(G)
bc = nx.betweenness_centrality(G)

print("degree centrality")
pprint.pprint(dc)
print("")
print('max: ', max(dc, key=dc.get), max(dc.values()))
print('min: ', min(dc, key=dc.get), min(dc.values()))

print("\n ---------- ")
print("betweenness centrality")
pprint.pprint(bc)
print("")
print('max: ', max(bc, key=bc.get), max(bc.values()))
print('min: ', min(bc, key=bc.get), min(bc.values()))
