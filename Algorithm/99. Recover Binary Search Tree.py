'''
You are given the root of a binary search tree (BST), 
where the values of exactly two nodes of the tree were swapped by mistake. 
Recover the tree without changing its structure.

Example 1:
Input: root = [1,3,null,null,2]
Output: [3,1,null,null,2]
Explanation: 3 cannot be a left child of 1 because 3 > 1. Swapping 1 and 3 makes the BST valid.

Example 2:
Input: root = [3,1,4,null,null,2]
Output: [2,1,4,null,null,3]
Explanation: 2 cannot be in the right subtree of 3 because 2 < 3. Swapping 2 and 3 makes the BST valid.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        '''
        解題思路:
        正常的BST，如果是in-order遍歷，會是一個遞增的序列，例如1,2,3,4,5
        但如果發現是1,4,3,2,5，那就有問題了。
        可以用prev和curr兩個指針，如果第一次發現問題(prev>curr)，則prev是有問題的節點。
        如果第二次發現問題(prev>curr)，則是curr有問題。
        '''

        if not root: return None
        first = None
        second = None
        prev = None

        def helper(node):
            nonlocal first, second, prev
            if not node: return None

            helper(node.left)   # in-order遍歷，所以先跑左節點

            '''
            Example: 1     4     3  2  5 or 1  4  2  3  5
                     prev  node
            '''
            if prev and prev.val > node.val:
                # print(f"prev.val: {prev.val}, node.val: {node.val}")
                if not first: first = prev
                second = node
            
            prev = node # 可以這樣想: 因為最一開始是丟root進來，root沒有prev，所以這行會在第23行邏輯的後面
            
            helper(node.right)  # in-order遍歷，所以後跑右節點
        
        helper(root)
        # print(f"prev:{prev.val}, first:{first}, second:{second.val}")
        first.val, second.val = second.val, first.val