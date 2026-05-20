"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        intervals.sort(key = lambda x: x.start)
        q = []
        for interval in intervals:
            start, end = interval.start, interval.end
            if q and q[0] <= start:
                heapq.heappop(q)
            heapq.heappush(q, end)
        return len(q)