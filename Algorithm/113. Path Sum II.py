'''
Given the root of a binary tree and an integer targetSum, 
return all root-to-leaf paths where the sum of the node values in the path equals targetSum. 
Each path should be returned as a list of the node values, not node references.
A root-to-leaf path is a path starting from the root and ending at any leaf node. 
A leaf is a node with no children.

Example1:
Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: [[5,4,11,2],[5,8,4,5]]
Explanation: There are two paths whose sum equals targetSum:
5 + 4 + 11 + 2 = 22
5 + 8 + 4 + 5 = 22

Example2:
Input: root = [1,2,3], targetSum = 5
Output: []
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root: return []
        res=[]

        def backtrack(root, targetSum, temp):
            if not root: return
            if not root.left and not root.right:    # 如果都沒有左右節點，代表到了leaf Node
                if root.val == targetSum:           # 且當前leaf Node的值等於傳進來的targetSum的話
                    temp.append(root.val)
                    res.append(temp.copy())
                    temp.pop()                  # 記得要再pop掉
                    return
            
            temp.append(root.val)
            backtrack(root.left, targetSum-root.val, temp)
            backtrack(root.right, targetSum-root.val, temp)
            temp.pop()
        
        backtrack(root, targetSum, [])
        return res