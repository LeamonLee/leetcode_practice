'''
You are given an integer array nums and an integer k. You want to find a subsequence of nums of length k that has the largest sum.
Return any such subsequence as an integer array of length k.
A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.


Example 1:
Input: nums = [2,1,3,3], k = 2
Output: [3,3]
Explanation:
The subsequence has the largest sum of 3 + 3 = 6.

Example 2:
Input: nums = [-1,-2,3,4], k = 3
Output: [-1,3,4]
Explanation: 
The subsequence has the largest sum of -1 + 3 + 4 = 6.

Example 3:
Input: nums = [3,4,3,3], k = 2
Output: [3,4]
Explanation:
The subsequence has the largest sum of 3 + 4 = 7. 
Another possible subsequence is [4, 3].
'''


import heapq

class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        q = []
        
        # python的priority queue是用min heap實作，每次pop會將最小的元素pop出來
        for i in range(len(nums)):
            heapq.heappush(q, (nums[i], i))

            # 如果數量大於k了，就pop出來，這樣可以確保priority queue裡面always只有k個element，且最後只留最大的k個element
            if len(q) > k:
                heapq.heappop(q)
        
        hashset=set()
        while q:
            hashset.add(heapq.heappop(q)[1])
        
        res=[]
        for i in range(len(nums)):
            if i in hashset:
                res.append(nums[i])
        
        return res