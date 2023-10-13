'''
Given the head of a linked list and a value x, 
partition it such that all nodes less than x come before nodes greater than or equal to x.
You should preserve the original relative order of the nodes in each of the two partitions.


Example 1:
Input: head = [1,4,3,2,5,2], x = 3
Output: [1,2,2,4,3,5]

Example 2:
Input: head = [2,1], x = 2
Output: [1,2]
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        '''
        這題就是給一個x值假設是3，
        要把小於x的照原本的相對順序放左邊，然後把大於x的照相對順序放右邊
        最後再串接起來
        所以要建立兩個Linked List，一邊放小於的，一邊放大於的，最後再串接起來
        '''
        dummy1 = ListNode()
        curr1 = dummy1
        dummy2 = ListNode()
        curr2 = dummy2

        while head:
            temp = ListNode(val=head.val)
            if head.val < x:
                curr1.next = temp
                curr1 = curr1.next
            else:
                curr2.next = temp
                curr2 = curr2.next
            
            head = head.next
        
        # 最後要串接起來
        curr1.next = dummy2.next
        return dummy1.next