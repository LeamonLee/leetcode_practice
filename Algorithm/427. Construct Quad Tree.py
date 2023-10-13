"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':

        #################### Neetcode的解答 #########################
        def helper(n, rStart, cStart):
            val = grid[rStart][cStart]
            isSame = True

            for r in range(n):
                for c in range(n):
                    if grid[rStart+r][cStart+c] != val:
                        isSame=False
                        break
            
            if isSame:
                # isLeaf = True if val == 1 else False
                return Node(val, True)
            
            n = n//2
            
            topLeft = helper(n, rStart, cStart)
            topRight = helper(n, rStart, cStart+n)
            bottomLeft = helper(n, rStart+n, cStart)
            bottomRight = helper(n, rStart+n, cStart+n)

            return Node(0, False, topLeft, topRight, bottomLeft, bottomRight)

        node = helper(len(grid), 0, 0)
        return node

        #################### 賈考博的解答 #########################

        # def helper(x1, y1, x2, y2):
        #     if x1 > x2 or y1 > y2: return None
            
        #     val = grid[x1][y1]
        #     isSame = True

        #     for r in range(x1, x2+1):
        #         for c in range(y1, y2+1):
        #             if grid[r][c] != val:
        #                 isSame=False
        #                 break
            
        #     node = Node()
        #     if isSame:
        #         node.val = val
        #         # node.isLeaf = True if val == 1 else False   # 這樣寫會報錯
        #         node.isLeaf = True
        #         return node
            
        #     midRow = (x1+x2)//2
        #     midCol = (y1+y2)//2

        #     node.val = 0
        #     node.isLeaf = False
        #     node.topLeft = helper(x1, y1, midRow, midCol)
        #     node.topRight = helper(x1, midCol+1, midRow, y2)
        #     node.bottomLeft = helper(midRow+1, y1, x2, midCol)
        #     node.bottomRight = helper(midRow+1, midCol+1, x2, y2)

        #     return node

        # node = helper(0, 0, len(grid)-1, len(grid[0])-1)
        # print(node.val, node.isLeaf, node.topLeft)
        # return node

        