'''
Given an array of positive integers nums and a positive integer target, 
return the minimal length of a subarray 
whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.


Example 1:
Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.

Example 2:
Input: target = 4, nums = [1,4,4]
Output: 1

Example 3:
Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0
'''

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        '''
        解題思路: 用sliding window
        首先l=0，r不斷往右遞增，直到出現總和 >= target，
        接著慢慢縮小window大小(l+=1)，直到總和 < target
        '''
        res = float("inf")
        l = 0
        total = 0

        for r in range(len(nums)):
            total+=nums[r]

            while l<=r and total >= target:
                res = min(r-l+1, res)   # 計算window的長度
                total-=nums[l]
                l+=1
        
        return 0 if res == float("inf") else res