class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()                
        res = []
        self.helper(nums, 0, [], res)
        return res

    def helper(self, nums, start, soFar, res):
        res.append(soFar[:])        

        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i - 1]:
                continue

            soFar.append(nums[i])
            self.helper(nums, i + 1, soFar, res)
            soFar.pop()