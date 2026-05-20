import heapq
class MedianFinder:

    def __init__(self):
        self.min_q, self.max_q = [], []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.max_q, -num)
        heapq.heappush(self.min_q, -heapq.heappop(self.max_q))
        if len(self.max_q) < len(self.min_q):
            heapq.heappush(self.max_q, -heapq.heappop(self.min_q))

    def findMedian(self) -> float:
        if len(self.max_q) - len(self.min_q) == 1:
            return -self.max_q[0]
        return (-self.max_q[0] + self.min_q[0]) / 2