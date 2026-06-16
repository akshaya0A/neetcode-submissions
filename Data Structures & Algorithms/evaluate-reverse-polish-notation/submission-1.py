import operator

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': lambda a, b: int(a / b) 
        }
        for c in tokens:
            if c in ops:
                t2 = stack.pop()
                t1 = stack.pop()
                stack.append(ops[c](t1,t2))
            else:
                stack.append(int(c))
        return stack[0]