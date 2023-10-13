class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        '''
        nums:  1 3  5  4  7
        dp     1 2  3  3  4
        counts 1 1  1  1  2

        nums:  2 2  2  2  2
        dp     1 1  1  1  1
        counts 1 1  1  1  1
        '''
        dp = [1] * len(nums)            # 以index i結束最長的increasing subsequence是多少
        counts = [0] * len(nums)        # 以index i結束有幾種increasing subsequence

        dp[0] = 1
        counts[0] = 1

        maxDP = 1
        res = 0
        for i in range(1, len(nums)):
            maxCount = 1
            for j in range(i):
                if nums[j] < nums[i]:
                    if dp[j] + 1 > dp[i]:
                        dp[i]+=1
                        # counts[i] = counts[j]
                        maxCount = counts[j]
                    elif dp[j]+1 == dp[i]:
                        # counts[i]+=1
                        maxCount+=counts[j]
            
            counts[i] = maxCount
            maxDP = max(maxDP, dp[i])
        
        for i in range(len(nums)):
            if dp[i] == maxDP:
                res+=counts[i]
        
        print(f"dp:{dp}")
        print(f"counts:{counts}")
        return res
                        
                
                    