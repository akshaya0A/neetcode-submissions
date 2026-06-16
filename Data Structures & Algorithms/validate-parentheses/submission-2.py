class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        things = {")":"(", "]":"[", "}":"{"}
        for c in s:
            if c in things:
                if stack and stack[-1] == things[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False