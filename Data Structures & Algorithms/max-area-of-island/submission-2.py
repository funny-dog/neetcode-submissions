class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        max_area = 0
        m, n = len(grid), len(grid[0])
        def dfs(row, col):
            if row < 0 or row >= m or col < 0 or col >= n or grid[row][col] == 0:
                return 0
            grid[row][col] = 0
            return 1 + dfs(row+1, col) + dfs(row-1, col) + dfs(row, col+1) + dfs(row, col-1)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    max_area = max(max_area, dfs(i, j))
        return max_area