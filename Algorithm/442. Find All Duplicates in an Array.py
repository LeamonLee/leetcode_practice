'''
Given an integer array nums of length n where all the integers of nums are in the range [1, n] 
and each integer appears once or twice, return an array of all the integers that appears twice.
You must write an algorithm that runs in O(n) time and uses only constant extra space.


Example 1:
Input: nums = [4,3,2,7,8,2,3,1]
Output: [2,3]

Example 2:
Input: nums = [1,1,2]
Output: [1]

Example 3:
Input: nums = [1]
Output: []
'''
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res=[]
        for i in range(len(nums)):
            index = abs(nums[i]) - 1    # 加絕對值是因為有可能之前已經變成負數過
            if nums[index] < 0:         # 如果是負數，代表之前已經出現過
                res.append(abs(nums[i]))
            else:                       # 如果是正數，代表之前沒出現過，就變成負數做記號
                nums[index] = -nums[index]
        
        return res