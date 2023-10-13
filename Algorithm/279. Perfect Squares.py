'''
Given an integer n, return the least number of perfect square numbers that sum to n.
A perfect square is an integer that is the square of an integer; 
in other words, it is the product of some integer with itself. 
For example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are not.


Example 1:
Input: n = 12
Output: 3
Explanation: 12 = 4 + 4 + 4.

Example 2:
Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.
'''
class Solution:
    def numSquares(self, n: int) -> int:
        '''
        要用dp
        '''
        dp = [float("inf")] * (n+1)     # 一定要用float("inf")初始化
        dp[0] = 0

        # Ex: i=4, j=2, num=4-4=0       dp[4] = dp[0]+1     = 1
        # Ex: i=13, j=3, num=13-9=4     dp[13] = dp[4]+1    = 2
        for i in range(1, n+1): # 記得從1開始，外層for迴圈是在算每個dp數字最少可以用幾個square number算出總合
            for j in range(i+1):            # 內層for迴圈只跑到外層for迴圈的數字而已
                num = i - (j*j)
                if num < 0:
                    break
                dp[i] = min(dp[i], dp[num]+1)

                # if num >= 0 and dp[num] != float("inf"):  # 這個判斷式會超時，用上面那個不會
                #     dp[i] = min(dp[i], dp[num]+1)
        
        # print(f"dp:{dp}")
        return dp[-1]