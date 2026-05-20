class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles) 
        def can_finish(speed):
            return sum(1 + (pile - 1) // speed for pile in piles) <= h
        
        while left < right:
            mid = left + (right - left) // 2
            if can_finish(mid):
                right = mid
            else:
                left = mid + 1
        
        return left