'''
Given a 2D matrix matrix, handle multiple queries of the following type:

Calculate the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).

Implement the NumMatrix class:
NumMatrix(int[][] matrix) Initializes the object with the integer matrix matrix.
int sumRegion(int row1, int col1, int row2, int col2) Returns the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).
You must design an algorithm where sumRegion works on O(1) time complexity.

Example 1:
Input
["NumMatrix", "sumRegion", "sumRegion", "sumRegion"]
[[[[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]], [2, 1, 4, 3], [1, 1, 2, 2], [1, 2, 2, 4]]
Output
[null, 8, 11, 12]

Explanation
NumMatrix numMatrix = new NumMatrix([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]);
numMatrix.sumRegion(2, 1, 4, 3); // return 8 (i.e sum of the red rectangle)
numMatrix.sumRegion(1, 1, 2, 2); // return 11 (i.e sum of the green rectangle)
numMatrix.sumRegion(1, 2, 2, 4); // return 12 (i.e sum of the blue rectangle)
'''

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):

        if not matrix or not matrix[0]: return

        # self.matrix = matrix
        self.ROWS=len(matrix)
        self.COLUMNS=len(matrix[0])
        self.dp=[[0 for _ in range(self.COLUMNS+1)] for _ in range(self.ROWS+1)]
        # self.dp=[[0 for _ in range(self.COLUMNS)] for _ in range(self.ROWS)]

        for r in range(self.ROWS):
            for c in range(self.COLUMNS):
                self.dp[r+1][c+1] = self.dp[r][c+1] + self.dp[r+1][c] + matrix[r][c] - self.dp[r][c] 
                
                # if r == 0 and c == 0: 
                #     self.dp[r][c] = matrix[r][c]
                # elif r==0 and c!=0:
                #     self.dp[r][c] = self.dp[r][c-1] + matrix[r][c]
                # elif r!=0 and c==0:
                #     self.dp[r][c] = self.dp[r-1][c] + matrix[r][c]
                # else:
                #     self.dp[r][c] = self.dp[r-1][c] + self.dp[r][c-1] + matrix[r][c] - self.dp[r-1][c-1] 
        
        # print(f"self.ROWS:{self.ROWS}, self.COLUMNS:{self.COLUMNS}")
        # print(f"self.dp:{self.dp}")

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.dp[row2+1][col2+1] - self.dp[row1][col2+1] - self.dp[row2+1][col1] + self.dp[row1][col1]
        # print(f"row1:{row1}, col1:{col1}, row2:{row2}, col2:{col2}")
        # if row2 - row1 == 0 and col2 - col1==0:
        #     print(f"case1: {self.dp[row2][col2]}, {self.matrix[row2][col2]}")
        #     # return self.dp[row2][col2]
        #     return self.matrix[row2][col2]
        # elif row2 - row1 == 0:
        #     print(f"case2: {self.dp[row2][col2] - self.dp[row1][col1-1]}")
        #     if col1 == 0:
        #         return self.dp[row2][col2]
        #     else:
        #         return self.dp[row2][col2] - self.dp[row1][col1-1]
        # elif col2-col1==0:
        #     print(f"case3: {self.dp[row2][col2] - self.dp[row1-1][col1]}")
        #     if row1 == 0:
        #         return self.dp[row2][col2]
        #     else:
        #         return self.dp[row2][col2] - self.dp[row1-1][col1]
        # else:
        #     print(f"case4: {self.dp[row2][col2] - self.dp[row2][col1-1] - self.dp[row1-1][col2] + self.dp[row1-1][col1-1]}")
        #     if row1 == 0 and col1 == 0:
        #         return self.dp[row2][col2]
        #     elif row1 == 0 and row2 == 0:
        #         return self.dp[row2][col2] - self.dp[row1][col1-1]
        #     elif col1 == 0 and col2 == 0:
        #         return self.dp[row2][col2] - self.dp[row1-1][col1]
        #     else:
        #         return self.dp[row2][col2] - self.dp[row2][col1-1] - self.dp[row1-1][col2] + self.dp[row1-1][col1-1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)