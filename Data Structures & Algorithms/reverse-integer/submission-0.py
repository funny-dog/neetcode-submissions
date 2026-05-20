class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x<0 else 1
        x = abs(x)
        res = 0
        while x:
            if res > (2 ** 31 - 1) // 10:
                return 0
            res = res * 10 + x%10
            x //= 10
        return res * sign