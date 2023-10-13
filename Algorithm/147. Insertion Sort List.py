'''
Given the head of a singly linked list, sort the list using insertion sort, 
and return the sorted list's head.

The steps of the insertion sort algorithm:
Insertion sort iterates, consuming one input element each repetition 
and growing a sorted output list.
At each iteration, insertion sort removes one element from the input data, 
finds the location it belongs within the sorted list and inserts it there.
It repeats until no input elements remain.

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
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return None

        dummy = ListNode()
        dummy.next = head
        curr = head
        
        prevLarge = None
        small = None

        '''
        因為需要讓當前node和下一個node比較，所以需要check curr and curr.next是否同時存在
        '''
        while curr and curr.next:           
            if curr.val <= curr.next.val:   # 如果下一個值比當前自己大，說明正常
                curr = curr.next
            else:                           # 如果當前值比較大，就需要找到重新insert的node，也就是下一個值比當前自己小
                small = curr.next           # 先把要重新insert的node保存起來
                curr.next = curr.next.next  # 這一步很重要，但很容易忘記
                
                prevLarge = dummy           # 從頭遍歷到尾，找到需要插入的地方
                while prevLarge.next.val <= small.val:  # 如果找到prevLarge下一個值大於small的值，就是small可以重新插入的地方
                    prevLarge = prevLarge.next
                
                '''
                prevLarge -> small -> prevLarge.next
                '''
                small.next = prevLarge.next
                prevLarge.next = small
        
        return dummy.next
