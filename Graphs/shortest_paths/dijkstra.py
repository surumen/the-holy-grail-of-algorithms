""""
Dijkstra finds the shortest path from Node A to Node B in a weighted graph
regardless of if there is a cycle or not (as long as there are no negative
weights).

However, it doesn't calculate all paths from A to B. It stops when it finds
the shortest path from A to B.
"""
from graph import Graph
from priority_queue import PriorityQueue

def dijkstra_single_source(graph, src):
    # flush old junk values in par[]
    graph.par = [-1] * graph.num_nodes

    # set distance of starting node to 0
    graph.dist[src] = 0

    # initialize priority queue
    Q = PriorityQueue()
    Q.insert((0, src))
    for u in graph.adjList.keys():
        if u != src:
            graph.dist[u] = sys.maxsize # infinity
            graph.par[u] = -1

    while not Q.isEmpty():
        u = Q.extract_min() # return node with the min dist from source

        # Update the distance of all the neighbors of u and
        # if their prev distance was INFINITY then push them into Queue
        for v, w in graph.adjList[u]:
            new_dist = graph.dist[u] + w
            if graph.dist[v] > new_dist:
                if graph.dist[v]


