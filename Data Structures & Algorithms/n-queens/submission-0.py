class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        cols = set()
        diag1, diag2 = set(), set()
        def backtrack(row, curr_board):
            if row == n:
                res.append(curr_board[:])
                return
            for col in range(n):
                if col in cols or (row - col) in diag1 or (row + col) in diag2:
                    continue
                cols.add(col)
                diag1.add(row-col)
                diag2.add(row+col)
                curr_board.append("." * col + "Q" + "." * (n-col-1))
                
                backtrack(row+1, curr_board)

                curr_board.pop()
                diag2.remove(row+col)
                diag1.remove(row-col)
                cols.remove(col)
        backtrack(0, [])
        return res