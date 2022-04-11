# Dijkstra Algorithm 😈

Remember in SSSPP problem in case our graph is weighted, we couldnt use the BFS method? 
So the solution to the same problem for the case of weighted graph is **Dijkstra 😎**!

## Therminology

The idea is pretty simple! 
1. We set the starting point cost to 0 and all other nodes to infinity!
2. Start moving from the start point to the next oitential destination! Remember that the goal is to find **shortest path with minimum cost to each and every node in the graph**!
3. The way we work is add(+) the current node cost plus the cost on edge, then..
4. If the sumation of step 3, is **less** than the next node cost, we update the nxt node cost to the calculated cost!
5. If not, we don't do anything n leave the costs the way they are so far!
6. We compare the nodes, chose the minimum among them n continue our path along the minimum node!


## 🔥 Notice

**Dijkstra** does not work on Negative Cycle Graphs! Ya ask why? Look at the picture below!

#####Add Picture!

Imagine we wanna get to B from A (Paths from A to B),however as there is a directional approaching to A so we can't go back to A from B! Therefore, we need to go thro the cycle (D-->B--->A) to reach out to A, right? 
But opss... there is a Negative edge there! So let's go thro it and see what happens! (calculation in the picture)!
So as ya saw, as we walked thro the cycle heading to A, the total sum of the weights became Negative! (-5)! 
Remember, the overal goal was to find minimum cost? So what if we go thro the cycle one more time? If so, the total sum will be -7 which is less than -5! So as ya go over n over the loop, the overall weight becomes smaller n smaller! Which means we are stucking in n infinity loop, right? So that's why Dijkstra is not working on Negative Cycle Graphs!


