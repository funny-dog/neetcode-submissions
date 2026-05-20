class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        curr_end = 0
        curr_length = 0
        for i in range(len(nums) - 1):
            curr_length = max(curr_length, i+nums[i])
            if i == curr_end:
                jumps += 1
                curr_end = curr_length
        return jumps
