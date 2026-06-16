class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        while i < len(nums) - 1:
            left = target - nums[i]
            for j in range(len(nums)):
                if i != j and nums[j] == left:
                    return [i, j]
            i += 1
        return []