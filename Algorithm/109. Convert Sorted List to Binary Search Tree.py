'''
Given the head of a singly linked list where elements are sorted in ascending order, 
convert it to a height-balanced binary search tree.

Example 1:
Input: head = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: One possible answer is [0,-3,9,-10,null,5], which represents the shown height balanced BST.

Example 2:
Input: head = []
Output: []
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        '''
        解題思路: 和Sorted Array一樣，
        找到Linked List的中間Node，左邊就會是left child，右邊就會是right child。
        因此要找到Linked List的中間Node，就要用到快慢指針。
        while迴圈跑完後的slow就是中間點。
        '''
        if not head: return head

        def helper(start, end):
            if start == end: return None

            slow = start
            fast = start

            # while fast and fast.next: # <--- 這樣寫會報錯
            while fast != end and fast.next != end:
                slow = slow.next
                fast = fast.next.next
            
            
            root = TreeNode(val=slow.val)
            root.left = helper(start, slow)
            root.right = helper(slow.next, end)

            return root
        
        return helper(head, None)