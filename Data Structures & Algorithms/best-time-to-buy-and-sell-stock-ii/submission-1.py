class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        candidate = prices[0]
        profit = 0
        for i in range(1, len(prices)) :
            if prices[i] <= candidate :
                candidate = prices[i]
            else :
                profit = profit + (prices[i]- candidate)
                candidate = prices[i]
        return profit
            



