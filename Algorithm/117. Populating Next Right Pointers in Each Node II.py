'''
Given a binary tree

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. 
If there is no next right node, the next pointer should be set to NULL.
Initially, all next pointers are set to NULL.

Example 1:
Input: root = [1,2,3,4,5,null,7]
Output: [1,#,2,3,#,4,5,7,#]
Explanation: Given the above binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.

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
    def connect(self, root: 'Node') -> 'Node':
        if not root: return None

        '''
        這一題不是perfect binary tree，所以有可能沒有左子樹或右子樹
        '''

        curr = root # 當下遍歷那一層的Node，也會不斷變動(curr=curr.next)
        head = None # 下一層的第一個Node
        prev = None # 下一層會一直遍歷變動的Node(不斷進行連接的node)

        while curr:
            # 每一層遍歷的while loop
            while curr:
                if curr.left:
                    if not head:                # 先看看head(要記錄每一層的第一個node)是否已經存在
                        head = curr.left
                        prev = curr.left
                    else:
                        prev.next = curr.left
                        prev = prev.next
                
                if curr.right:
                    if not head:                # 有可能curr.left=None
                        head = curr.right
                        prev = curr.right
                    else:
                        prev.next = curr.right
                        prev = prev.next
            
                curr = curr.next

            curr = head
            head = None
            prev = None

        return root