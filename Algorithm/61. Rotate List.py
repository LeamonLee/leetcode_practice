'''
Given the head of a linked list, rotate the list to the right by k places.

Example 1:
Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]

Example 2:
Input: head = [0,1,2], k = 4
Output: [2,0,1]
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        ''' 先遍歷一遍看總共有多少個node '''
        totalNodes = 1
        index = head
        while index.next:
            totalNodes +=1
            index = index.next
        
        ''' 這一步很重要，不能少，此時index已經在最後一個node，要連接回第一個Node才能變成一個環 '''
        index.next = head
        
        ''' 
        k % totalNodes目的是有可能k大於totalNodes的數量，造成沒意義的rotate
        Ex: 
        totalNodes=5, k=1, 1%5=1
        totalNodes=5, k=6, 6%5=1

        記得要多減一個1，目的是為了要找到旋轉後最後一個元素(3)，這樣exit for loop後才可以用head.next找到4
        以totalNodes=5, k=2為例，旋轉前最後一個元素是5，旋轉一次後，最後一個元素變成4，旋轉第二次後，最後一個元素變成3。
        這時候要把head.next變回None，因為我們在上一步把它變成一個cycle了。
        '''
        for i in range(totalNodes - (k % totalNodes) - 1):
            head = head.next
        
        ''' 
        Before Rotate: 1,2,3,4,5->1,2...
        After Rotate 1: 5,1,2,3,4->5,1...
        After Rotate 2: 4,5,1,2,3->4,5...
        '''
        # head.val = 3
        # res.val = 4
        res = head.next
        head.next = None

        return res
