from _heapq import heappop
import heapq
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = Counter(nums)
        q = []
        for key, freq in d.items():
            if len(q) < k:
                heapq.heappush(q, (freq, key))
            elif freq > q[0][0]:
                heapq.heappushpop(q, (freq, key))
        return [item[1] for item in q]