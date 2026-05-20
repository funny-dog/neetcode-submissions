from _heapq import heappop
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort(key = lambda x: x[0])
        n = len(intervals)
        q = []
        res = [-1] * len(queries)
        j = 0

        for i, query in sorted(enumerate(queries), key = lambda x: x[1]):
            while j < n and intervals[j][0] <= query:
                l, r = intervals[j]
                heapq.heappush(q, (r-l+1, r))
                j += 1
            while q and q[0][1] < query:
                heapq.heappop(q)
            if q:
                res[i] = q[0][0]
        return res
