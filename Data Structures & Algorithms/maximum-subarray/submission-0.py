class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_val, curr_val = nums[0], nums[0]
        for num in nums[1:]:
            curr_val = max(num, num + curr_val)
            max_val = max(max_val, curr_val)
        return max_val