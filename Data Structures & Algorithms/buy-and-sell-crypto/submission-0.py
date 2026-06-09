class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        L =0
        profit = 0
        minimum = prices[0]

        for R in range(len(prices)):
            minimum = min(minimum, prices[R])
            profit = max(profit, prices[R] - minimum)
        return profit




        