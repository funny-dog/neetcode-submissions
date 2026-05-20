class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []
        m, n = len(heights), len(heights[0])
        pacific = [[False] * n for _ in range(m)]
        atlantic = [[False] * n for _ in range(m)]
        def dfs(r, c, visited):
            visited[r][c] = True
            for dr, dc in [(0,1), (1,0), (0,-1), (-1,0)]:
                dx, dy = r+dr, c+dc
                if 0<=dx<m and 0<=dy<n and visited[dx][dy] == False and heights[dx][dy] >= heights[r][c]:
                    dfs(dx, dy, visited)
        for i in range(m):
            dfs(i, 0, pacific)
            dfs(i, n-1, atlantic)
        for j in range(n):
            dfs(0, j, pacific)
            dfs(m-1, j, atlantic)
        return [[i, j] for i in range(m) for j in range(n) if pacific[i][j] and atlantic[i][j]]
        