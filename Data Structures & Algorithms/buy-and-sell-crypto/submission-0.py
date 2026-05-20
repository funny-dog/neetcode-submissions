class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float("inf")
        max_res = 0
        for price in prices:
            min_price = min(price, min_price)
            max_res = max(max_res, price - min_price)
        return int(max_res)