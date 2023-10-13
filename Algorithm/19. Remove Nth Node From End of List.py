'''
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Example 1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:
Input: head = [1], n = 1
Output: []

Example 3:
Input: head = [1,2], n = 1
Output: [1]
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        first = second = dummy

        '''
        使用兩個指標(first和second)，
        先將first移動n步，
        接著將first和second同時移動，當first為None時，則second就會剛好在要刪除node的前面
        '''

        for _ in range(n+1):
            first = first.next
        
        while first:
            first = first.next
            second = second.next
        
        second.next = second.next.next

        return dummy.next