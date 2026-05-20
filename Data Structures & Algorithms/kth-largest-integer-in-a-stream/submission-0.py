import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.q = []
        self.k = k
        for num in nums:
            if len(self.q) == k:
                if num > self.q[0]:
                    heapq.heappushpop(self.q, num)
                continue
            heapq.heappush(self.q, num)


    def add(self, val: int) -> int:
        if len(self.q) == self.k:
            if val > self.q[0]:
                heapq.heappushpop(self.q, val)
        else:
            heapq.heappush(self.q, val)
        return self.q[0]
