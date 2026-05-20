class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def check(left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True
        
        def backtrack(path, start):
            if start == len(s):
                res.append(path[:])
                return
            for i in range(start, len(s)):
                if check(start, i):
                    path.append(s[start:i+1])
                    backtrack(path, i+1)
                    path.pop()

        backtrack([], 0)
        return res