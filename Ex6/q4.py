import doctest

import networkx as nx


# i've modified the dijkstra algo from here: https://www.geeksforgeeks.org/python-program-for-dijkstras-shortest-path
# -algorithm-greedy-algo-7/

def check_cycle(g):
    """
    :param g: Directed graph
    :return: if there is a DiGraph with weights Mul < 1
    >>> # First Cycle: 2->7->3
    Mul: 15
    Second Cycle: 5->8->4
    Mul: 42
    >>> g = nx.DiGraph()
    >>> edges = [(6, 1, 10), (1, 2, 2), (2, 7, 1), (3, 2, 3), (7, 3, 5), (5, 8, 6), (8, 4, 7), (4, 5, 1)]
    >>> g.add_weighted_edges_from(edges)
    >>> print(check_cycle(g))
    no cycle with Mul<1 found
    >>> # 2 cycles in the graph, first with Mul 6 and the second < 1
    >>> g = nx.DiGraph()
    >>> edges = [(6, 1, 0.1), (1, 2, 0.2), (2, 7, 10), (3, 2, 1.3), (7, 3, 0.5), (5, 8, 0.6), (8, 4, 0.7), (4, 5, 1.5)]
    >>> g.add_weighted_edges_from(edges)
    >>> print(check_cycle(g))
    Cycle:8->4->5
    Mul:0.6299999999999999
    >>> g = nx.DiGraph()
    >>> edges = [(1, 2, 0.5), (2, 1, 0.5)]
    >>> g.add_weighted_edges_from(edges)
    >>> print(check_cycle(g))
    Cycle:1->2
    Mul:0.25
    >>> # Cycle: [(1, 2, 'forward'), (2, 1, 'forward')]
    Mul: 1
    >>> g = nx.DiGraph()
    >>> edges = [(1, 2, 1), (2, 1,1)]
    >>> g.add_weighted_edges_from(edges)
    >>> print(check_cycle(g))
    no cycle with Mul<1 found
    >>> g = nx.DiGraph()
    >>> edges = [(1, 2, 2.5), (2, 3, 2), (3, 1, 1), (3, 4, 0.5), (4, 2, 0.1)]
    >>> g.add_weighted_edges_from(edges)
    >>> print(check_cycle(g))
    Cycle:2->3->4
    Mul:0.1
    """
    found_cycle = nx.simple_cycles(g)
    for cycle in found_cycle:
        Mul = 1
        res = ""
        for i in range(len(cycle) - 1):
            res += str(cycle[i]) + "->"
            u = cycle[i]
            v = cycle[i + 1]
            weight = g[u][v]["weight"]
            Mul *= weight
        u = cycle[len(cycle) - 1]
        v = cycle[0]
        weight = g[u][v]["weight"]
        Mul *= weight
        res += str(u)
        if Mul < 1:
            return "Cycle:" + res + "\nMul:" + str(Mul)
    return "no cycle with Mul<1 found"


