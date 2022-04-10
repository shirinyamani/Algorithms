#Graph representation
class Graph:
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict

    def addedge(self, vertex, edge):
        self.gdict[vertex].append(edge)

    #BFS
    def bfs(self, vertex):
        queue = [vertex]
        visited = [vertex]
        while queue:
            deVertex = queue.pop(0) #works as the queue (FIFO)
            for adjecntdeVertex in self.gdict[deVertex]:
                if adjecntdeVertex not in visited:
                    visited.append(adjecntdeVertex)
                    queue.append(adjecntdeVertex)

    #DFS
    def dfs(self, vertex):
        stack = [vertex]
        visited = [vertex]
        while stack:
            popVertex = stack.pop() #bring last element
            for adjecentVertex in self.gdict[popVertex]:
                if adjecentVertex not in visited:
                    visited.append(adjecentVertex)
                    stack.append(adjecentVertex)




