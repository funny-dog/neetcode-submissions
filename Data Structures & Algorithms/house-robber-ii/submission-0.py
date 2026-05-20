class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def get_part_max(left, right):
            dp1, dp2 = 0, 0
            for i in range(left, right):
                dp1, dp2 = dp2, max(dp2, dp1+nums[i])
            return dp2
        return max(get_part_max(0, len(nums)-1), get_part_max(1, len(nums)))