class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if len(nums) == 1: return nums[0]
        
        cumSum = 0
        maxSum = float("-inf")  # 這裡初始化成float("-inf")很重要

        for i in range(len(nums)):
            cumSum += nums[i]

            ''' 下面兩個if的順序很重要 '''
            if i > k - 1:
                cumSum -= nums[i-k]

            if i >= k - 1:
                maxSum = max(maxSum, cumSum)
        
        return maxSum / k
