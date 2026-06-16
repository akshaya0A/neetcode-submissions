class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        self.helper(candidates,target,  res, 0, [])
        return res
    def helper(self, candidates,target, res, start, soFar):
        if target == 0:
            res.append(soFar[:])
            return
        if target < 0:
            return
        for i in range(start, len(candidates)):
            if i > start and candidates[i] == candidates[i - 1]:
                continue
            soFar.append(candidates[i])
            self.helper(candidates, target-candidates[i], res, i+1, soFar)
            soFar.pop()
    