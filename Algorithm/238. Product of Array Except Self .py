'''
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

nums = [1,2,3,4]

res[0] = 1
curr = nums[0]
1        2         3         4
        res[i]
curr
'''

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [0]*len(nums)

        res[0] = 1
        curr = nums[0]
        for i in range(1, len(nums)):           # 從array第二個元素開始往後遍歷
            res[i] = curr
            curr*=nums[i]
        
        curr = nums[-1]
        for i in range(len(nums)-2, -1, -1):    # 從array倒數第二個元素開始往前遍歷
            res[i] *= curr
            curr*=nums[i]
        
        return res