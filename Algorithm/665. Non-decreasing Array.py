'''
Given an array nums with n integers, 
your task is to check if it could become non-decreasing by modifying at most one element.
We define an array is non-decreasing if nums[i] <= nums[i + 1] holds for every i (0-based) 
such that (0 <= i <= n - 2).

Example 1:
Input: nums = [4,2,3]
Output: true
Explanation: You could modify the first 4 to 1 to get a non-decreasing array.

Example 2:
Input: nums = [4,2,1]
Output: false
Explanation: You cannot get a non-decreasing array by modifying at most one element.
'''

class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        isChanged=False

        for i in range(len(nums)-1):
            if nums[i]<=nums[i+1]: continue

            if isChanged: return False

            # 如果下一個比當前的小，但下一個比前一個還大
            #    i i+1
            # [3,5,4]
            # or
            # 記得要處理i=0的情況，否則會out of bound
            #  i i+1
            # [5,4]
            if i==0 or nums[i+1] >= nums[i-1]:
                nums[i] = nums[i+1]     # [3,4,4]
            
            # 如果下一個比當前的小，也比前一個還小
            else:
                #    i i+1
                # [3,4,2]
                nums[i+1] = nums[i]     # [3,4,4]
            isChanged=True
        
        return True