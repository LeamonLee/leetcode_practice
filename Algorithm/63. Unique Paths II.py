'''
You are given an m x n integer array grid. 
There is a robot initially located at the top-left corner (i.e., grid[0][0]). 
The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). 
The robot can only move either down or right at any point in time.

An obstacle and space are marked as 1 or 0 respectively in grid. 
A path that the robot takes cannot include any square that is an obstacle.
Return the number of possible unique paths that the robot can take to reach the bottom-right corner.
The testcases are generated so that the answer will be less than or equal to 2 * 109.

Example 1:
Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
Output: 2
Explanation: There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right

Example 2:
Input: obstacleGrid = [[0,1],[0,0]]
Output: 1
'''

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        
        ''' 注意!!! 這題因為有障礙物，所以不能再將first row和first column初始化成1 '''
        dp = [[0 for _ in range(n)] for _ in range(m)]

        # First Row
        for c in range(n):
            if obstacleGrid[0][c] == 1: break   # 一旦遇到障礙物，後面的都到達不了，所以直接Break
            dp[0][c] = 1

        # First Column
        for r in range(m):
            if obstacleGrid[r][0] == 1: break   # 一旦遇到障礙物，後面的都到達不了，所以直接Break
            dp[r][0] = 1

        ''' 一樣由左往右，Column by column看 '''
        for c in range(1,n):
            for r in range(1,m):
                if obstacleGrid[r][c] == 1: continue

                dp[r][c] = dp[r-1][c] + dp[r][c-1]
        
        return dp[-1][-1]
                