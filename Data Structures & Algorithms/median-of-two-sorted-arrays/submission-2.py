class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:        
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        m, n = len(nums1), len(nums2)
        left, right = 0, m
        while left <= right:
            mid1 = left + (right - left) // 2
            mid2 = (m + n + 1) // 2 - mid1

            nums1_left = nums1[mid1 - 1] if mid1 > 0 else float("-inf")
            nums1_right = nums1[mid1] if mid1 < m else float("inf")
            nums2_left = nums2[mid2 - 1] if mid2 > 0 else float("-inf")
            nums2_right = nums2[mid2] if mid2 < n else float("inf")

            left_max, right_min = max(nums1_left, nums2_left), min(nums1_right, nums2_right)
            if left_max <= right_min:
                if (m + n) % 2 == 1:
                    return left_max
                else:
                    return (left_max + right_min) / 2
            elif nums1_left > nums2_right:
                right = mid1 - 1
            else:
                left = mid1 + 1
        return 0.0