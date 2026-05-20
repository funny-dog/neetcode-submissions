class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        res_dict = {}
        for i in range(len(s)):
            res_dict[s[i]] = res_dict.get(s[i], 0) + 1
            res_dict[t[i]] = res_dict.get(t[i], 0) - 1
        for val in res_dict.values():
            if val != 0:
                return False
        return True