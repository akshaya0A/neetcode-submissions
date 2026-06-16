class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matching = {')': '(', ']': '[', '}': '{'}

        for c in s:
            # If it's an opening bracket, push to stack
            if c in "([{":
                stack.append(c)

            # If it's a closing bracket
            elif c in ")]}":
                # Stack must not be empty AND must match the correct opener
                if not stack or stack.pop() != matching[c]:
                    return False

        # All open brackets must be matched
        return len(stack) == 0
