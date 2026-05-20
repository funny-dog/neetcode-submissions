class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visited = [[False] * n for _ in range(n)]
        q = [(grid[0][0], 0, 0)]

        while q:
            max_height, r, c = heapq.heappop(q)
            visited[r][c] = True
            if r == n-1 and c == n-1:
                return max_height
            
            for dr, dc in [(0,1), (0,-1), (1,0), (-1,0)]:
                x, y = r+dr, c+dc
                if 0<=x<n and 0<=y<n and not visited[x][y]:
                    heapq.heappush(q, (max(max_height, grid[x][y]), x, y))
        return -1