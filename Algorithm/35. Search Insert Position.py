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
        '''
        這題nums已經排序好，且不重複(distinct)
        '''
        l=0
        r=len(nums)-1

        '''
        使用二分搜索法
        '''

        while(l+1 < r):      # 因為要找mid，所以是l+1<r
            mid = l + (r - l) // 2
            # mid = (r + l) // 2               # 測試過和上面寫法一樣都可以work

            if target == nums[mid]: # 有找到(Example1)，直接返回該index
                return mid
            
            if target > nums[mid]:
                l = mid
            else:
                r = mid
        
        if target <= nums[l]:    # 沒找到且比數組中的數字都小(Example 4)
            return l
        
        elif target > nums[l] and target <= nums[r]: # 沒找到且介於數組中最小值和最大值的範圍(Example2)的
            return r
        
        else:   # 沒找到且比數組中的數字都大(Example3)
            return len(nums)    # 直接放在數組最後面