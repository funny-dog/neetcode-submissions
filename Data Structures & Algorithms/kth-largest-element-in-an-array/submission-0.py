import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        q = []
        for num in nums:
            if len(q) >= k:
                if num > q[0]:
                    heapq.heapreplace(q, num)
            else:
                heapq.heappush(q, num)
        return q[0]