'''
A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. 
Note that the path does not need to pass through the root.
The path sum of a path is the sum of the node's values in the path.
Given the root of a binary tree, return the maximum path sum of any non-empty path.


Example 1:
Input: root = [1,2,3]
Output: 6
Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.

Example 2:
Input: root = [-10,9,20,null,null,15,7]
Output: 42
Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        """
        可以與543題一起比較
        """

        res = root.val

        def traverse(node):
            if not node:
                return 0

            nonlocal res
            leftMax = traverse(node.left)
            rightMax = traverse(node.right)
            leftMax = max(leftMax, 0)       # 怕如果子樹是負的就直接變成0，等於不加了
            rightMax = max(rightMax, 0)     # 怕如果子樹是負的就直接變成0，等於不加了
            
            # with split
            res = max(res, node.val + leftMax + rightMax)   # 遍歷的過程中就不斷更新最大值

            # without split
            return node.val + max(leftMax, rightMax)    # 只看單邊子樹分支誰加起來的總合最大
            # return max(0, node.val + max(leftMax, rightMax))  # 這樣寫的話前面的leftMax和rightMax就不用加max
        
        traverse(root)
        return res