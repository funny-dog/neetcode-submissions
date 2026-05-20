from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid:
            return
        
        m, n = len(grid), len(grid[0])
        q = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    q.append((i,j))
        while q:
            i, j = q.popleft()
            for dx, dy in [(0,1), (0,-1), (1,0), (-1,0)]:
                di, dj = i+dx, j+dy
                if 0<=di<m and 0<=dj<n and grid[di][dj] == 2 ** 31 - 1:
                    grid[di][dj] = grid[i][j] + 1
                    q.append((di, dj))
