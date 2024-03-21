'''
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
There is only one repeated number in nums, return this repeated number.
You must solve the problem without modifying the array nums and uses only constant extra space.

Example 1:
Input: nums = [1,3,4,2,2]
Output: 2

Example 2:
Input: nums = [3,1,3,4,2]
Output: 3
'''
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        '''
        使用Floyed算法
        每個array element的index都會指向另一個array element
        所以如果有duplicate number的話，會有兩個element指向同一個element，形成一個環，
        因此第一步使用快慢指針
        '''
        slow = fast = 0

        while True:
            fast = nums[nums[fast]]
            slow = nums[slow]
            if slow == fast: break
        
        ''' 本題關鍵: 將fast重新指向0的位置 '''
        fast = 0
        while True:
            fast = nums[fast]
            slow = nums[slow]
            if slow == fast: break

        return slow