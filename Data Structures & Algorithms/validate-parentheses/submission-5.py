class Solution:
    def isValid(self, s: str) -> bool:
        vals = {']':'[', '}':'{', ')':'('}
        stack = []
        for c in s:
            if c in vals:                
                if stack and stack[-1] == vals[c]:
                    stack.pop()          
                else:
                    return False         
            else:                        
                stack.append(c)
        return len(stack) == 0