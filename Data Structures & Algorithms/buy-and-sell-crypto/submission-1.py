class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = float("-inf")
        min_val = float("inf")
        for n in prices:
            min_val = min(min_val, n)
            max_profit = max(n - min_val, max_profit)

        return max_profit
        