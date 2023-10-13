# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        res=[]

        def preOrder(node: Optional[TreeNode]):
            if not node: return None

            res.append(str(node.val))

            if node.left:
                res.append('(')
                preOrder(node.left)
                res.append(')')    
            else:
                if node.right:
                    res.append('()')

            if node.right:
                res.append('(')
                preOrder(node.right)
                res.append(')')

        
        preOrder(root)
        return "".join(res)

