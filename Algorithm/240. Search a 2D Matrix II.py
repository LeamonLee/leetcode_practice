'''
Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. 
This matrix has the following properties:
Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.

Example 1:
Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5
Output: true

Example 2:
Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 20
Output: false
'''
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        '''
        由於矩陣是有排序過的，所以下一列會比當前這一列的element都大，且越往右邊越大。
        此題可從每一列的最右邊開始找，如果target比當前element大，則往下一列找，反之往左邊找。
        '''
        if not matrix or not matrix[0]: return False
        ROWS = len(matrix)
        COLUMNS = len(matrix[0])
        r = 0
        c = COLUMNS - 1

        while c >=0 and r <= ROWS-1:
            num = matrix[r][c]
            if target == num: return True

            if target < num:
                c-=1
            else:
                r+=1
        
        return False