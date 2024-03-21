'''
Given an integer n, break it into the sum of k positive integers, where k >= 2, and maximize the product of those integers.
Return the maximum product you can get.

Example 1:
Input: n = 2
Output: 1
Explanation: 2 = 1 + 1, 1 × 1 = 1.

Example 2:
Input: n = 10
Output: 36
Explanation: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36.
'''

class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0] * (n+1)
        dp[1]=1
        
        for i in range(2, n+1):
            for j in range(1, i):
                '''
                Ex: 
                i=7, j=3,
                7 => 3*4=12
                3 => 1*2=2  or 3 itself
                4 => 2*2=4  or 4 itself
                但是3去拆分成1*2的話會得到2，如果3本身不拆的話就是3，
                所以每次都要去比較拆與不拆誰比較大。
                 
                '''
                dp[i] = max(dp[i], max(j, dp[j]) * max((i-j), dp[i-j]))
        
        return dp[-1]