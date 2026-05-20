class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def backtrack(start, path, target):
            if target == 0:
                res.append(path[:])
                return
            if target < 0:
                return
            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i, path, target - nums[i])
                path.pop()
        backtrack(0, [], target)
        return res
                
                