'''
Given a m x n grid filled with non-negative numbers, 
find a path from top left to bottom right, 
which minimizes the sum of all numbers along its path.
Note: You can only move either down or right at any point in time.

Example 1:
Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
Output: 7
Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.

Example 2:
Input: grid = [[1,2,3],[4,5,6]]
Output: 12
'''

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        '''由上往下，由左往右去計算path sum '''
        
        # Iterate Columns
        for c in range(1, n):   # 注意從1開始
            # First row
            grid[0][c] = grid[0][c] + grid[0][c-1]  # First row(最上面的)，先把左右總和加起來
        
        # Iterate Rows
        for r in range(1, m):   # 注意從1開始
            # First Col
            grid[r][0] = grid[r][0] + grid[r-1][0]  # First column(最左邊的)，先把上下總和加起來
            
            # 從(1,1)開始，每個row在加的時候，也把column方向的給加完
            for c in range(1, n):
                grid[r][c] = grid[r][c] + min(grid[r-1][c], grid[r][c-1])   # (1,1)之後每個點，都去看是從左邊走來比較小，還是上面比較小
        
        return grid[-1][-1]