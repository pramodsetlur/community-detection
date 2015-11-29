#Community Detection

This project detect communities in a graph. A graph would have nodes distributed and clustered in a particular manner. This program detects the set of communities with the highest modularity.

##USAGE
`$ python pramod_setlur_communities.py input(1).txt image.png`
  
  Each line in the input file is in the format `[number1] [number2]`. This indicates an edge between number 1 and number 2 in the graph
  You would need networkx and matplotlib to run this program.
  
##Algorithm
Initially the entire graph is considered as one community. Loop the following untill every node is considered a different community by itself.
  1. Calculate the betweenness of all the edges present in the graph.
  2. Remove the edge with the maximum betweenness. The resulting sub graphs are now considered seperate communities.
  3. Calculate the modularty.
  4. if the max_modularity has increased:
      Update the max_modularity
      Update the communities list

