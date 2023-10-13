'''
Given a linked list, swap every two adjacent nodes and return its head. 
You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

Example 1:
Input: head = [1,2,3,4]
Output: [2,1,4,3]

Example 2:
Input: head = []
Output: []

Example 3:
Input: head = [1]
Output: [1]
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: return head

        '''
        dummy     -> head      
        curr         first     second
    ==> curr.next -> second -> first
    ==>                        curr
        '''

        dummy = ListNode()
        dummy.next = head           # 這一行和下一行對調也可以work
        curr = dummy

        while curr.next and curr.next.next:
            first = curr.next
            second = curr.next.next

            curr.next = second      # 這一行寫到下下行也可以work
            first.next = second.next    # 這一行是關鍵，要把first接到原本second的next
            second.next = first     

            curr = curr.next.next   # 不能寫 curr = second，會報錯
        
        return dummy.next