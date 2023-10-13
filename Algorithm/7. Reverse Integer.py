'''
Given a signed 32-bit integer x, return x with its digits reversed. 
If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 
Example 1:
Input: x = 123
Output: 321

Example 2:
Input: x = -123
Output: -321

Example 3:
Input: x = 120
Output: 21
'''
class Solution:
    def reverse(self, x: int) -> int:
        res=0
        isNeg = False
        MAX_INT = 2**31 -1
        MIN_INT = -2**31

        # 統一用正數處理，最後再乘上-1變回來
        if x < 0:
            isNeg = True
            x*=-1
        
        while x != 0:
            digit = x % 10
            newRes = res * 10 + digit
            
            # If reversing x causes the value to go outside the signed 32-bit integer range
            ''' 
            本題關鍵!
            Ex: x=123456789, reverse後變成
            '''
            if newRes // 10 != res or \
                newRes > MAX_INT or \
                newRes < MIN_INT:
                return 0
            
            res = newRes
            
            x//=10 # 對負數會失敗
        
        if isNeg: res*=-1

        return res