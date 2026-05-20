class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if not s:
            return 0
        cnt_dict: dict = {}
        max_char_cnt = 0
        res = 0
        left = 0
        for right in range(len(s)):
            cnt_dict[s[right]] = cnt_dict.get(s[right], 0) + 1
            max_char_cnt = max(max_char_cnt, cnt_dict[s[right]])
            while right - left + 1 - max_char_cnt > k:
                cnt_dict[s[left]] -= 1
                left += 1
            res = max(res, right - left + 1)
        return res