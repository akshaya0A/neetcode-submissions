class Solution:
    def isValid(self, s: str) -> bool:
        stack =[]
        dic = {')': '(',"}": "{", "]":"["}
        so =""
        for c in s:
            if c in "([{":
                stack.append(c)
                so+=c
            elif c in "])}":
                if not stack:     
                    return False

                x = stack.pop()
                if dic[c] != x:
                    return False
        return len(stack) == 0