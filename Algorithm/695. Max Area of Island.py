'''
Example 1:
Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
Output: 6
Explanation: The answer is not 11, because the island must be connected 4-directionally.

Example 2:
Input: grid = [[0,0,0,0,0,0,0,0]]
Output: 0
'''

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        maxArea = 0
        res = 0

        def dfs(r,c):
            nonlocal maxArea
            
            if r < 0 or c < 0 or\
                r >= ROWS or c >= COLS or \
                grid[r][c] == 0: return
            
            maxArea +=1
            grid[r][c] = 0
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)
            return


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    maxArea = 0
                    dfs(r,c)
                    res = max(res, maxArea)
        
        return res
