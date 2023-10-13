'''
Given an array nums with n objects colored red, white, or blue, 
sort them in-place so that objects of the same color are adjacent, 
with the colors in the order red, white, and blue.
We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
You must solve this problem without using the library's sort function.


Example 1:
Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

Example 2:
Input: nums = [2,0,1]
Output: [0,1,2]
'''

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.

        將0,1,2由小到大排序好，且不能使用built-in sort
        """
        p0 = 0          # 紀錄0的位置
        i = 0
        p2 = len(nums) - 1  # 紀錄2的位置


        '''
        2,0,2,1,1,0
        p0        p2
        i
        
        0,0,2,1,1,2
        p0
          i
                p2
        
        0,0,2,1,1,2
          p0
            i
                p2
        
        0,0,1,1,2,2
          p0 
              i
              p2  
        '''

        while i <= p2:   # 注意這裡遍歷到p2就好，且是<=，因為要遍歷到array的最後一個item
            if nums[i] == 0:
                nums[i], nums[p0] = nums[p0], nums[i]
                p0+=1
                i+=1
            elif nums[i] == 1:
                i+=1
            elif nums[i] == 2:
                nums[i], nums[p2] = nums[p2], nums[i]
                p2-=1
        
