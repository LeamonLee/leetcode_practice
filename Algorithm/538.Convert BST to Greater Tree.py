# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        curSum = 0

        '''
        關鍵在於 遍歷右中左子樹
        Solution1 (Recursion)
        '''
        def inOrder(node: Optional[TreeNode]):
            if not node: return
            nonlocal curSum

            inOrder(node.right)
            
            curSum += node.val
            node.val = curSum

            inOrder(node.left)
        
        inOrder(root)
        return root

        #####################################################
        '''
        關鍵在於 遍歷右中左子樹
        Solution2 (Stack)
        '''
        # currSum = 0
        # stack = []
        # curr=root

        # while curr or stack:
        #     while curr:
        #         stack.append(curr)
        #         curr = curr.right
            
        #     curr = stack.pop()
        #     currSum+=curr.val
        #     curr.val=currSum

        #     curr = curr.left
        
        # return root

