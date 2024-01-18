""" q15_1.py """


class Graph:
    """ graph """
    def __init__(self, num, directed=True):
        self.num = num
        self.directed = directed
        self.adj_matrix = \
            [[0 for _ in range(0, num)] \
             for _ in range(0, num)]

    def add_edge(self, src, dst, weight=1):
        """ add edge """
        self.adj_matrix[src][dst] = weight
        if not self.directed:
            self.adj_matrix[dst][src] = weight

    def display(self):
        """ display """
        print(*self.adj_matrix, sep='\n')
        print('')


print("directed")
g1 = Graph(5, directed=True)
g1.add_edge(0, 1, 8)
g1.add_edge(0, 2, 4)
g1.add_edge(1, 3, 3)
g1.add_edge(1, 4, 2)
g1.add_edge(3, 4, 2)
g1.display()

print("undirected")
g2 = Graph(5, directed=False)
g2.add_edge(0, 1, 8)
g2.add_edge(0, 2, 4)
g2.add_edge(1, 3, 3)
g2.add_edge(1, 4, 2)
g2.add_edge(3, 4, 2)
g2.display()
