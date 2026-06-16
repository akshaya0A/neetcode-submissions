import operator

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            if c in "+-*/":
                t2 = stack.pop()
                t1 = stack.pop()
                if c == "+":
                    stack.append(t1+t2)
                elif c == "-":
                    stack.append(t1-t2)
                elif c == "*":
                    stack.append(t1*t2)
                else:
                    stack.append(int(float(t1)/t2))                
            else:
                stack.append(int(c))
        return stack[0]