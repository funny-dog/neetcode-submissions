class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        dp1, dp2 = nums[0], max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp1, dp2 = dp2, max(dp2, dp1+nums[i])
        return dp2