'''
Given two integer arrays inorder and postorder where inorder is the inorder traversal of a binary tree and postorder is the postorder traversal of the same tree, construct and return the binary tree.

Example 1:
Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
Output: [3,9,20,null,null,15,7]

Example 2:
Input: inorder = [-1], postorder = [-1]
Output: [-1]
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        '''
        postorder的特性是"左右根"，因此Postorder的最後一個節點是根節點。
        inorder遍歷是"左根右"，
        因此先用postorder的最後一個節點找到根節點，接著從inorder的map找到根節點所在的index，
        就可以以此index所在的左半邊當作左節點，以此index所在右半邊當作右節點。
        '''
        
        # 先用一個map紀錄inorder所有值所在的index
        dctInOrderIdxMap = {}
        for i in range(len(inorder)):
            dctInOrderIdxMap[inorder[i]] = i
        
        def helper(inStart, inEnd, postStart, postEnd):
            if inStart > inEnd or postStart > postEnd: return None

            rootVal = postorder[postEnd]
            rootIdx = dctInOrderIdxMap[rootVal]
            root = TreeNode(val=rootVal)

            # 左節點的個數有多少個，可以從inorder根節點的左半邊index判斷((rootIdx-1) - inStart + 1)，
            # 但是這邊是算index，也就是假設原本rootIdx=5，inStart=0，雖然左子樹有5個，但是index是從0~4，因此要再多減1
            root.left = helper(inStart, rootIdx-1, postStart, postStart+rootIdx-inStart-1)
            
            # postorder的特性是"左右根"，因此右節點的new postEnd很單純直接是postEnd-1
            # 右節點的new postStart則是看左子樹有多少個，也就是((rootIdx-1) - inStart +1) <--左子樹數量
            root.right = helper(rootIdx+1, inEnd, postStart+rootIdx-inStart, postEnd-1)

            return root
        
        root = helper(0, len(inorder)-1, 0, len(postorder)-1)
        return root