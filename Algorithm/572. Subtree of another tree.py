# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot: return True # 如果subTree為null就算有subtree了
        if not root: return False
        
        if root.val == subRoot.val:
            if self.helper(root, subRoot): return True
        
        # 這裡不能寫else，因為如果根節點失敗的話，可以試試看左右子節點
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot) # 這裡是要recursively call isSubtree
    
    def helper(self, root, subRoot):
        if not root and not subRoot: return True    # 兩個都null就回傳True
        if not root or not subRoot: return False    # 其中一個null就回傳False

        if root.val != subRoot.val: return False

        return self.helper(root.left, subRoot.left) and self.helper(root.right, subRoot.right) 