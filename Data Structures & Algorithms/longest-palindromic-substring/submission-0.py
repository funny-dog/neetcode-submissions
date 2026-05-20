class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        def expand(l, r):
            while 0<=l and r<len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l+1:r]

        res = ""
        for i in range(len(s)):
            s1, s2 = expand(i, i), expand(i, i+1)
            res = max(res, s1, s2, key=len)
        return res