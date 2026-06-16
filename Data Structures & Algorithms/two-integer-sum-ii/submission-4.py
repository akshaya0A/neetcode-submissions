class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            rem = target -  numbers[i]
            for j in range(len(numbers)):
                if  numbers[j] == rem and i < j:
                    return [i+1, j+1]
        return []
