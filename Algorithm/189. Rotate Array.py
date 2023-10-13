'''
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

Example 1:
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]

Example 2:
Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
'''

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        '''
        這一題就是要記得解題技巧:
        三次翻转：
        1. 整个数组翻转
        2. 前k 个数字翻转
        3. 后n-k 个数字翻转
        '''

        def reverse(startIdx, endIdx):
            while startIdx < endIdx:
                nums[startIdx], nums[endIdx] = nums[endIdx], nums[startIdx]
                startIdx+=1
                endIdx-=1
        
        k %= len(nums)  # 這一步很重要!因為k有可能大於nums的長度，假設k=10，nums長度等於7，這樣k=10和k=3的旋轉結果是一樣的
        reverse(0, len(nums)-1)
        reverse(0, k-1)
        reverse(k, len(nums)-1)

        return nums