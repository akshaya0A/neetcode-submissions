class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            rem = target - nums[i]
            for j in range(len(nums)):
                if nums[j] == rem and i != j:
                    return [i,j]
        return []