class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        columns = len(board[0])
        visited = set()
        
        for r in range(rows):
            for c in range(columns):
                if dfs(r,c,0): return True
        
        def dfs(r, c, i):

            if i == len(word):
                return True
            
            if r < 0 or c < 0 or \
                r >= rows or c >= columns or \
                board[r][c] != word[i] or \
                (r,c) in visited:
                return False
            
            visited.add((r,c))
            res = (dfs(r+1, c, i+1) or
                    dfs(r-1, c, i+1) or
                    dfs(r, c-1, i+1) or
                    dfs(r, c+1, i+1))
            
            visited.remove((r,c))
            return res

        return False