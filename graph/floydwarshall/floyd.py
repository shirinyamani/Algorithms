def floyd(num_vertice, graph):
    distance = graph #to keep the distances of the graph
    for target in range(num_vertice): #going thro all vertices
        for i in range(num_vertice): #go thro row
            for j in range(num_vertice):#go thro column
                distance[i][j] = min(distance[i][j], distance[i][target] + distance[target][i])

