class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        visited = [False] * n
        dist = [float("inf")] * n
        dist[0] = 0
        sum = 0

        def get_min_val():
            min_val = float("inf")
            min_idx = -1
            for i, d in enumerate(dist):
                if not visited[i] and d < min_val:
                    min_val = d
                    min_idx = i
            return min_idx, min_val

        for _ in range(n):
            min_idx, min_val = get_min_val()
            visited[min_idx] = True
            sum += min_val

            for v in range(n):
                if visited[v]:
                    continue
                d = abs(points[min_idx][0] - points[v][0]) + abs(points[min_idx][1] - points[v][1])
                dist[v] = min(dist[v], d)
        return sum
