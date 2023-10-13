'''
You are given row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0 represents water.
Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).
The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island. One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

Example 1:
Input: grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
Output: 16
Explanation: The perimeter is the 16 yellow stripes in the image above.

Example 2:
Input: grid = [[1]]
Output: 4

Example 3:
Input: grid = [[1,0]]
Output: 4
'''
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        res=0

        '''
        思路: 由於是從左往右，從上往下遍歷下來，
        因此只需要去看左邊和上面的element即可。
        每次看到1都先加4(因為一個正方形有四個邊)，
        接著看左邊和上面的點，如果也是1就減2。
        '''

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    res+=4
                
                    # 如果上面也是 1 的話
                    if r > 0 and grid[r-1][c] == 1:
                        res-=2
                    
                    # 如果左邊也是 1 的話
                    if c > 0 and grid[r][c-1] == 1:
                        res-=2
        
        return res