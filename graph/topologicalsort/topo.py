from collections import defaultdict

class Graph:
    def __init__(self,graphVertices):
        self.graph = defaultdict(list)
        self.graphVertices = graphVertices

    def addEdge(self,vertex, edge):
        self.graph[vertex].append(edge)


    def topohelper(self, currvertex, visited, stack):
        visited.append(currvertex)

        for i in self.graph[currvertex]: #traverse thro vertices
            if i not in visited:
                self.topohelper(i, visited, stack)

        stack.insert(0,currvertex) #LIFO

    def topo(self):
        visited = []
        stack = []

        for key in list(self.graph):
            if key not in visited:
                self.topohelper(key, visited,stack)

        print(stack)


if __name__ == "__main__":
    customGraph = Graph(8)
    customGraph.addEdge("A","C")
    customGraph.addEdge("C","E")
    customGraph.addEdge("E","H")
    customGraph.addEdge("E","F")
    customGraph.addEdge("F","G")
    customGraph.addEdge("B","D")
    customGraph.addEdge("B","C")
    customGraph.addEdge("D","F")
    
    print(Graph.topo(customGraph))