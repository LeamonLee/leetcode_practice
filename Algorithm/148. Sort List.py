'''
Given the head of a linked list, return the list after sorting it in ascending order.

Example1:
Input: head = [4,2,1,3]
Output: [1,2,3,4]

Example2:
Input: head = [-1,5,3,4,0]
Output: [-1,0,3,4,5]
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: return head 

        '''
        使用merge sort
        '''

        ''' Get the Middle '''
        middle = self.getMiddle(head)
        
        ''' Break into two linked list '''
        l2 = middle.next
        middle.next = None

        ''' Merge and Recursion '''
        return self.merge(self.sortList(head), self.sortList(l2))

        # def getMiddle(self, head: Optional[ListNode]):
        #     slow = head
        #     fast = head
        #     while (fast.next is not None and fast.next.next is not None):
        #         slow = slow.next
        #         fast = fast.next.next
            
        #     return slow
        
        # def merge(self, l1, l2):
        #     dummy = ListNode()
        #     cur = dummy

        #     while (l1 is not None and l2 is not None):
        #         if l1.val < l2.val:
        #             cur.next = l1
        #             l1 = l1.next
        #         else:
        #             cur.next = l2
        #             l2 = l2.next
                
        #         cur = cur.next

        #     if l1:
        #         cur.next = l1
            
        #     if l2:
        #         cur.next = l2
            
        #     return dummy.next

    def getMiddle(self, head):
        '''
        找Linked list有兩種寫法
        1. while (fast.next and fast.next.next):
        2. while (fast and fast.next): 

        假設一個linked list是1 -> 2 -> 3 -> 4
        在偶數情況下，第一種會找到2，第二種會找到3
        '''

        slow = fast = head

        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        
        return slow

    def merge(self, l1, l2):
        dummy = ListNode()
        curr = dummy

        '''
        merge兩個linked list不用將dummy.next先指向head
        '''

        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            
            curr = curr.next
        
        if l1:
            curr.next = l1
        if l2:
            curr.next = l2
        
        return dummy.next

