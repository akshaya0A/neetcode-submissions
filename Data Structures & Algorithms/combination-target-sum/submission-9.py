from typing import List

class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def helper(start, path, total):
            if total == target:
                res.append(path.copy())
                return
            if total > target:
                return
            
            for i in range(start, len(nums)):
                path.append(nums[i])
                helper(i, path, total + nums[i])  
                path.pop() 
        helper(0, [], 0)
        return res