'''
Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. If the two linked lists have no intersection at all, return null.
For example, the following two linked lists begin to intersect at node c1:
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headB: return None

        a = headA
        b = headB

        # 如果兩個node有交叉(intersection)，則x+z+y = y+z+x
        # 也就是說，先走headA，走到Null後再換走nodeB。nodeB也一樣
        while a != b:
            a = headB if not a else a.next
            b = headA if not b else b.next
        
        return a    # 隨便return a或b都行