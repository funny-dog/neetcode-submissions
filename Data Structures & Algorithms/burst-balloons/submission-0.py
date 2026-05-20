class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        if not nums:
            return 0
        balloons = [1] + nums + [1]
        n = len(balloons)
        dp = [[0] * n for _ in range(n)]

        left, right = 0, n
        for span in range(2, n):
            for left in range(n-span):
                right = span+left
                for last in range(left+1, right):
                    coins = dp[left][last] + dp[last][right] + balloons[left] * balloons[right] * balloons[last]
                    dp[left][right] = max(dp[left][right], coins)
                     
        return dp[0][n-1]