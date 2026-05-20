import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        q = []
        res = 0
        for stone in stones:
            heapq.heappush(q, -stone)
        while len(q) > 1:
            s1, s2 = heapq.heappop(q), heapq.heappop(q)
            heapq.heappush(q, -abs(s1 - s2))
        return -q[0]