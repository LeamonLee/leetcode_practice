class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        top = 0
        down = len(matrix) -1 

        # Exchange the rows elements between top and down
        while top < down:
            matrix[top], matrix[down] = matrix[down], matrix[top]

            top+=1
            down-=1
        
        # Exchange the diagonal elements
        for r in range(len(matrix)):
            for c in range(r+1, len(matrix[0])):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c] 