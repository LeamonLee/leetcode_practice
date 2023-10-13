'''
Given an array nums, write a function to move all 0’s to the end of it 
while maintaining the relative order of the non-zero elements.

Example:
Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array. Minimize the total number of operations.
'''
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        '''
        用index紀錄在array中是0的位置，
        然後遍歷整個array，發現不等於0的，就搬到index的位置。

        最後再用一個for迴圈，從index走到底補0。
        '''
        index=0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[index] = nums[i]
                index+=1
        
        for i in range(index, len(nums)):
            nums[i] = 0