class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pre_idx: dict[int, int] = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in pre_idx:
                return [pre_idx[diff], i]
            pre_idx[num] = i
        return []