'''
Given the root of a binary tree, flatten the tree into a "linked list":
The "linked list" should use the same TreeNode class 
where the right child pointer points to the next node in the list 
and the left child pointer is always null.
The "linked list" should be in the same order as a pre-order traversal of the binary tree.

Example 1:
Input: root = [1,2,5,3,4,null,6]
Output: [1,null,2,null,3,null,4,null,5,null,6]

Example 2:
Input: root = []
Output: []

Example 3:
Input: root = [0]
Output: [0]
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        '''
        解題思路用stack，由右到左遍歷後，再從左子樹的繼續由右到左遍歷。
        因為是stack，所以左子樹會先被pop出來，接到root的right child，
        最後就會是由小排到大的linked list。
        '''

        if not root: return root

        stack = list()
        stack.append(root)

        while stack:
            curr = stack.pop()
            '''
            由右->左遍歷，所以最左邊的node就會在stack最上面，也是值最小的
            因此把當前curr.right接上stack最上方的節點(list的最後一個element) curr.right = stack[-1]
            因為要全部都排到右子樹，因此要由小到大排下來。
            '''
            if curr.right: stack.append(curr.right)
            if curr.left: stack.append(curr.left)

            if stack:
                curr.right = stack[-1]
            
            curr.left = None