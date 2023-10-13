'''
Given an m x n binary matrix filled with 0's and 1's, 
find the largest square containing only 1's and return its area.

Example 1:
Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 4

Example 2:
Input: matrix = [["0","1"],["1","0"]]
Output: 1

Example 3:
Input: matrix = [["0"]]
Output: 0
'''
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])

        res = 0

        dp=[[0]*n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    if i-1 < 0 or j-1 < 0:  # 第一行和第一列都先初始化為1，因為每個點最小都能是一個正方形(自己)
                        dp[i][j]=1
                    else:
                        dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])+1  # 取左上方、上方、左方dp中最小的，只有當這三個點(左上、上、左)的值都一樣時，當前的點的正方形面積才有辦法再增加

                    res = max(res, dp[i][j])
        
        return res*res 