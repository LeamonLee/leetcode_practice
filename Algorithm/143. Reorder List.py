'''
You are given the head of a singly linked-list. 

The list can be represented as:
L0 → L1 → … → Ln - 1 → Ln

Reorder the list to be on the following form:
L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.

Example 1:
Input: head = [1,2,3,4]
Output: [1,4,2,3]

Example 2:
Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        ''' Step1: Get Middle and split it into 2 linked list '''
        middle = self.getMiddle(head)
        l2 = middle.next
        middle.next = None

        ''' Step2: reverse the second list '''
        l2 = self.reverse(l2)

        ''' Step3: merge two list together '''
        ''' 兩個list merge時要考慮4個角色: l1, l1_next, l2, l2_next '''
        while (head is not None and l2 is not None):
            l1_next = head.next
            l2_next = l2.next

            head.next = l2
            
            l2.next = l1_next

            head = l1_next
            l2 = l2_next
        
        # if l2:
        #     head.next = l2
        
        # if head:
        #     head.next = head

        return


    def getMiddle(self, head: Optional[ListNode]):
        slow=head
        fast=head

        '''
        找Linked list有兩種寫法
        1. while (fast.next and fast.next.next):
        2. while (fast and fast.next): 

        假設一個linked list是1 -> 2 -> 3 -> 4
        在偶數情況下，第一種會找到2，第二種會找到3
        '''
        while (fast.next is not None and fast.next.next is not None):
            slow = slow.next
            fast = fast.next.next
        
        return slow
    
    def reverse(self, head: Optional[ListNode]):
        '''
        None -> head -> head.next
        prev -> head -> _next
                prev    head
        '''
        prev = None
        while (head is not None):
            _next = head.next
            head.next = prev
            prev = head
            head = _next
        
        return prev
