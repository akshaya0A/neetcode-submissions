class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minn = prices[0]
        profit = 0
        for price in prices:
            minn = min(minn, price)
            profit = max(price - minn, profit)
        return profit