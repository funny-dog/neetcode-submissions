from collections import Counter, defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_cnt = Counter(s1)
        window = defaultdict(int)
        for i in range(len(s1)):
            window[s2[i]] += 1
        if window == s1_cnt:
            return True
        for i in range(len(s1), len(s2)):
            left, right = s2[i - len(s1)], s2[i]
            window[right] += 1
            window[left] -= 1
            if window[left] == 0:
                del window[left]
            if window == s1_cnt:
                return True
        return False