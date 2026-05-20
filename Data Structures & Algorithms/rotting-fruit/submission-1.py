from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return -1
        m, n = len(grid), len(grid[0])
        q = deque()
        fresh = 0
        time = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1
        if fresh == 0:
            return 0
            
        while q:
            size = len(q)
            for _ in range(size):
                i, j = q.popleft()
                for dx, dy in [(0,1), (0,-1),(1,0), (-1,0)]:
                    di, dj = i+dx, j+dy
                    if 0<=di<m and 0<=dj<n and grid[di][dj] == 1:
                        grid[di][dj] = 2
                        q.append((di, dj))
                        fresh -= 1
            time += 1
        
        return time-1 if not fresh else -1