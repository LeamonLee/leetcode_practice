'''
Given an integer array nums, find a 
subarray that has the largest product, and return the product.
The test cases are generated so that the answer will fit in a 32-bit integer.

Example 1:
Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.

Example 2:
Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
'''

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        '''
        由於題目說明是subarray，所以只能是"連續"兩個數的乘積。
        因此可以使用dp來解，每一個數只和前一個數的最大值、最小值有關係
        會用最小值的原因主要是因為有可能有負數，負負得正，因此當前如果也是負數，乘上之前最小值也是負數的話，就有可能變成最大值。
        '''

        maxSum = nums[0]
        minSum = nums[0]
        res=nums[0]

        for i in range(1, len(nums)):
            temp = maxSum
            maxSum = max(max(maxSum*nums[i], minSum*nums[i]), nums[i])
            minSum = min(min(temp*nums[i], minSum*nums[i]), nums[i])

            res = max(res, maxSum)
        
        return res