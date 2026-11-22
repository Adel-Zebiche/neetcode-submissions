class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        i = 1
        candidate = prices[0]
        profit = 0
        while i < n :
            if prices[i] <= candidate :
                candidate = prices[i]
            else :
                profit = profit + (prices[i]- candidate)
                candidate = prices[i]
            i+=1
        return profit
            



