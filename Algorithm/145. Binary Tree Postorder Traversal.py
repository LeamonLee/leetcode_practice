'''
Given the root of a binary tree, return the postorder traversal of its nodes' values.

Example 1:
Input: root = [1,null,2,3]
Output: [3,2,1]

Example 2:
Input: root = []
Output: []

Example 3:
Input: root = [1]
Output: [1]
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ################## Stack Solution ##################
        
        if not root: return []

        stack = [(root, False)]
        ans = []
        while stack:
            curr, visited = stack.pop()
            if curr:
                if visited:
                    ans.append(curr.val)
                else:
                    stack.append((curr, True))
                    stack.append((curr.right, False))
                    stack.append((curr.left, False))

        return ans

        ################## DFS Solution ##################
        # if not root: return []

        # res = []
        # def helper(root):
        #     if not root: return None

        #     helper(root.left)
        #     helper(root.right)
        #     res.append(root.val)
        
        # helper(root)
        # return res