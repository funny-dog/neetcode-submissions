class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        num_set = set(nums)
        max_len = 0

        for num in nums:
            if num - 1 not in num_set:
                curr_num = num
                tmp_len = 1
                while curr_num + 1 in num_set:
                    curr_num += 1
                    tmp_len += 1
                max_len = max(max_len, tmp_len)
        
        return max_len