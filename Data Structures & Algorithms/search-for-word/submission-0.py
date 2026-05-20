class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board:
            return False
        m, n = len(board), len(board[0])
        res = False
        def backtrack(row, col, idx):
            if idx == len(word):
                return True
            
            if row < 0 or row >= m or col < 0 or col >= n or board[row][col] != word[idx]:
                return False
            
            tmp = board[row][col]
            board[row][col] = "#"
            res = backtrack(row+1, col, idx+1) or backtrack(row-1, col, idx+1) or backtrack(row, col+1, idx+1) or backtrack(row, col-1, idx+1)
            board[row][col] = tmp
            return res
        for i in range(m):
            for j in range(n):
                if backtrack(i, j, 0):
                    return True
        return False
            