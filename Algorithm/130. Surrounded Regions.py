'''
Given an m x n matrix board containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'.
A region is captured by flipping all 'O's into 'X's in that surrounded region.

Example 1:
Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
Explanation: Notice that an 'O' should not be flipped if:
- It is on the border, or
- It is adjacent to an 'O' that should not be flipped.
The bottom 'O' is on the border, so it is not flipped.
The other three 'O' form a surrounded region, so they are flipped.

Example 2:
Input: board = [["X"]]
Output: [["X"]]
'''

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        '''
        解題思路: 
        1. 先從四個邊(First Row/Column, Last Row/Column)判斷是否有O的，有的就繼續往裡面跑，並標記為^
        2. 最後重新遍歷整個board，如果是^就變回O，如果是O就變成X
        '''

        ROWS = len(board)
        COLS = len(board[0])

        def helper(r,c):
            # 如果越界了，或是走到X，就return
            if r<0 or r>=ROWS or\
                c<0 or c>=COLS or\
                board[r][c] != 'O':
                return
            
            # 會走到這，代表這個位子是O，可以變成^
            board[r][c] = '^'
            helper(r-1,c)
            helper(r,c-1)
            helper(r+1,c)
            helper(r,c+1)

        ''' Iterate through First/Last Column '''
        for r in range(ROWS):
            if board[r][0] == 'O': 
                helper(r, 0)
            if board[r][-1] == 'O':
                helper(r, COLS-1)

        ''' Iterate through First/Last Row '''
        for c in range(COLS):
            if board[0][c] == 'O':
                helper(0,c)
            if board[-1][c] == 'O':
                helper(ROWS-1,c)

        ''' Iterate through the entire matrix '''
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                if board[r][c] == '^':
                    board[r][c] = 'O'
