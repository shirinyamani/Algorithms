# Dijkstra Algorithm

Remember in SSSPP problem in case our graph is weighted, we couldnt use the BFS method? 
So the solution to the same problem for the case of weighted graph is **Dijkstra 😎**!

## Therminology

The idea is pretty simple! 
1. We set the starting point cost to 0 and all other nodes to infinity!
2. Start moving from the start point to the next oitential destination! Remember that the goal is to find **shortest path with minimum cost to each and every node in the graph**!
3. The way we work is add(+) the current node cost plus the cost on edge, then..
4. If the sumation of step 3, is **less** than the next node cost, we update the nxt node cost to the calculated cost!
5. If not, we don't do anything n leave the costs the way they are so far!
