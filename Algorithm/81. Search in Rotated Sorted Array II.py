'''
There is an integer array nums sorted in non-decreasing order (not necessarily with distinct values).
Before being passed to your function, 
nums is rotated at an unknown pivot index k (0 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). 
For example, [0,1,2,4,4,4,5,6,6,7] might be rotated at pivot index 5 and become [4,5,6,6,7,0,1,2,4,4].
Given the array nums after the rotation and an integer target, return true if target is in nums, or false if it is not in nums.
You must decrease the overall operation steps as much as possible.

Example 1:
Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true

Example 2:
Input: nums = [2,5,6,0,0,1,2], target = 3
Output: false

可以和33題比較
'''

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        '''
        這題關鍵在給定的nums會重複，但33題的nums element不會重複
        '''
        l=0
        r=len(nums)-1

        while l+1<r:
            mid = l + (r-l)//2
            if nums[mid]==target: return True

            '''
            本題關鍵! 判斷mid和l,r是否一樣，如果一樣就把l和r各往左右移動
            其他寫法都和33題一樣
            '''
            if nums[mid]==nums[r]:
                r-=1
            elif nums[mid]==nums[l]:
                l+=1
            elif nums[mid]>nums[l]: # 這裡沒有等於，33有等於
                if target>=nums[l] and target<=nums[mid]:   # 記得要寫等於
                    r=mid
                else:
                    l=mid
            else:
                if target>=nums[mid] and target <= nums[r]: # 記得要寫等於
                    l=mid
                else:
                    r=mid
        
        if nums[l]==target or nums[r]==target:
            return True
        else:
            return False