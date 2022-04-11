# Bellman Ford Algorithm 😈

Remember in [Dijkstra](https://github.com/shirinyamani/Algorithms/tree/main/graph/dijkstra) section I mentioned that it is not working on Negative Cycle Graphs? So it can be solved by Bellman Ford Algorithm! 😎
But always remember that whenever we have a Negative Cycle Graph, can only catch it then report it! So there would be No shortest path in such case!

So, let's see how **Bellman Ford Algorithm** works on positive cycle graphs first! The logic beyond it is pretty same as the Dijkstra Algorithm; updating the destintion vertex just in case the overall distance+edge weight is less than the current cost!
So in the exp. below, we wanna know abt the shortest path from E to all other nodes!
To do so, as before in the first iteration, we set the distance of the Starting Vertex (E) to 0 and all other nodes to infinity! Then get started with the process of comparing the cost of the current node with the cost of the next node! 

Remenber in the case of Bellman Ford Algorithm, we need to do this `number of vertex - 1` times! Therefore in our exp, we need to do this `4` times, right? 😜

So let's see the result in the chart below!

####add graph + chart 

## Dsudo Code

```
if the distance + weight of the source Vertex is less than the distance of the next node:
    update the distance of the destination Vertex to the distance + weight between the source Vertex and destination Vertex
```

Now let's look at the Negative case!
Remember I mentioned we run the algorithm `number of vertex - 1` times e.g. 4 times in our case? But just let's assume that we run it one more time(5 times!). if so, as you can see in the chart below the weights gonna be changed! So, we can conclude that whenever the weights changes, we have a negative cycle in the graph!

###add just the 5th iteration chart