We are creating the worst possible script for BOTC!!! (We being me and one Grace!!!)

Some may ask, "Why would you do this?" and those who ask certainly have their right to ask. However, as much as you have a right to ask, I have my right not to answer. 

**Sceptic**: "Why are you making the _worst_ possible script?

**Tristan**: "..."

**Sceptic**: "No seriously... why???"

**Tristan**: "BECAUSE WE CAN!"


Some may say "Just because we can doesn't mean we should", but too bad I didn't take the time to think about that. May I present the worst possible scripts you can make in BOTC. 
Now, of course, worse is a very subjective term. We have to find a way to mathematically define worse. Starting out, we simply define unplayability by how many jinxes are present in the script.
Later on, we hope to expand this by giving a "salty-ness" value to each jinx and maximizing the total salt score. 

This problem is broken down in pure and abstracted math. Grace posed the script formation process as selecting a subgraph over the graph of all characters, where jinxes are edges in said graph.
Each character falls into one of four disjoint sets denoting the character type, such as minion or demon. 
From there, we are tasked with selecting a set of nodes within the graph of specific sizes (based on how many players are present, how many of each character type we want in the game) to maximize the number of edges among the selected nodes. 
Easy, right!

Well, we could think about this as purely a graph problem. It stands that if we ignore the character type sets and are just selecting nodes, a greedy algorithm that starts with the complete graph and removes nodes would perform well. (optimal, i think, have not thought about it much)
But then as we add in sets it complicates. So what we do is we ignore all thought on trying to find an algorithm, and break it down further into pure math nonsense. See the PDF LP_for_grace.pdf for details. It really is quite interesting how we turn this graph problem into pure linear equations.
Once we represent the entire problem as linear equations, specifically an IP, we can rely on the work of others to solve it. Convex analysis Woo! Branch and bound my beloved! We throw existing tools at the equations and BAM, out falls an optimal solution. 

Enjoy!
