'''
Given an array of integers nums sorted in non-decreasing order, 
find the starting and ending position of a given target value.
If target is not found in the array, return [-1, -1].
You must write an algorithm with O(log n) runtime complexity.


Example 1:
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

Example 3:
Input: nums = [], target = 0
Output: [-1,-1]

-
'''
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums: return [-1, -1]

        '''
        變形的二分搜索法
        這一題就是要找到一個array最左邊和最右邊都等於target的index
        '''

        def findLeft():
            l = 0
            r = len(nums) - 1
            while l + 1 < r:
                mid = l + (r-l) // 2

                # 這邊的判斷式是關鍵
                # 因為是找最左邊的index，
                # 所以即使mid已經等於target了，還是要將mid賦值給right，因為要盡量往最左邊去找
                if target <= nums[mid]:
                    r = mid
                else:
                    l = mid

            if nums[l] == target:
                return l
            elif nums[r] == target:
                return r
            else:
                return - 1
        
        def findRight():
            l = 0
            r = len(nums) - 1
            
            while l + 1 < r:
                mid = l + (r-l)//2

                # 這邊的判斷式是關鍵
                if target >= nums[mid]:
                    l = mid
                else:
                    r = mid
            
            if nums[r] == target:
                return r
            elif nums[l] == target:
                return l 
            else:
                return -1
        
        firstIndex = findLeft()
        if firstIndex == -1:
            return [-1, -1]
        
        lastIndex = findRight()
        return [firstIndex, lastIndex]