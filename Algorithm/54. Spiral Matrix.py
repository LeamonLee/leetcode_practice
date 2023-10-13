'''
Given an m x n matrix, return all elements of the matrix in spiral order.

Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

Example 2:
Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
'''

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix: return []

        res = []
        rowBegin = 0
        rowEnd = len(matrix)
        colBegin = 0
        colEnd = len(matrix[0])

        while rowBegin < rowEnd and colBegin < colEnd:
            # print(f"rowBegin:{rowBegin}, rowEnd:{rowEnd}, colBegin:{colBegin}, colEnd:{colEnd}")
            ''' Left -> Right '''
            for c in range(colBegin, colEnd):
                res.append(matrix[rowBegin][c])
            
            # 因為第一個row跑完了，接著要往下走
            rowBegin +=1
            
            ''' Up -> Down '''
            # print(f"rowBegin:{rowBegin}, rowEnd:{rowEnd}")
            for r in range(rowBegin, rowEnd):
                res.append(matrix[r][colEnd-1])
            
            # 因為接著要往左邊走
            colEnd -=1

            # 往回走時要再多判斷
            if rowBegin < rowEnd:
                ''' Right -> Left '''
                for c in range(colEnd-1, colBegin-1, -1):
                    res.append(matrix[rowEnd-1][c])
                rowEnd-=1

            # 往回走時要再多判斷
            if colBegin < colEnd:
                ''' Down -> Up '''
                for r in range(rowEnd-1, rowBegin-1, -1):
                    res.append(matrix[r][colBegin])
                colBegin+=1
        
        return res