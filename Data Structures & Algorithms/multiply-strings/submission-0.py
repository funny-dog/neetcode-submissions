class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        m, n = len(num1), len(num2)
        res = [0] * (m+n)

        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                res[i+j+1] += (ord(num1[i])-ord("0")) * (ord(num2[j])-ord("0"))
        
        for i in range(m+n-1, 0, -1):
            res[i-1] += res[i] // 10
            res[i] %= 10
        
        start = 1 if res[0] == 0 else 0
        return "".join(map(str, res[start:]))