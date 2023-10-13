'''
In this problem, a tree is an undirected graph that is connected and has no cycles.
You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added. The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed. The graph is represented as an array edges of length n where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the graph.
Return an edge that can be removed so that the resulting graph is a tree of n nodes. If there are multiple answers, return the answer that occurs last in the input.

Example 1:
Input: edges = [[1,2],[1,3],[2,3]]
Output: [2,3]

Example 2:
Input: edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
Output: [1,4]
'''

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        totalNodes = len(edges)+1
        nodeInfoMap={i:{"parent":i, "rank":1} for i in range(1, totalNodes)}

        # print(f"nodeInfoMap:{nodeInfoMap}")

        def findParent(node):
            if node == nodeInfoMap[node]["parent"]: return node
            return findParent(nodeInfoMap[node]["parent"])

        '''
        edges=[[3,4],[1,2],[2,4],[3,5],[2,5]]
              3---
              |  |
        1->2->4  |
           |     |
           |->5<-|
        return [2,5]
        '''
        def unionFind(a,b):
            parentA = findParent(a)
            parentB = findParent(b)
            # print(f"a:{a}, b:{b}")
            # print(f"parentA:{parentA}, parentB:{parentB}")

            if parentA == parentB: return False
            
            if nodeInfoMap[parentA]["rank"] > nodeInfoMap[parentB]["rank"]:
                # nodeInfoMap[b]["parent"] = parentA
                nodeInfoMap[parentB]["parent"] = parentA
            elif nodeInfoMap[parentA]["rank"] < nodeInfoMap[parentB]["rank"]:
                # nodeInfoMap[a]["parent"] = parentB
                nodeInfoMap[parentA]["parent"] = parentB
            else:
                # nodeInfoMap[b]["parent"] = parentA
                nodeInfoMap[parentB]["parent"] = parentA
                nodeInfoMap[parentA]["rank"]+=1
            
            return True
            # print(f"nodeInfoMap:{nodeInfoMap}")

        # print(f"nodeInfoMap:{nodeInfoMap}")

        for a,b in edges:
            if not unionFind(a,b): return [a,b]