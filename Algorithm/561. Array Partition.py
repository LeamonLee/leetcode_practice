class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        total=0
        nums.sort()

        for i in range(len(nums)):
            if i % 2 == 0:
                total+=nums[i]
        
        return total