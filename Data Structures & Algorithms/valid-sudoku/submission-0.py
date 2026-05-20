class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row, col, box = [set() for i in range(9)], [set() for i in range(9)], [set() for i in range(9)]
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num == ".":
                    continue
                box_idx = (i // 3) * 3 + j // 3
                if num in row[i] or num in col[j] or num in box[box_idx]:
                    return False
                row[i].add(num)
                col[j].add(num)
                box[box_idx].add(num)
        return True