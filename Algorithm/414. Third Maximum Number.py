'''
Given an integer array nums, return the third distinct maximum number in this array. 
If the third maximum does not exist, return the maximum number.

Example 1:
Input: nums = [3,2,1]
Output: 1
Explanation:
The first distinct maximum is 3.
The second distinct maximum is 2.
The third distinct maximum is 1.

Example 2:
Input: nums = [1,2]
Output: 2
Explanation:
The first distinct maximum is 2.
The second distinct maximum is 1.
The third distinct maximum does not exist, so the maximum (2) is returned instead.

Example 3:
Input: nums = [2,2,3,1]
Output: 1
Explanation:
The first distinct maximum is 3.
The second distinct maximum is 2 (both 2's are counted together since they have the same value).
The third distinct maximum is 1.
'''

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        max1=float("-inf")
        max2=float("-inf")
        max3=float("-inf")

        for num in nums:
            # 這個條件是關鍵
            if num==max1 or num==max2 or num==max3: continue
            if num > max1:
                max3=max2
                max2=max1
                max1=num
            elif num > max2:
                max3=max2
                max2=num
            elif num > max3:
                max3=num
        
        print(f"max3:{max3}")
        return max1 if max3==float("-inf") else max3