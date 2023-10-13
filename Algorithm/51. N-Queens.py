'''
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.
Given an integer n, return all distinct solutions to the n-queens puzzle. 
You may return the answer in any order.
Each solution contains a distinct board configuration of the n-queens' placement, 
where 'Q' and '.' both indicate a queen and an empty space, respectively.


Example 1:
Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above

Example 2:
Input: n = 1
Output: [["Q"]]
'''


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        '''
        這題就是每個Queen的位置在同一個row、同一個col、斜對角都不會被碰到其他Queen
        因此每一個row和column都只能擺一個queen
        '''
        cols=set()
        posDiog = set() # r+c would be the same Ex: (0,3), (1,2), (2,1), (3,0)
        negDiog = set() # r-c would be the same Ex: (0,0), (1,1), (2,2), (3,3)

        boards = [['.']*n for _ in range(n)]
        res=[]

        def backtrack(r):
            # 代表最後一個row已經跑完了
            if r == n:
                res.append(["".join(board) for board in boards])
                return
            
            # 從第一個column開始遍歷
            for c in range(n):
                if c in cols or \
                    r+c in posDiog or \
                    r-c in negDiog:
                    continue
                
                cols.add(c)
                posDiog.add(r+c)
                negDiog.add(r-c)
                boards[r][c] = 'Q'

                # 因為每一個row只能擺一個queen，所以這個row和column變成Queen之後，就可以往下一個row移動了
                backtrack(r+1)

                cols.remove(c)
                posDiog.remove(r+c)
                negDiog.remove(r-c)
                boards[r][c] = '.'
        
        backtrack(0)
        return res

