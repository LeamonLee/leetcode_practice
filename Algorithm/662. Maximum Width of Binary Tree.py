'''
Given the root of a binary tree, return the maximum width of the given tree.
The maximum width of a tree is the maximum width among all levels.
The width of one level is defined as the length between the end-nodes (the leftmost and rightmost non-null nodes), where the null nodes between the end-nodes that would be present in a complete binary tree extending down to that level are also counted into the length calculation.
It is guaranteed that the answer will in the range of a 32-bit signed integer.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root: return 0

        maxWidth = 0
        q=deque()
        q.appendleft((root, 0))
        while q:
            headIndex=0
            tailIndex=0
            qLength = len(q)
            for i in range(qLength):
                node, nodeIndex = q.pop()
                if i==0:
                    headIndex = nodeIndex
                
                tailIndex = nodeIndex
                '''
                解題重點:
                這題主要運用BST節點的特性，
                左子樹的index=當前節點index*2
                右子樹的index=當前節點index*2 + 1
                '''
                if node.left: q.appendleft((node.left, nodeIndex*2))
                if node.right: q.appendleft((node.right, (nodeIndex*2)+1))
            
            maxWidth = max(maxWidth, tailIndex-headIndex+1)
        
        return maxWidth

