'''
Given an integer array nums, return the length of the longest strictly increasing 
subsequence.

Example 1:
Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

Example 2:
Input: nums = [0,1,0,3,2,3]
Output: 4

Example 3:
Input: nums = [7,7,7,7,7,7,7]
Output: 1
'''

from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp=[1]*len(nums)
        dpMax=1

        
        # dp[0]一定等於1，因此從1開始遍歷
        # for i in range(1, len(nums)):
        #     for j in range(i):
        #         if nums[j]<nums[i]:
        #             if dp[j] + 1 > dp[i]:
        #                 dp[i]+=1
            
        #     dpMax = max(dpMax, dp[i])
        
        # return dpMax

        for i in range(1, len(nums)):
            tmax=1
            for j in range(i):
                if nums[j]<nums[i]:
                    tmax = max(tmax, dp[j]+1)
            
            dp[i] = tmax
        
        return max(dp)
    
        

if __name__ == "__main__":
    s = Solution()
    # nums=[10,9,2,5,3,7,101,18]
    # nums=[0,1,0,3,2,3]
    nums=[7,7,7,7,7,7,7]

    result = s.lengthOfLIS(nums)
    print(f"result:{result}")