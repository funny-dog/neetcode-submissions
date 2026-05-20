class Trie:
    def __init__(self) -> None:
        self.children = {}
        self.is_end = False
        self.word = ""

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if not board or not words:
            return []
        res = []
        m, n = len(board), len(board[0])
        unique = set()

        root = Trie()
        for word in words:
            node = root
            for c in word:
                if c not in node.children:
                    node.children[c] = Trie()
                node = node.children[c]
            node.is_end = True
            node.word = word

        def dfs(row, col, node):
            if row < 0 or row >= m or col < 0 or col >= n:
                return
            c = board[row][col]
            if c not in node.children:
                return
            next_node = node.children[c]
            if next_node.is_end:
                res.append(next_node.word)
                next_node.is_end = False

            board[row][col] = "#"
            dfs(row+1, col, next_node)
            dfs(row-1, col, next_node)
            dfs(row, col+1, next_node)
            dfs(row, col-1, next_node)
            board[row][col] = c
           
        for i in range(m):
            for j in range(n):
                dfs(i, j, root)
        return res