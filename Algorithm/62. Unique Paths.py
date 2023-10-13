'''
There is a robot on an m x n grid. 
The robot is initially located at the top-left corner (i.e., grid[0][0]). 
The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). 
The robot can only move either down or right at any point in time.

Given the two integers m and n, 
return the number of possible unique paths that the robot can take to reach the bottom-right corner.
The test cases are generated so that the answer will be less than or equal to 2 * 109.

Example 1:
Input: m = 3, n = 7
Output: 28

Example 2:
Input: m = 3, n = 2
Output: 3
Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down
'''

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        ################# Solution1 1維dp ##################
        # dp = [1]*m

        ''' 外層for loop是column，內層是row，所以是由左往右，Column by column看 '''
        # for c in range(1, n):
        #     for r in range(1, m):
        #         dp[r] = dp[r] + dp[r-1]
        
        # return dp[-1]

        ''' 我比較喜歡第二種，用二維矩陣的方式，每個點都去看dp上方和左方總共有多少種方法 '''
        ################# Solution2 2維dp ##################
        dp = [[1 for _ in range(n)] for _ in range(m)]  # 初始化為1，因為每個點本身至少都有1種方法到終點

        ''' 上面這樣initialize就不用再多跑兩次for loop '''
        # First Row
        # for c in range(n):
        #     dp[0][c] = 1

        # # First Column
        # for r in range(m):
        #     dp[r][0] = 1

        ''' 一樣由左往右，Column by column看 '''
        for c in range(1,n):
            for r in range(1,m):
                dp[r][c] = dp[r-1][c] + dp[r][c-1]
        
        return dp[-1][-1]