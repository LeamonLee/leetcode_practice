'''
Given the root of a binary tree, imagine yourself standing on the right side of it, 
return the values of the nodes you can see ordered from top to bottom.

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []

        res=[]
        q = deque()
        q.appendleft(root)

        while q:
            lengthQ = len(q)
            for i in range(lengthQ):
                node = q.pop()
                if i == 0:
                    res.append(node.val)
                # res.append(node.val)
                
                # print(f"node:{node.val}, node.right:{node.right.val}")
                if node.right: q.appendleft(node.right)
                if node.left: q.appendleft(node.left)   # 雖然題目是只印右邊，但這一行還是要寫，因為如果遇到根節點只有左子樹沒有右子樹的情況，左子樹也要印出來。例如: [1,2]
        
        return res