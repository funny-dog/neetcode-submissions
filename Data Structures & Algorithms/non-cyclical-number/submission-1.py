class Solution:
    def isHappy(self, n: int) -> bool:
        def get_next(num):
            next_num = 0
            while num > 0:
                next_num += (num%10) ** 2
                num //= 10
            return next_num
        slow, fast = get_next(n), get_next(get_next(n))
        while fast != 1 and slow != fast:
            slow, fast = get_next(slow), get_next(get_next(fast))
        return fast == 1