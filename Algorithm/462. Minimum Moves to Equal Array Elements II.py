class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        midIndex = len(nums)//2
        nums.sort()
        mid = nums[midIndex]
        
        # print(f"mid:{mid}")
        numMove = 0
        for num in nums:
            numMove+=abs(num-mid)
        
        return numMove
