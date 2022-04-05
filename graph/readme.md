# Graph
Collection of nodes and edges!

## Difference with Tree:
Graph can have a cycle/loop in itself, whereas tree can't!

<img src="./img/graph.png">

## How implement in python?
- Using a dictionary to store nodes and edges.
- Each node is a dictionary with key: value pairs ---> all the nodes that are connected to that node!

## Graph Traversal Algorithms : visiting all the nodes in a graph!
- Depth First Search (DFS)
- Breadth First Search (BFS)

## BFS 
- Level order traversal
- Implements using Queue (FIFO)
- Difference w/ tree: possible to have a loop, but to avoid it, we define "visited" nodes to not return back to the ones that already have been visited!

<img src="./img/bfs.png">