import numpy as np

class Graph():
    
    def __init__(self, vertices):
        self.V = vertices
        self.graph = np.array([[0, 10, 0, 30, 100],
                               [10, 0, 50, 0, 0],
                               [0, 50, 0, 20, 10],
                               [30, 0, 20, 0, 60],
                               [100, 0, 10, 60, 0]])
    
    def printSolution(self, dist):
        print("Vertex \t Distance from Source")
        for node in range(self.V):
            print(node, "\t\t", dist[node])
    
    def minDistance(self, dist, sptSet):
        min = 1e7
        for v in range(self.V):
            if dist[v] < min and not sptSet[v]:
                min = dist[v]
                min_index = v
        return min_index
    
    def dijkstra(self, src):
        dist = [1e7] * self.V
        dist[src] = 0
        sptSet = [False] * self.V

        for cout in range(self.V):
            u = self.minDistance(dist, sptSet)
            sptSet[u] = True
            for v in range(self.V):
                if (self.graph[u][v] > 0 and
                    not sptSet[v] and
                    dist[v] > dist[u] + self.graph[u][v]):
                    dist[v] = dist[u] + self.graph[u][v]
        self.printSolution(dist)
        
g = Graph(5)
g.dijkstra(0)

# Output esperado:
# Vertex   Distance from Source
# 0                0
# 1                10
# 2                50
# 3                30
# 4                60

# Fonte do código: https://www.geeksforgeeks.org/python-program-for-dijkstras-shortest-path-algorithm-greedy-algo-7/
