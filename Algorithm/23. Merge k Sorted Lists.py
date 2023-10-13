'''
You are given an array of k linked-lists lists, 
each linked-list is sorted in ascending order.
Merge all the linked-lists into one sorted linked-list and return it.

Example 1:
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6

Example 2:
Input: lists = []
Output: []

Example 3:
Input: lists = [[]]
Output: []
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        q=[]
        for i in range(len(lists)):
            '''
            因為題目有說每個array都是排序過的
            所以先把每個array的第一個元素丟進priority queue(python是用min heap，也就是最小的會被pop出來)
            '''
            if lists[i]:
                heapq.heappush(q, (lists[i].val, i))
                lists[i] = lists[i].next    # 這一步非常重要，因為是linked list，所以要移到下一個node
        
        '''
        記得要先create一個dummy node
        '''
        dummy = ListNode()
        curr=dummy
        while q:
            val, i = heapq.heappop(q)
            curr.next = ListNode(val)
            curr=curr.next

            # 如果list還有的話就一樣把剩下的丟進priority queue
            if lists[i]:
                heapq.heappush(q, (lists[i].val, i))
                lists[i] = lists[i].next
        
        return dummy.next