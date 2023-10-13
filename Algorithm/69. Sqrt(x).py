'''
Given a non-negative integer x, return the square root of x rounded down to the nearest integer. 
The returned integer should be non-negative as well.
You must not use any built-in exponent function or operator.
For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.

Example 1:
Input: x = 4
Output: 2
Explanation: The square root of 4 is 2, so we return 2.

Example 2:
Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.
'''
class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0: return 0
        
        ''' 解題思路: 用類似二分搜尋法，將1~x之間的數字都平方，看是否找到x或近似於x '''
        start = 1
        end = x
        while start + 1 < end:
            mid = start + (end-start)//2
            num = mid*mid
            if num == x:
                return mid
            elif num < x:       # 平方後仍然小於target，所以可以把start變成mid，縮小搜尋範圍
                start = mid
            elif num > x:       # 平方後大於target了，所以把end變成mid，縮小搜尋範圍
                end = mid
        
        ''' 如果上面都找不到，就有可能是end或start '''
        if end*end < x:
            return end
        else:
            return start