'''
According to Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

The board is made up of an m x n grid of cells, where each cell has an initial state: live (represented by a 1) or dead (represented by a 0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population.
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously. Given the current state of the m x n grid board, return the next state.

Example 1:
Input: board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
Output: [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]

Example 2:
Input: board = [[1,1],[1,0]]
Output: [[1,1],[1,1]]
'''

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        def helper(i,j):
            count=0
            for r in range(max(0,i-1), min(len(board), i+2)):
                for c in range(max(0, j-1), min(len(board[0]), j+2)):
                    if i==r and j==c: continue
                    if board[r][c] & 1: count+=1
            
            return count

        for r in range(len(board)):
            for c in range(len(board[0])):
                neiCount = helper(r,c)
                if board[r][c]==1:
                    if neiCount==2 or neiCount==3:
                        board[r][c] += 2
                elif board[r][c]==0:
                    if neiCount==3:
                        board[r][c] += 2
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                board[r][c] >>= 1
