class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)
        if n == 0:
            return []
        intervals.sort(key = lambda x: x[0])
        res = [intervals[0]]
        for interval in intervals:
            if interval[0] <= res[-1][1]:
                res[-1][1] = max(interval[1], res[-1][1])
            else:
                res.append(interval)
        return res