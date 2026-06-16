class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        self.dfs(s, 0, res, [])
        return res
    def dfs(self, s, start, res, soFar):
        if start == len(s):
            res.append(soFar[:])
            return
        for i in range(start, len(s)):
            if self.isPal(s, start, i):
                soFar.append(s[start:i+1])
                self.dfs(s, i+1, res, soFar)
                soFar.pop()

    def isPal(self, s, i, j):
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True
            