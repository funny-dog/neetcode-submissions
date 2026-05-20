class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def find(left, right):
            if left > right:
                return -1
            mid = left + (right - left) // 2
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                return find(left, mid-1)
            else:
                return find(mid+1, right)
        return find(0, len(nums) - 1)