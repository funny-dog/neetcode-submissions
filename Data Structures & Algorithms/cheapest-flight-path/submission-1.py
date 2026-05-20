class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = [[] for _ in range(n)]
        for u,v,w in flights:
            graph[u].append((v, w))
        visited = set()
        q = [(0, src, 0)]

        while q:
            price, node, stops = heapq.heappop(q)
            if node == dst:
                return price
            if stops > k:
                continue
            if (node, stops) in visited:
                continue
            visited.add((node, stops))
            for next_node, cost in graph[node]:
                if next_node not in visited:
                    heapq.heappush(q, (price+cost, next_node, stops+1))
        return -1
