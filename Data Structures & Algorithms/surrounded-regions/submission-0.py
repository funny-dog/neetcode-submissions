from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board:
            return None
        m,n = len(board), len(board[0])
        visited = [[False] * n for _ in range(m)]
        q = deque()
        for i in range(m):
            if board[i][0] == "O":
                q.append((i, 0))
            if board[i][n-1] == "O":
                q.append((i, n-1))
        for j in range(n):
            if board[0][j] == "O":
                q.append((0, j))
            if board[m-1][j] == "O":
                q.append((m-1, j))
        while q:
            r, c = q.popleft()
            visited[r][c] = True
            for dr, dc in [(0,1), (0,-1), (1,0), (-1,0)]:
                rx, ry = r+dr, c+dc
                if 0<=rx<m and 0<=ry<n and board[rx][ry] == "O" and visited[rx][ry] == False:
                    q.append((rx, ry))
        for i in range(m):
            for j in range(n):
                if visited[i][j] == False and board[i][j] == "O":
                    board[i][j] = "X"