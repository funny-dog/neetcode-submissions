class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        if not temperatures:
            return []
        n = len(temperatures)
        output = [0] * n
        stack = [(n-1, temperatures[n-1])]
        for j in range(n-2, -1, -1):
            while stack and temperatures[j] >= stack[-1][1]:
                stack.pop()
            if stack:
                output[j] = stack[-1][0] - j
            stack.append((j, temperatures[j]))

        return output