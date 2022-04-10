from collections import defaultdict
from platform import node

class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = defaultdict(list)
        self.distances = {}

    def addNode(self,value):
        self.nodes.add(value)

    def addEdge(self, fromNode, toNode, distance):
        self.edges[fromNode].append(toNode)
        self.distances[(fromNode, toNode)] = distance


def dijkstra(graph, start):
    visited = {start:0} #dont go over the gone path twice!
    path = defaultdict(list) #want the path from A to B nodes!

    nodes = set(graph.nodes)

    while nodes: #Goal is to find the minimum node(step 6)
        minNode = None #initially we don't have a value for the cost!(step 3 in info)
        for node in nodes:
            if node in visited:
                if minNode is None:
                    minNode = node
                elif visited[node] < visited[minNode]:
                    minNode = node
        if minNode is None: #not finding the minimum node cost! otherwise 
                break
                                  #continue to findout abt the wights!
        nodes.remove(minNode) #first if we visit the node, then remove it from the nodes list
        currentWeight = visited[minNode]

        for edge in graph.edges[minNode]: #calculate the weight
            weight = currentWeight + graph.distances[(minNode,edge)]
            if edge not in visited or weight < visited[edge]:
                visited[edge] = weight
                path[edge].append(minNode)

    return visited, path

if __name__=="__main__":

    customGraph = Graph()
    customGraph.addNode("A")
    customGraph.addNode("B")
    customGraph.addNode("C")
    customGraph.addNode("D")
    customGraph.addNode("E")
    customGraph.addNode("F")
    customGraph.addNode("G")
    customGraph.addEdge("A", "B", 2)
    customGraph.addEdge("A", "C", 5)
    customGraph.addEdge("B", "C", 6)
    customGraph.addEdge("B", "D", 1)
    customGraph.addEdge("B", "E", 3)
    customGraph.addEdge("C", "F", 8)
    customGraph.addEdge("D", "E", 4)
    customGraph.addEdge("E", "G", 9)
    customGraph.addEdge("F", "G", 7)

    print(dijkstra(customGraph, "A"))