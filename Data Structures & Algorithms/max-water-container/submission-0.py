class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_res = -1
        left, right = 0, len(heights) - 1
        while left < right:
            max_res = max(max_res, min(heights[left], heights[right]) * (right - left))
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return max_res