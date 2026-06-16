class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # Build prefix array
        prefix = []
        running = 1
        for x in nums:
            running *= x
            prefix.append(running)

        # Build suffix array (reverse direction)
        suffix = []
        running = 1
        for i in range(n - 1, -1, -1):
            running *= nums[i]
            suffix.append(running)
        suffix.reverse()
        result = []
        for i in range(n):
            left = prefix[i - 1] if i > 0 else 1
            right = suffix[i + 1] if i < n - 1 else 1
            result.append(left * right)

        return result