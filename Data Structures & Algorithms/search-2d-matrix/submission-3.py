class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            if row[0] <= target <= row[-1]:
                left = 0
                right = len(row)
                while left <= right:
                    mid = left + (right - left) // 2
                    if row[mid] == target:
                        return True
                    elif row[mid] < target:
                        left = mid +1 
                    else:
                        right = mid -1
        return False