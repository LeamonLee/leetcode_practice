'''
A peak element is an element that is strictly greater than its neighbors.
Given a 0-indexed integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.
You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.
You must write an algorithm that runs in O(log n) time.

Example 1:
Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.

Example 2:
Input: nums = [1,2,1,3,5,6,4]
Output: 5
Explanation: Your function can return either index number 1 where the peak element is 2, or index number 5 where the peak element is 6.
'''

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        '''
        回傳peak element的array index
        使用Binary Search(二分搜尋法)
        '''
        l = 0
        r=len(nums)-1
        while l+1<r:                    # 因為要找mid，所以會是l+1<r
            mid = l + (r-l)//2
            '''
            拿到mid點後會有兩種情況:
            1. nums[mid] > nums[mid+1] 說明是一個往右下的斜線，所以peak會在左半邊，因為左邊(mid)比右邊(mid+1)大
            2. nums[mid] <= nums[mid+1] 說明是一個往右上的斜線，且peak點就在右半邊
            '''
            if nums[mid] > nums[mid+1]: # peak在左半邊
                r = mid
            else:                       # peak在右半邊
                l = mid
        
        # 最後l和r會在相鄰的位置
        if nums[l]>nums[r]:
            return l
        else:
            return r