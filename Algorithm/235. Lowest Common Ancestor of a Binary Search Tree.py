'''
Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.
According to the definition of LCA on Wikipedia: 
“The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if  root.val < p.val and root.val < q.val:  # 代表p和q都在右子樹
            return self.lowestCommonAncestor(root.right, p, q)
        elif root.val > p.val and root.val > q.val: # 代表p和q都在左子樹
            return self.lowestCommonAncestor(root.left, p, q)
        else:   # 這個判斷式一定要寫在最後
            return root