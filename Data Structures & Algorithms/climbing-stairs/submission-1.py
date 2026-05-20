class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        dp1, dp2 = 1, 2
        for _ in range(n-2):
            dp1, dp2 = dp2, dp1 + dp2
        return dp2