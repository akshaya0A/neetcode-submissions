class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        self.helper(n, res, [], 0, 0)
        return ["".join(s) for s in res]  

    def helper(self, n, res, soFar, openCount, closeCount):
        if openCount == closeCount == n:
            res.append(soFar[:])
            return

        if openCount < n:
            soFar.append('(')
            self.helper(n, res, soFar, openCount + 1, closeCount)
            soFar.pop()

        if closeCount < openCount:
            soFar.append(')')
            self.helper(n, res, soFar, openCount, closeCount + 1)
            soFar.pop()
