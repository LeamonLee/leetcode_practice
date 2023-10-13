'''
Given the head of a singly linked list, return true if it is a 
palindrome or false otherwise.


Example 1:
Input: head = [1,2,2,1]
Output: true

Example 2:
Input: head = [1,2]
Output: false
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        mid = self.getMid(head)
        midNext = self.reverseLinkedList(mid.next)
        
        while midNext:
            if head.val == midNext.val:
                head = head.next
                midNext = midNext.next
            else:
                return False
        
        return True
        
    
    def getMid(self, head: ListNode):
        dummy = ListNode()
        dummy.next = head

        fast = slow = dummy
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        return slow
    
    def reverseLinkedList(self, head: ListNode):
        pre = None
        while head:
            temp = head.next
            head.next = pre
            pre = head
            head = temp
        return pre

