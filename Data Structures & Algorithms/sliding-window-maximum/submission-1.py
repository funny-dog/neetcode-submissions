from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        if k > n:
            return [max(nums)]
        q_idx = deque()
        res = []
        for i in range(n):
            while q_idx and nums[q_idx[-1]] <= nums[i]:
                q_idx.pop()
            q_idx.append(i)
            if q_idx[0] < i-k+1:
                q_idx.popleft()
            if i >= k-1:
                res.append(nums[q_idx[0]])
        return res