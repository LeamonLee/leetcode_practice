class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS = len(board)
        COLUMNS = len(board[0])
        visited = set()

        def dfs(r, c, index):
            if index == len(word): return True
            if r < 0 or c < 0 or \
                r >= ROWS or c >= COLUMNS or \
                (r,c) in visited or board[r][c] != word[index]:
                return False

            visited.add((r,c))

            if dfs(r-1, c, index+1) or \
                dfs(r+1, c, index+1) or \
                dfs(r, c-1, index+1) or \
                dfs(r, c+1, index+1):
                return True

            visited.remove((r,c))

            return False

        for r in range(ROWS):
            for c in range(COLUMNS):
                if dfs(r, c, 0):
                    return True
        return False