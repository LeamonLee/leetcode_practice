'''
Given the head of a sorted linked list, 
delete all nodes that have duplicate numbers, 
leaving only distinct numbers from the original list. 
Return the linked list sorted as well.


Example 1:
Input: head = [1,2,3,3,4,4,5]
Output: [1,2,5]

Example 2:
Input: head = [1,1,1,2,3]
Output: [2,3]
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: return head

        '''
        題目給定的head已經排序好了
        這題只要發現有重複的node要全部砍掉，一個都不能留

        '''

        dummy = ListNode()
        dummy.next = head
        curr = dummy

        while curr.next and curr.next.next:
            # 代表有重複，因此需要把下一個和下下個拿掉
            '''
                  1,  1,2,3
            dummy head
            curr-->

            curr------>
            curr-------->
            '''
            if curr.next.val == curr.next.next.val:
                val = curr.next.val
                while curr.next and curr.next.val == val:
                    curr.next = curr.next.next
            else:
                curr = curr.next
        
        return dummy.next