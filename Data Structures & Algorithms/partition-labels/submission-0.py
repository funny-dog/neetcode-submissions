class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # 找同一个字母的最后位置，这是为了相同字母保持在同一个子串
        last = {c: i for i, c in enumerate(s)}
        start, end = 0, 0
        res = []
        for i, c in enumerate(s):
            # 扩展边界
            end = max(end, last[c])
            # 到达边界
            if i == end:
                res.append(end - start + 1)
                start = end + 1
        return res