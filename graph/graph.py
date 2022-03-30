#Graph representation

class Graph:
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict
        
    def addedge(self, vertex, edge):
        self.gdict[vertex].append(edge)