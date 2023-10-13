'''
Given the root of a binary tree, 
check whether it is a mirror of itself (i.e., symmetric around its center).

Example 1:
Input: root = [1,2,2,3,4,4,3]
Output: true

Example 2:
Input: root = [1,2,2,null,3,null,3]
Output: false
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root: return True

        def helper(left, right):
            '''
            直覺想法: symmetric tree左右子樹本身val相同，且且左子樹的左子樹等於右子樹的右子樹，且左子樹的右子樹等於右子樹的左子樹。
            1. 如果左右節點都為空節點，則是symmetric tree
            2. 如果只有其中一邊為空節點，則不為symmetric tree
            3. 如果左右節點值不一樣，則不為symmetric tree
            4. 以上都通過了，最後驗證左右子樹是否也為symmetric tree
            '''
            if not left and not right: return True
            if not left or not right: return False
            if left.val != right.val: return False

            return helper(left.left, right.right) and helper(left.right, right.left)
        
        return helper(root.left, root.right)