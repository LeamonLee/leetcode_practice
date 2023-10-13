'''
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.
Given an integer n, return the number of distinct solutions to the n-queens puzzle.

Example 1:
Input: n = 4
Output: 2
Explanation: There are two distinct solutions to the 4-queens puzzle as shown.

Example 2:
Input: n = 1
Output: 1

'''
class Solution:
    def totalNQueens(self, n: int) -> int:
        '''
        這題就是每個Queen的位置在同一個row、同一個col、斜對角都不會被碰到其他Queen
        因此每一個row和column都只能擺一個queen

        但這題只需要算有幾種可能就好，所以也不用建boards的資料
        '''
        cols=set()
        posDiog=set()
        negDiog=set()
        res=0

        def backtrack(r):
            nonlocal res
            
            if r == n:
                res+=1
                return

            for c in range(n):
                if c in cols or \
                    r+c in posDiog or \
                    r-c in negDiog:
                    continue
                
                cols.add(c)
                posDiog.add(r+c)
                negDiog.add(r-c)

                backtrack(r+1)

                cols.remove(c)
                posDiog.remove(r+c)
                negDiog.remove(r-c)

        backtrack(0)
        return res