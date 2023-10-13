'''
Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.
The integer division should truncate toward zero, which means losing its fractional part. 
For example, 8.345 would be truncated to 8, and -2.7335 would be truncated to -2.
Return the quotient after dividing dividend by divisor.
Note: Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231, 231 − 1]. 
For this problem, if the quotient is strictly greater than 231 - 1, then return 231 - 1, and if the quotient is strictly less than -231, then return -231.

Example 1:
Input: dividend = 10, divisor = 3
Output: 3
Explanation: 10/3 = 3.33333.. which is truncated to 3.

Example 2:
Input: dividend = 7, divisor = -3
Output: -2
Explanation: 7/-3 = -2.33333.. which is truncated to -2.
'''
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        MAX_INTEGER = (2**31)-1
        
        '''
        都先使用正整數來操作
        所以用sign來記錄是正數還負數，如果是負數最後再乘回來
        '''
        sign=1
        if (dividend>=0 and divisor<0) or \
            (dividend<0 and divisor>=0):
            sign=-1
        
        '''
        都先使用正整數來操作
        '''
        dividend = abs(dividend)
        divisor = abs(divisor)
        quotient = 0
        # Ex: dividend=19, divisor=3
        while dividend >= divisor:
            mul=1
            # tmp=divisor*mul # Initial value = 3*1
            # 19 = 3*2^2+3*2^1 => quotient=6=2^2+2^1，2^2和2^1就是mul
            while dividend >= divisor*(mul<<1):
                mul<<=1
                
            dividend -= divisor*mul
            quotient+=mul
        
        quotient*=sign
        if quotient>=MAX_INTEGER:
            return MAX_INTEGER
        return quotient

