# Graph
Collection of nodes and edges!

## Difference with Tree:
Graph can have a cycle/loop in itself, whereas tree can't!

<img src="./img/graph.png">

## How implement a graph in python?
- Using a dictionary to store nodes and edges.
- Each node is a dictionary with key: value pairs ---> all the nodes that are connected to that node!

## Graph Traversal Algorithms: visiting all the nodes in a graph!
- Depth First Search (DFS)
- Breadth First Search (BFS)

## BFS ---> wider/broader on surface!
- Level order traversal
- Implements using Queue (FIFO)
- Difference w/ tree: possible to have a loop, but to avoid it, we define "visited" nodes to not return back to the ones that already have been visited!

<img src="./img/bfs.png">

## BFS desudo Code
1. Define a queue to store the nodes that are to be visited!
2. while queue is not empty:
    - pop the first node from the queue (Dequeue)
    - if the node has not been visited:
        - mark it as visited
        - add all the unvisited neighbors to the queue

<img src="./img/bfsq.png">

Python code added to the `graph.py` file

## DFS ---> deep in the tree/ asking children for a path!
- Hey Node X, do ya have a path to node Y? 
Node X: hmm, I'm not sure, lemme go and ask from my children!
Node X-child1: Hey child, do ya have a path to node Y? 
Node X-grandchild: Hmm, I'm not sure! Lemme go n ask from my child!
The process goes on and on and on, till we get to the target point! 
So as ya see DFS build with **Recursion**. 
But the problem with it is that it can get pretty tiring! Since maybe the target node is right next to the starting node, while we go deep in the trees children! So that's why we sometimes prefer to use **BFS**! 

- **NOTE TO REMEMBER:** In order to avoid stuck in an infinite loop, we need a **flag** to make sure that we have visited a node!
- Implements using Stack (LIFO)

<img src="./img/dfsCTCI.png">
<img src="./img/dfs.png">

## DFS desudo Code
1. Define a stack to store the nodes!
2. Push any starting node to the stack!
3. while stack is not empty:
    - pop the first node from the stack 
    - if the node has not been visited:
        - mark it as visited
        - push all the unvisited neighbors to the stack!

<img src="./img/dfss.png">

## Summary

<img src="./img/sum.png">