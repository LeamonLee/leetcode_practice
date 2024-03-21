'''
Given a positive integer num, return true if num is a perfect square or false otherwise.
A perfect square is an integer that is the square of an integer. In other words, it is the product of some integer with itself.
You must not use any built-in library function, such as sqrt.


Example 1:
Input: num = 16
Output: true
Explanation: We return true because 4 * 4 = 16 and 4 is an integer.

Example 2:
Input: num = 14
Output: false
Explanation: We return false because 3.742 * 3.742 = 14 and 3.742 is not an integer.
'''

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l=1
        # r=num     # 這樣也可以
        r=num//2    # 進一步優化

        while l+1<r:                # 因為要找mid，所以是l+1<r
            mid = (l+r)//2
            if mid*mid==num: return True

            if mid*mid > num:
                r=mid
            else:
                l=mid
        
        if l*l==num: return True
        if r*r==num: return True

        return False