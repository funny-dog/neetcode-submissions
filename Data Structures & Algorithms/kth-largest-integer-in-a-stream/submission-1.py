import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.q = []
        self.k = k
        for num in nums:
            self.add(num)


    def add(self, val: int) -> int:
        heapq.heappush(self.q, val)
        if len(self.q) > self.k:
                heapq.heappop(self.q)
        return self.q[0]
