'''
Given an integer array nums sorted in non-decreasing order, 
remove the duplicates "in-place" such that each unique element appears only once. 
The relative order of the elements should be kept the same. 
Then return the number of unique elements in nums.

Example 1:
Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).

Example 2:
Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).

-

可以和80題做比較
'''

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        '''
        題目要求要in-place，且每個element最多出現1次
        nums已經由小到大排序好
        '''
        '''
        1   1   1   2
            p
            i
    
    ==>
            p
                i
    ==>
            p
                   i
        1   2   1   2
                p
                        i
        '''
        # p去紀錄目前還沒重複數字的index，然後i從1開始
        # 如果nums[i] != nums[p]就把nums[i]放到nums[p]，代表沒重複
        # 

        p = 1
        for i in range(1,len(nums)):
            if nums[i] != nums[p-1]:
                nums[p] = nums[i]
                p+=1
        
        return p

        '''
        1   1   1   2
        p
            i
    
    ==>
        p
                i
    ==>
            p
                   i
        '''
        # p = 0
        # for i in range(1,len(nums)):
        #     if nums[i] != nums[p]:
        #         p+=1
        #         nums[p] = nums[i]
        
        # return p+1