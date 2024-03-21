'''
Given a binary tree, find the length of the longest consecutive sequence path.
The path refers to any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The longest consecutive path need to be from parent to child (cannot be the reverse).

Example 1:
Input:
   1
    \
     3
    / \
   2   4
        \
         5
Output:3
Explanation:
Longest consecutive sequence path is 3-4-5, so return 3.

Example 2:
Input:
   2
    \
     3
    / 
   2    
  / 
 1
Output:2
Explanation:
Longest consecutive sequence path is 2-3,not 3-2-1, so return 2.
'''

from lintcode import (
    TreeNode,
)

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the root of binary tree
    @return: the length of the longest consecutive sequence path
    """
    def longest_consecutive(self, root: TreeNode) -> int:
        # write your code here
        if not root: return 0
        res=1

        def helper(node, val, count):
            nonlocal res
            if not node: return 
            if node.val == val:
                count+=1
                res = max(res, count)
                helper(node.left, node.val+1, count)
                helper(node.right, node.val+1, count)
            else:
                helper(node.left, node.val+1, 1)
                helper(node.right, node.val+1, 1)

                # helper(node.left, node.left.val, 0)       (X)
                # helper(node.right, node.right.val, 0)      (X)

        helper(root, root.val, 0)
        return res
