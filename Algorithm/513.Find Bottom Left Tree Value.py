'''
Given the root of a binary tree, return the leftmost value in the last row of the tree.


Example 1:
Input: root = [2,1,3]
Output: 1

Example 2:
Input: root = [1,2,3,4,null,5,6,null,null,7]
Output: 7
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        '''
        由右往左遍歷，不斷加進queue裡面，看是要appendleft再pop還是append再popleft都可以，
        因為是先放右邊節點，再放左邊節點，所以最後pop出來的節點就是最後一個left node。
        '''
        q = deque([root])

        while q:
            node = q.popleft()
            if node.right: q.append(node.right)
            if node.left: q.append(node.left)
        
        return node.val