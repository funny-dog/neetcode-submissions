class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float("inf")] * n
        prices[src] = 0

        for i in range(k+1):
            # 必须用副本，防止同一轮相互影响
            tmp = prices[:]
            for u,v,w in flights:
                if prices[u] == float("inf"):
                    continue
                tmp[v] = min(tmp[v], prices[u] + w)
            prices = tmp
        return -1 if prices[dst] == float("inf") else prices[dst]