class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        crt_buy, crt_sell = prices[0], None
        profit = 0
        for elt in prices :
            if not crt_sell :
                if elt-crt_buy > 0 :
                    crt_sell = elt
                    profit = max(profit,crt_sell-crt_buy)
            elif elt > crt_sell :
                crt_sell = elt
                profit = elt-crt_buy
            
            if elt < crt_buy :
                crt_buy = elt
                crt_sell = None
        return profit
            
            
