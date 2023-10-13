'''
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
You must do it in place.

Example 1:
Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]

Example 2:
Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
'''

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        ROWS = len(matrix)
        COLUMNS = len(matrix[0])
        isFirstRowZero = False
        isFirstColumnZero = False

        # Find which row/column has 0
        for r in range(ROWS):
            for c in range(COLUMNS):
                # 第一個ROW和COLUMN如果有0，要單獨額外用變數紀錄，因為最後需要特別處理
                if r == 0:
                    if matrix[0][c] == 0:
                        isFirstRowZero = True
                if c == 0:
                    if matrix[r][0] == 0:
                        isFirstColumnZero = True
                
                # 如果有0就把所屬的第一個row和第一個column變成0
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    matrix[r][0] = 0
        
        # Iterate through First ROW and find which column has 0
        # 如果哪一個column有0，就把該column全步變成0
        for c in range(1, COLUMNS):
            if matrix[0][c] == 0:
                for r in range(1, ROWS):
                    matrix[r][c] = 0
        
        # Iterate through First COLUMN and find which row has 0
        # 如果哪一個row有0，就把該row全步變成0
        for r in range(1, ROWS):
            if matrix[r][0] == 0:
                for c in range(1, COLUMNS):
                    matrix[r][c] = 0
        
        # 如果第一個row有0，就把第一個row全部變成0
        if isFirstRowZero:
            for c in range(COLUMNS):
                matrix[0][c] = 0
        
        # 如果第一個column有0，就把第一個column全部變成0
        if isFirstColumnZero:
            for r in range(ROWS):
                matrix[r][0] = 0