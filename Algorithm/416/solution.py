class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if len(nums) < 2:
            return False

        totalSum = 0
        for num in nums:
            totalSum += num
        
        print(f"nums:{nums}, totalSum:{totalSum}")
        if totalSum % 2 != 0:
            return False
        
        targetSum = totalSum // 2
        print(f"targetSum:{targetSum}")

        dp = [True] + [False] * targetSum

        '''
        [1,5,11,5] target = 22/2=11
        [1,2,3,5]  target = 11/2=5.5

        dp[11] = dp[11] || dp[10]
        dp[10] = dp[10] || dp[9]
        ...
        dp[1] = dp[1] || dp[0]
        dp[1] = True

        dp[11] = dp[11] || dp[6]
        ...
        dp[6] = True
        dp[5] = True

        dp[11] = dp[11] || dp[0]
        ...
        dp[11]=True

        dp[11] = dp[11] || dp[6]
        dp[10] = dp[10] || dp[5]
        ...
        dp[10]=True
        '''

        for num in nums:
            for target in range(targetSum, -1, -1):
                if target - num >= 0:
                    dp[target] |= dp[target-num]
        
        return dp[targetSum]
        