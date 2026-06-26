class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_pf = 0
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                profit = prices[j] - prices[i]
                max_pf = max(max_pf, profit)
        return max_pf 