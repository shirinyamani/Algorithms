class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []
        self.nodes = []

    def addVertex(self, value):
        self.nodes.append(value)

    def addEdge(self, source, distance, weight):
        self.graph.append([source,distance,weight])


    def bellman(self, src):
        dist = {i: float("Inf") for i in self.nodes}
        dist[src] = 0

        for _ in range(self.V - 1):
            for s, d, w in self.graph:
                if d[s] != float("Inf") and d[s] + w < dist[d]:
                    dist[d] = dist[s] + w

        for s,d,w in self.graph: #run it one more time (V th time) to catch whether have a - cycle!
            if d[s] != float("Inf") and d[s] + w < dist[d]:
                print("We have a Negative Cycle!")
                return
        
        #Step1 : Set all the vertexes except src to inf
        #Step2 : Run Algo for V-1 n check the condition
        #Step3 : Check the V th to recognize abt - cycle!
