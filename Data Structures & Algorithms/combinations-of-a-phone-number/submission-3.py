class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        res = []
        mapp = {2:'abc', 3:'def', 4:'ghi', 5:'jkl', 6:'mno', 7:'pqrs', 8:'tuv', 9:'wxyz'}
        self.helper(digits,mapp, 0, res, [])
        return res
    def helper(self, digits,mapp, start, res, soFar):
        if len(digits) == len(soFar):
            res.append("".join(soFar))
            return
        
        digit = int(digits[start])
        for val in mapp[digit]:
            soFar.append(val)
            self.helper(digits, mapp, start+1, res, soFar)
            soFar.pop()
