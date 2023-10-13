'''
You are given an m x n integer matrix matrix with the following two properties:
Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

Example 1:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

Example 2:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false
'''

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        '''
        每一列都已經由小到大排序好，且下一個row一定比上一個row大
        時間複雜度必須在O(log(m * n))
        關鍵: 使用二分搜尋法，將2D矩陣攤平成1D陣列來看
        '''
        if not matrix or len(matrix) == 0: return False
        if not matrix[0] or len(matrix[0]) == 0: return False

        ROWS = len(matrix)
        COLUMNS = len(matrix[0])
        start = 0
        end = (ROWS * COLUMNS) - 1

        while start + 1 < end:
            mid = start + (end-start)//2

            '''
            本題關鍵! 要把mid位置轉成2D矩陣所在的row和column
            '''
            # 假設m=5, n=5, mid=13(如果是0 based，其實是第14個)
            # 代表在第三個row(row=2, column=3)
            row = mid//COLUMNS
            column = mid % COLUMNS

            if matrix[row][column] == target: return True

            if matrix[row][column] < target:
                start = mid
            else:
                end = mid
        
        '''
        和一般二分搜索法一樣，如果上面while loop都沒有找到
        就看看start index和end index
        '''
        # print(f"end:{end}, end//COLUMNS:{end//COLUMNS}, end%COLUMNS:{end%COLUMNS}")
        if matrix[start//COLUMNS][start % COLUMNS] == target:
            return True
        elif matrix[end//COLUMNS][end % COLUMNS] == target:
            return True
        else:
            return False