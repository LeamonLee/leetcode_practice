'''
Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), 
write a function to check whether these edges make up a valid tree.

Example 1:
Input: n = 5 edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
Output: true.

Example 2:
Input: n = 5 edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]
Output: false.
'''

from typing import (
    List,
)

class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """
    def valid_tree(self, n: int, edges: List[List[int]]) -> bool:
        # write your code here
        if n < 2: return True
        if len(edges)+1 < n: return False

        neighborMap={node:[] for node in range(n)}
        visited=set()
        for a,b in edges:
            neighborMap[a].append(b)
            neighborMap[b].append(a)
        
        def dfs(node, prev):
            if node in visited: return False
            
            visited.add(node)
            for nei in neighborMap[node]:
                if nei == prev: continue    # 例如node=1, prev=0, nei=0，就可以continue

                if not dfs(nei, node): return False
            
            return True
        
        res=dfs(0, -1)
        return res and len(visited) == n