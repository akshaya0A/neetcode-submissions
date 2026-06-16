class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []
        self.helper(nums,res,  0, target, [])
        return res
    def helper(self, nums, res,start, target, soFar): 
        if target == 0:
            res.append(soFar[:])
            
        if target < 0:
            return
        for i in range(start, len(nums)):
            soFar.append(nums[i])
            self.helper(nums, res,i, target - nums[i], soFar)  
            soFar.pop()

    