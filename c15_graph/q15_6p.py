""" q15_6p.py """

from matplotlib import pyplot as plt
import networkx as nx

g = nx.gnp_random_graph(7, 0.5, seed=1)
# g = nx.karate_club_graph()

f_dfs = nx.dfs_tree(g, 0)

print('dfs edges')
print(f_dfs.edges())
print('dfs nodes')
print(f_dfs.nodes())
print('')

f_bfs = nx.bfs_tree(g, 0)
print('bfs edges')
print(f_bfs.edges())
print('bfs nodes')
print(f_bfs.nodes())

mpos = nx.spring_layout(g, seed=2024)
nx.draw_networkx(g, pos=mpos, \
                 node_color='Cyan', \
                 node_size=200, \
                 font_size=12)
plt.show()
plt.savefig("q15_6p.png")
