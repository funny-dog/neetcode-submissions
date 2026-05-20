class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK, MAX = 0xFFFFFFFF, 0x7FFFFFFF
        while b:
            carry = ((a & b) << 1) & MASK
            a = (a ^ b) & MASK
            b = carry
        return a if a<=MAX else ~(a ^ MASK)