def check_dijkstra(g, ver_num):
    """
    :param g:
    >>> # 2 cycles in graph, one with sum 14 one other with 0.36
    >>> g = Graph(8)
    >>> g.graph = [[0, 0.5, 0, 0, 0, 0, 0, 0, 0],
    ...           [0, 0, 0, 0, 0, 0, 0.8, 0, 0],
    ...           [0, 6, 0, 0, 0, 0, 0, 0, 0],
    ...           [0, 0, 0, 0, 0.9, 0, 0, 0, 0],
    ...           [0, 0, 0, 0, 0, 0, 0, 0.5, 0],
    ...           [1, 0, 0, 0, 0, 0, 0, 0, 0],
    ...           [0, 0, 3, 0, 0, 0, 0, 0, 0],
    ...           [0, 0, 0, 0.8, 0, 0, 0, 0, 0]]
    >>> check_dijkstra(g,g.get_vertices())
    3-> 4-> 7-> 3  0.36000000000000004
    >>> # just two nodes connected to each other
    >>> g = Graph(2)
    >>> g.graph = [[0, 0.5, 0],
    ...           [0.5, 0, 0]]
    >>> check_dijkstra(g,g.get_vertices())
    0-> 1-> 0  0.25
    >>> # empty graph
    >>> g = Graph(0)
    >>> g.graph = []
    >>> check_dijkstra(g,g.get_vertices())
    >>> # graph with one node
    >>> g = Graph(1)
    >>> g.graph = [[1,0]]
    >>> check_dijkstra(g,g.get_vertices())
    >>> # one cycle, but mul > 1
    >>> g = Graph(4)
    >>> g.graph = [[0, 0, 0, 0, 0, 0, 0.8, 0, 0],
    ...           [0, 6, 0, 0, 0, 0, 0, 0, 0],
    ...           [1, 0, 0, 0, 0, 0, 0, 0, 0],
    ...           [0, 0, 3, 0, 0, 0, 0, 0, 0]]
    >>> check_dijkstra(g,g.get_vertices())
    >>> # one cycle of 3 nodes with mul<1
    >>> g = Graph(3)
    >>> g.graph = [[0, 0.8, 0],
    ...           [0, 0, 0.3],
    ...           [0.6, 0, 0]]
    >>> check_dijkstra(g,g.get_vertices())
    0-> 1-> 2-> 0  0.144
    """
    for i in range(ver_num):
        res, dist = g.dijkstra(i)
        if dist < 1:
            print(res, dist)
            return


# Python program for Dijkstra's single
# source the shortest path algorithm. The program is
# for adjacency matrix representation of the graph
class Graph():

    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]
        self.memory = {}
        self.src = -1

    def get_vertices(self):
        return self.V

    def printSolution(self, dist):
        res = ""
        src_copy = self.src
        res += str(self.src) + "-> "
        while 1:
            if self.memory[self.src] == src_copy:
                res += str(self.memory[self.src]) + " "
                return res, dist
            res += str(self.memory[self.src]) + "-> "
            self.src = self.memory[self.src]

    # A utility function to find the vertex with
    # minimum distance value, from the set of vertices
    # not yet included in the shortest path tree
    def minDistance(self, dist, sptSet):

        # Initialize minimum distance for next node
        min = 1e7
        min_index = -1

        # Search the nearest vertex not in the
        # shortest path tree
        for v in range(self.V):
            if dist[v] < min and sptSet[v] == False:
                min = dist[v]
                min_index = v

        return min_index

    # Function that implements Dijkstra's single source
    # the shortest path algorithm for a graph represented
    # using adjacency matrix representation
    def dijkstra(self, src):
        self.src = src
        dist = [1e7] * self.V
        dist[src] = 1
        sptSet = [False] * self.V

        for cout in range(self.V):

            # Pick the minimum distance vertex from
            # the set of vertices not yet processed.
            # u is always equal to src in first iteration
            u = self.minDistance(dist, sptSet)
            if u == -1:
                return "no cycle found", 1

            # Put the minimum distance vertex in the
            # shortest path tree
            sptSet[u] = True

            # Update dist value of the adjacent vertices
            # of the picked vertex only if the current
            # distance is greater than new distance and
            # the vertex in not in the shortest path tree
            for v in range(self.V):
                if (self.graph[u][v] > 0 and
                        v == self.src):
                    dist[v] = dist[u] * self.graph[u][v]
                    self.memory[u] = v
                    return self.printSolution(dist[v])
                if (self.graph[u][v] > 0 and
                        sptSet[v] == False and
                        dist[v] > dist[u] * self.graph[u][v]):
                    self.memory[u] = v
                    dist[v] = dist[u] * self.graph[u][v]


if __name__ == '__main__':
    (failures, tests) = doctest.testmod(report=True)
    print("{} failures, {} tests".format(failures, tests))
