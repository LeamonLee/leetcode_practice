'''
Given a binary tree, find its minimum depth.
The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
Note: A leaf is a node with no children.

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: 2

Example 2:
Input: root = [2,null,3,null,4,null,5,null,6]
Output: 5
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        ''' 除了這種recursion的方法之外，還可以使用level order(層次遍歷)，用deque '''
        if not root: return 0

        # 如果左節點或右節點可能為空的時候，則返回其中一邊子節點不為空的深度(取最大值，因為為空的那一邊深度一定為0)，
        # 因為不為空的那一邊才有可能找到葉子節點。
        # 如果左右都為空，則取min或max都沒差別了，因為下一層就會都返回0
        if not root.left or not root.right:
            return 1 + max(self.minDepth(root.left), self.minDepth(root.right))
        
        # 左右節點都不為空的情況，則取min
        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))