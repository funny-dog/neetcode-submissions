class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == "0":
            return 0
        dp1, dp2 = 1, 1
        for i in range(1, len(s)):
            cur = 0
            if s[i] != "0":
                cur = dp2
            if 10<=int(s[i-1:i+1]) <= 26:
                cur += dp1
            dp1, dp2 = dp2, cur
        return dp2