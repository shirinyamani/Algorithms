from collections import defaultdict

class Graph:
    def __init__(self,gdict):
        if gdict is None:
            gdict = {}
        self.gdict = gdict

    def bfs(self, start, end): #find shortest path from start to end
        q = [] #for saving the path

        q.append([start]) #first path

        while q:
            path = q.pop(0)
            node = path[-1] #last node in the path

            if node == end:
                return path
            
            for adjVertex in self.gdict.get(node, []):
                new_path = list(path)
                new_path.append(adjVertex)
                q.append(new_path)
    
if __name__ == "__main__":
    customGraph = {"A": ["B", "C"],
                   "B": ["D","G"],
                   "C": ["D","E"],
                   "D": ["F"],
                   "E": ["F"],
                   "F": ["G"]}
    
    g = Graph(customGraph)
    print(g.bfs("A", "F"))
