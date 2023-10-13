'''
Given a sorted array of distinct integers and a target value, 
return the index if the target is found. 
If not, return the index where it would be if it were inserted in order.
You must write an algorithm with O(log n) runtime complexity.


Example 1:
Input: nums = [1,3,5,6], target = 5
Output: 2

Example 2:
Input: nums = [1,3,5,6], target = 2
Output: 1

Example 3:
Input: nums = [1,3,5,6], target = 7
Output: 4

Example 4:
Input: nums = [1,3,5,6], target = 0
Output: 0
'''

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left=0
        right=len(nums)-1

        '''
        使用二分搜索法
        '''

        while(left+1 < right):
            mid = left + (right - left) // 2
            # mid = (right + left) // 2               # 測試過和上面寫法醫樣都可以work

            if target == nums[mid]: # 有找到(Example1)，直接返回該index
                return mid
            
            if target > nums[mid]:
                left = mid
            else:
                right = mid
        
        if target <= nums[left]:    # 沒找到且比數組中的數字都小(Example 4)
            return left
        
        elif target > nums[left] and target <= nums[right]: # 沒找到且介於數組中最小值和最大值的範圍(Example2)的
            return right
        
        else:   # 沒找到且比數組中的數字都大(Example3)
            return len(nums)    # 直接放在數組最後面