class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        for i in range(len(temperatures)):
            temp = temperatures[i]
            count = 0
            for j in range(i, len(temperatures)):
                if temperatures[j] > temp:
                    result[i] =count
                    break
                else:
                    count +=1
        return result