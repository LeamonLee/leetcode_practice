'''
Given the root of a binary tree, return the inorder traversal of its nodes' values.

Example 1:
Input: root = [1,null,2,3]
Output: [1,3,2]

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
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        # ======================= deque Stack Solution ========================
        res=[]
        stack = deque() # 使用deque當做stack
        curr = root
        while curr or stack:
            while curr: # 把所有左子樹都append進去
                stack.append(curr)
                curr=curr.left
            
            curr = stack.pop()
            res.append(curr.val)
            curr = curr.right
        
        return res
            
        # ======================= List Stack Solution ========================
        
        # res=[]
        # stack=[]      # 使用list當做stack，缺點就是容量是dynamic的，如果超過就要做memory relocation
        # curr = root

        # while curr or stack:
        #     while curr:
        #         stack.append(curr)
        #         curr = curr.left
            
        #     curr = stack.pop()
        #     res.append(curr.val)
        #     curr = curr.right
        
        # return res

        # ====================== DFS Solution =========================

        # res=[]

        # def inOrder(node):
        #     if not node: return None

        #     inOrder(node.left)
        #     res.append(node.val)
        #     inOrder(node.right)
        
        # inOrder(root)
        # return res

        