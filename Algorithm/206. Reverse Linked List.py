# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        '''
                1       2      3     4
        pre -> head -> _next
               pre  -> head -> _next
        '''

        pre = None
        while head:
            _next = head.next
            head.next = pre
            pre = head
            head = _next
        
        return pre