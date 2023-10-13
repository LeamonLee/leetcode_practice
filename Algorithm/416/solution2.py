class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if len(nums) < 2:
            return False

        totalSum = sum(nums)
        if totalSum % 2 != 0:
            return False
        
        targetSum = totalSum // 2

        dp = set()
        dp.add(0)

        # for i in range(len(nums)-1, -1, -1):
        for i in range(len(nums)):
            nextDP = set()
            for t in dp:
                if (t+nums[i]) == targetSum: return True
                nextDP.add(t+nums[i])
                nextDP.add(t)
            
            dp = nextDP
        
        return True if targetSum in dp else False
        