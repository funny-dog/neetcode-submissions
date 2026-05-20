class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.word = None

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for word in words:
            node = root
            for c in word:
                if c not in node.children:
                    node.children[c] = TrieNode()
                node = node.children[c]
            node.word = word

        res = []
        m, n = len(board), len(board[0])
        def dfs(row, col, node):
            if node.word:
                res.append(node.word)
                node.word = None
                    
            tmp = board[row][col]
            board[row][col] = "#"
            for row_offset, col_offset in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                next_row = row + row_offset
                next_col = col + col_offset
                if 0 <= next_row < m and 0 <= next_col < n and board[next_row][next_col] in node.children:
                    dfs(next_row, next_col, node.children[board[next_row][next_col]])
            board[row][col] = tmp
            
        for i in range(m):
            for j in range(n):
                if board[i][j] in root.children:
                    dfs(i, j, root.children[board[i][j]])
        return res