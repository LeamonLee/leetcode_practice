class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dctDiff = {}

        for idx, num in enumerate(nums):
            if num not in dctDiff.keys():
                dctDiff[target-num] = idx
            else:
                return [dctDiff[num], idx]