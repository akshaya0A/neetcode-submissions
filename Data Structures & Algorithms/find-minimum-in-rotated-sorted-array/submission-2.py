from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        # If the array is not rotated
        if nums[left] <= nums[right]:
            return nums[left]

        while left < right:
            mid = (left + right) // 2

            # If mid element is greater than the rightmost, min is to the right
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                # Min is at mid or to the left
                right = mid

        # left == right points to the smallest element
        return nums[left]

