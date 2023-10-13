class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        curLen = 1
        maxLen = 1

        
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                curLen+=1
            else:
                curLen = 1
            
            maxLen = max(maxLen, curLen)
        
        return maxLen