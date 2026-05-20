from collections import Counter
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freqs = Counter(tasks)
        q = []
        time = 0
        for freq in freqs.values():
            heapq.heappush(q, -freq)
        while q:
            next_tasks = []
            for _ in range(n + 1):
                if q:
                    task = heapq.heappop(q) + 1
                    if task != 0:
                        next_tasks.append(task)
                time += 1
                if not q and not next_tasks:
                    break
            for task in next_tasks:
                heapq.heappush(q, task)
        return time
