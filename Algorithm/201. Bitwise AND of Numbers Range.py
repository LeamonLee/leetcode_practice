'''
Given two integers left and right that represent the range [left, right], return the bitwise AND of all numbers in this range, inclusive.

Example 1:
Input: left = 5, right = 7
Output: 4

Example 2:
Input: left = 0, right = 0
Output: 0

Example 3:
Input: left = 1, right = 2147483647
Output: 0
'''

class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        offset = 0
        while left != right:
            left >>= 1
            right >>= 1
            offset +=1
        
        return left << offset