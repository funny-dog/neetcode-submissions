import heapq
from math import sqrt
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        q = []
        for i, point in enumerate(points):
            x, y = point[0], point[1]
            heapq.heappush(q, ((x**2 + y**2), i, point))
        res = []
        for _ in range(k):
            dist, i, point = heapq.heappop(q)
            res.append(point)
        return res