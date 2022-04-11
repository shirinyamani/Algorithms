# Floyd Warshall Algorithm 😈

Similar to [Single Source Shortest Path Problem](https://github.com/shirinyamani/Algorithms/tree/main/graph/ssspp) problem, we have another problem called **All pairs  Shortest Path** problem!
Now the difference between these two is that in SSSPP we were given a Single source and we would asked for finding the shorterst path to all other vetices! 
However, in **All pairs problem**, we are asked to find all possible shortest path for each and every vertices in the graph, not just a single one!

Ginven that, the first step is to define a Matrix of all the vertices n their respective weighted edges! In this Matrix, as ya see we put `Infinity` for the vertices that do not have directed path to each other! For exp. from A to C we don't have any directed path (-->) therefore we put *"infinity"* in front of this cell!

Once we have created the Matrix so far, the next step is to go for the algorithm and the calculation part! The formula for the calculation is;

```
if D[source][destination] > D[source][viaX] + D[viaX][destination]:
    D[source][destination] = D[source][viaX] + D[viaX][destination]
```

So for exp imagine we wanna get to A from D via C! if so, then the D[source] will be D, D[destination] will be A and viaX will be C! then the calculation comes afterward!

So what we are basically doing here is using **all** vertices as **viaX** one time and calculate the formula and if it passes the condition then we update the relative edge in the initial Matrix! (12 in Matrix)

