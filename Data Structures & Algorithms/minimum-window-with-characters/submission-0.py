from collections import Counter, defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        window = defaultdict(int)
        valid = 0
        left = 0
        min_size = float("inf")
        min_start = 0

        for right in range(0, len(s)):
            curr = s[right]
            if curr in need:
                window[curr] += 1
                if window[curr] == need[curr]:
                    valid += 1
            while valid == len(need):
                if right-left+1 < min_size:
                    min_size = right - left + 1
                    min_start = left
                pre = s[left]
                if pre in window:
                    if window[pre] == need[pre]:
                        valid -= 1
                    window[pre] -= 1
                left += 1
        
        return s[min_start: min_start + min_size] if min_size != float("inf") else ""