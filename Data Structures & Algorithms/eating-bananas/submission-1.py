class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        def helper(k):
            return sum(math.ceil(pile / k) for pile in piles)
        
        while left < right:
            mid = left + (right - left) // 2
            if helper(mid) <= h:
                right = mid  
            else:
                left = mid + 1  
        
        return left