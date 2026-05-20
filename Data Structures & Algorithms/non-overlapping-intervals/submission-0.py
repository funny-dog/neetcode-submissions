class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        if n == 0:
            return 0
        cnt = 0
        intervals.sort(key = lambda x: x[1])
        end = intervals[0][1]
        for i in range(1, len(intervals)):
            if intervals[i][0] < end:
                cnt += 1
            else:
                end = intervals[i][1]
        return cnt