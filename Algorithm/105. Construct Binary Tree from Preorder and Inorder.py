'''
Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and 
inorder is the inorder traversal of the same tree, construct and return the binary tree.

Example 1:
Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]

Example 2:
Input: preorder = [-1], inorder = [-1]
Output: [-1]
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        '''
        preorder遍歷是"根左右"，因此可以知道第一個節點就是根節點。
        inorder遍歷是"左根右"，
        因此接著可以去inorder map中找到此根節點所在array中的index，就可以知道此根節點的左半邊都是左子樹，右半邊都是右子樹。
        '''

        # 先用一個map紀錄inorder所有值所在的index
        dctInOrderIdxMap = {}
        for i in range(len(inorder)):
            dctInOrderIdxMap[inorder[i]] = i
        
        def helper(preStart, inStart, inEnd):
            if preStart >= len(preorder) or inStart > inEnd:
                return None
            
            root = TreeNode(val=preorder[preStart])
            rootIndex = dctInOrderIdxMap[preorder[preStart]]

            # 因為preorder是"根左右"的特性，所以根節點的下一個肯定就是左子樹的根節點，因此new preStart是preStart+1
            root.left = helper(preStart+1, inStart, rootIndex-1)

            # 因為preorder是"根左右"的特性，所以右子樹的根節點必須從inorder的遍歷中判斷左子樹有多少個，再加上根節點一個，
            # 左子樹有多少個就是((rootIndex-1)-inStart+1)，根節點一個，所以new preStart=preStart+(rootIndex-inStart+1)
            # 例如左子樹從index=0開始，然後總共有5個，因此右子樹會從index=5開始，
            # 所以右子樹的starting index就是左子樹的starting index + 左子樹數量 = (preStart+1) + ((rootIndex-1)-(inStart)+1) 
            root.right = helper((preStart+1)+(rootIndex-inStart), rootIndex+1, inEnd)

            return root
        
        return helper(0, 0, len(inorder)-1)

