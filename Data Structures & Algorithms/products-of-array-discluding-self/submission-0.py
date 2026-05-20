class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n
        left_total, right_total = 1, 1

        for i in range(n):
            res[i] *= left_total
            left_total *= nums[i]
        
        for i in range(n-1, -1, -1):
            res[i] *= right_total
            right_total *= nums[i]
        
        return res