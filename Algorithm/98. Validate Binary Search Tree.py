'''
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:
The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

Example 1:
Input: root = [2,1,3]
Output: true

Example 2:
Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root: return True

        def helper(node, minValue, maxValue):
            if not node: return True
            
            # 如果node的val小於最小值，或大於最大值，則不是valid BST
            if node.val <= minValue or node.val >= maxValue: return False

            # 接著判斷左子樹和右子樹是否也都是valid BST
            return helper(node.left, minValue, node.val) and helper(node.right, node.val, maxValue)
        
        return helper(root.left, float("-inf"), root.val) and helper(root.right, root.val, float("inf"))