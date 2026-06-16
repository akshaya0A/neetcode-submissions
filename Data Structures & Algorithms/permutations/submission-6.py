class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.helper(nums, [], res)
        return res

    def helper(self, nums, soFar, res):
        if not nums:             
            res.append(soFar[:])
            return

        for i in range(len(nums)):
            soFar.append(nums[i])
            self.helper(nums[:i] + nums[i+1:], soFar, res)
            soFar.pop()
