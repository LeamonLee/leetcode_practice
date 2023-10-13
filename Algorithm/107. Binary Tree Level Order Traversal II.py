'''
Given the root of a binary tree, 
return the bottom-up level order traversal of its nodes' values. 
(i.e., from left to right, level by level from leaf to root).

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: [[15,7],[9,20],[3]]

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
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        '''
        這題作法一樣由上到下遍歷，但下層的結果會一值從array左邊insert進來，形成queue的概念(先進先出)。
        '''
        res=[]
        q=deque()
        q.appendleft(root)
        while q:
            lenQueue = len(q)
            tmp = []
            for _ in range(lenQueue):
                node = q.pop()
                if node.left:
                    q.appendleft(node.left)
                if node.right:
                    q.appendleft(node.right)
                tmp.append(node.val)
            res.insert(0, tmp)  # <--- 本題關鍵，遍歷依樣從上到下，但insert always從左邊insert進array
        
        return res