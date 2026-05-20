class Solution:
    def isHappy(self, n: int) -> bool:
        def get_next(num):
            return sum(int(c) ** 2 for c in str(num))
        
        seen = set()
        while n != 1:
            if n in seen:
                return False
            seen.add(n)
            n = get_next(n)
        return True