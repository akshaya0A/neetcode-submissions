class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def helper(i, soFar):
            if i == len(nums):
                res.append(soFar[:])
                return
            helper(i+1, soFar)
            soFar.append(nums[i])
            helper(i+1, soFar)
            soFar.pop()
        helper(0, [])
        return res