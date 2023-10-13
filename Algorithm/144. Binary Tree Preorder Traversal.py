# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ############## Stack Solution #############
        if not root: return []
        
        stack, res = [root], []   
        while stack:
            curr = stack.pop()
            if curr:
                res.append(curr.val)
                stack.append(curr.right)
                stack.append(curr.left)
        return res
        
        ############## DFS Solution #############

        # if not root: return []

        # res=[]

        # def helper(root):
        #     if not root: return
            
        #     res.append(root.val)
        #     helper(root.left)
        #     helper(root.right)
        
        # helper(root)
        # return res