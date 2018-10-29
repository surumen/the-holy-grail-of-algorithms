"""
Graph implementation
"""

class Graph:
    def __init__(self, num):
        self.adjList = {}   # To store graph: u -> (v,w)
        self.num_nodes = num    # Number of nodes in graph
        # To store the distance from source vertex
        self.dist = [0] * self.num_nodes
        self.par = [-1] * self.num_nodes  # To store the path

    def add_edge(self, u, v, w):
        #  Edge going from node u to v and v to u with weight w
        # u (w)-> v, v (w) -> u
        # Check if u already in graph
        if u in self.adjList.keys():
            self.adjList[u].append((v, w))
        else:
            self.adjList[u] = [(v, w)]

        # Assuming undirected graph
        if v in self.adjList.keys():
            self.adjList[v].append((u, w))
        else:
            self.adjList[v] = [(u, w)]

    def show_graph(self):
        # u -> v(w)
        for u in self.adjList:
            print(u, '->', ' -> '.join(str("{}({})".format(v, w))
                                       for v, w in self.adjList[u]))


