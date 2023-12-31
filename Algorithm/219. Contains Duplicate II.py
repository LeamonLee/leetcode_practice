'''
Given an integer array nums and an integer k, 
return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] 
and abs(i - j) <= k.

Example 1:
Input: nums = [1,2,3,1], k = 3
Output: true

Example 2:
Input: nums = [1,0,1,1], k = 1
Output: true

Example 3:
Input: nums = [1,2,3,1,2,3], k = 2
Output: false
'''

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if not nums or len(nums) < 2: return False
        
        '''
        用一個hashmap邊跑for迴圈邊檢查
        '''


        hashMap = {}    # key是nums的值，value是index
        for i in range(len(nums)):
            if nums[i] in hashMap:
                if i - hashMap[nums[i]] <= k:
                    return True
            hashMap[nums[i]] = i
        
        return False