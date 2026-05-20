class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        hold, not_hold, freeze = -prices[0], 0, 0
        for price in prices[1:]:
            pre_hold, pre_not_hold, pre_freeze = hold, not_hold, freeze
            hold = max(pre_hold, pre_not_hold - price)
            not_hold = max(pre_not_hold, pre_freeze)
            freeze = hold + price
        return max(not_hold, freeze)