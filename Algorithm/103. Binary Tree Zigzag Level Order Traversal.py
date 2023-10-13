'''
Given the root of a binary tree, 
return the zigzag level order traversal of its nodes' values. 
(i.e., from left to right, then right to left for the next level and alternate between).

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]

Example 2:
Input: root = [1]
Output: [[1]]

Example 3:
Input: root = []
Output: []
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []

        res=[]
        q=deque()
        q.appendleft(root)

        isLeft2Right = True
        while q:
            qLength = len(q)
            tmp=[]
            for _ in range(qLength):
                curr = q.pop()
                
                ''' 本題關鍵 '''
                if isLeft2Right:
                    tmp.append(curr.val)
                else:
                    tmp.insert(0, curr.val)

                if curr.left: q.appendleft(curr.left)
                if curr.right: q.appendleft(curr.right)
            
            isLeft2Right = not isLeft2Right 
            res.append(tmp)
        
        return res