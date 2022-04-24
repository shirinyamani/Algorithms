class graph:
    def __init__(self, gdic):
        if gdic is None:
            gdic = {}
        gdic = self.gdic

    def add_edge(self, node, edge):
        self.gdic[node].append(edge)


    def BFS(self, node):
        queue = [node]
        visited = [node]
        while queue:
            denode = queue.pop(0)
            for adjacent in self.gdic[denode]:
                if adjacent not in visited:
                    queue.append(adjacent)
                    visited.append(adjacent)


    def DFS(self, node):
        stack = [node]
        visited = [node]

        while stack:
            denode = stack.pop()
            for children in self.gdic[denode]:
                if children not in visited:
                    visited.append(children)
                    stack.append(children)




