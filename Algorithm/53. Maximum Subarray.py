'''
Given an integer array nums, 
find the subarray with the largest sum, and return its sum.

Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.

Example 2:
Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.

Example 3:
Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.

'''
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        '''
        Subarray : [1,2],[1,2,3] - is continous and maintains relative order of elements
        Subsequence: [1,2,4] - is not continous but maintains relative order of elements
        Subset: [1,3,2] - is not continous and does not maintain relative order of elements
        '''
        dp = [0 for _ in range(len(nums))]  # 每個dp element代表，走到nums array的第幾個index時的largest sum是多少
        dp[0]=nums[0]   # 第一個element只有自己，所以直接填上即可
        res=dp[0]

        for i in range(1, len(nums)):   # 從1開始，因為0已經填過
            dp[i] = nums[i] + (dp[i-1] if dp[i-1]>0 else 0) # 如果上一個數>0才加進來
            res = max(res, dp[i])

        # print(f"dp:{dp}")
        return res