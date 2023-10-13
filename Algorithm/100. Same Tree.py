'''
Given the roots of two binary trees p and q, 
write a function to check if they are the same or not.
Two binary trees are considered the same if they are structurally identical, 
and the nodes have the same value.

Example 1:
Input: p = [1,2,3], q = [1,2,3]
Output: true

Example 2:
Input: p = [1,2], q = [1,null,2]
Output: false

Example 3:
Input: p = [1,2,1], q = [1,1,2]
Output: false
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        '''
        思路: p和q本身的val相同，且p的左子樹等於q的左子樹，且p的右子樹等於q的右子樹。

        corner case:
        1. 如果p and q都為空節點，則return True
        2. 如果p和q其中一個為空節點，則return False
        3. 看root本身的值是否一樣
        4. 接著遞歸調用同一個function驗證左子樹and右子樹是否相同。
        '''
        if not p and not q: return True
        if not p or not q: return False

        if p.val != q.val: return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)