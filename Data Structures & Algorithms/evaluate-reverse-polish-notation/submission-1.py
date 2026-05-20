class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        oprands = {"+": lambda a, b: a+b, "-": lambda a, b: a-b, 
        "*": lambda a, b: a*b, "/": lambda a, b: int(a/b)}
        for token in tokens:
            if token in oprands:
                b, a = stack.pop(), stack.pop()
                c = oprands[token](a, b)
                stack.append(c)
            else:
                stack.append(int(token))
        return stack[0]