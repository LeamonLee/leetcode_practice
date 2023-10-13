'''
Given a binary tree, determine if it is height-balanced.

A height-balanced binary tree is a binary tree 
in which the depth of the two subtrees of every node never differs by more than one.

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: true

Example 2:
Input: root = [1,2,2,3,3,null,null,4,4]
Output: false

Example 3:
Input: root = []
Output: true
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(root):
            # 空節點本身也算是balanced Tree，所以要回傳True，但高度0。
            if not root:
                return [True, 0]
            
            left, right = dfs(root.left), dfs(root.right)

            # 左右子樹本身皆為balanced Tree，且左右子樹高度相差小於等於1
            isBalanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1

            return (isBalanced, 1 + max(left[1], right[1]))
        
        result = dfs(root)
        return result[0]