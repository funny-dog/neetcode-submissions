class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = [[] for _ in range(n+1)]
        dist = [float("inf")] * (n+1)
        dist[k] = 0
        for u,v,t in times:
            graph[u].append((v, t))
        
        q = [(0, k)]
        while q:
            d, curr = heapq.heappop(q)
            if d > dist[curr]:
                continue
            for nxt, t in graph[curr]:
                if d + t < dist[nxt]:
                   dist[nxt] = d+t
                   heapq.heappush(q, (d+t, nxt))
        return max(dist[1:]) if max(dist[1:]) != float("inf") else -1