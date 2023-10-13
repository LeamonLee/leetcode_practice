'''
In this problem, there is an undirected graph with n nodes. 
There is also an edges array. Where edges[i] = [a, b] means that there is an edge between node a and node b in the graph.
You need to return the number of connected components in that graph.

Example 1
Input:
3
[[0,1], [0,2]]
Output:
1

Example 2
Input:
6
[[0,1], [1,2], [2, 3], [4, 5]]
Output:
2
'''

from typing import (
    List,
)

class Solution:
    """
    @param n: the number of vertices
    @param edges: the edges of undirected graph
    @return: the number of connected components
    """
    def count_components(self, n: int, edges: List[List[int]]) -> int:
        # write your code here

        nodeInfoMap = {i:{"parent": i, "rank":1} for i in range(n) }
        numGroups=n
        def findParent(node):
            if node == nodeInfoMap[node]["parent"]: return node

            return findParent(nodeInfoMap[node]["parent"])
        
        def unionFind(a,b):
            nonlocal numGroups
            parentA = findParent(a)
            parentB = findParent(b)

            if parentA == parentB: return
            numGroups-=1

            if nodeInfoMap[a]["rank"] > nodeInfoMap[b]["rank"]:
                nodeInfoMap[parentB]["parent"] = parentA
            elif nodeInfoMap[a]["rank"] < nodeInfoMap[b]["rank"]:
                nodeInfoMap[parentA]["parent"] = parentB
            else:
                nodeInfoMap[parentB]["parent"] = parentA
                nodeInfoMap[parentA]["rank"] += 1
        
            return

        for a,b in edges:
            unionFind(a,b)
        return numGroups

