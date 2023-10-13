'''
You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.
Initially, all next pointers are set to NULL.

Example 1:
Input: root = [1,2,3,4,5,6,7]
Output: [1,#,2,3,#,4,5,6,7,#]
Explanation: Given the above perfect binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.

Example 2:
Input: root = []
Output: []
'''

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root: return None
        
        '''
        這一題是一個perfect BST，代表一定有左右子樹(除了leaf node之外)
        解題思路:用層次遍歷(Level order)從左到右，
        並且用head紀錄每一層最一開始的Node
        '''
        curr=root
        while curr:
            head = curr     # 為了記錄每層的第一個node
            
            # 在這個while迴圈完成一層的連接
            while curr:
                if curr.left and curr.right:
                    curr.left.next = curr.right
                
                if curr.right and curr.next:
                    curr.right.next = curr.next.left
                
                curr = curr.next
            
            # 移動到下一層
            curr = head.left
        
        return root