class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        max_val, min_val = 1, 1
        for num in nums:
            if num == 0:
                max_val, min_val = 1, 1
                continue
            v1, v2 = max_val * num, min_val * num
            max_val = max(num, v1, v2)
            min_val = min(num, v1, v2)
            res = max(res, max_val, min_val)
        return res