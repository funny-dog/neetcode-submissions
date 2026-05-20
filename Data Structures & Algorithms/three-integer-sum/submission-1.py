class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []
        for k in range(len(nums)):
            if k>0 and nums[k] == nums[k-1]:
                continue
            target = -nums[k]
            i, j = k+1, n-1
            while i < j:
                if nums[i] + nums[j] == target:
                    res.append([nums[i], nums[j], nums[k]])
                    while i<j and nums[i] == nums[i+1]:
                        i += 1
                    while i<j and nums[j] == nums[j-1]:
                        j -= 1
                    i += 1
                    j -= 1
                elif nums[i] + nums[j] < target:
                    i += 1
                else:
                    j -= 1
        return res