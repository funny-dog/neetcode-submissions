class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0

        m, n = len(matrix), len(matrix[0])
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        indegree = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                for dr, dc in directions:
                    nr, nc = i+dr, j+dc
                    if 0<=nr<m and 0<=nc<n and matrix[nr][nc] < matrix[i][j]:
                        indegree[i][j] += 1
        
        max_length = 0
        q = deque([(r, c) for r in range(m) for c in range(n) if indegree[r][c] == 0])
        while q:
            max_length += 1
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r+dr, c+dc
                    if 0<=nr<m and 0<=nc<n and matrix[nr][nc] > matrix[r][c]:
                        indegree[nr][nc] -= 1
                        if indegree[nr][nc] == 0:
                            q.append((nr, nc))
        return max_length
