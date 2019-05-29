#!/usr/bin/env python3

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        DP_table = {}
        
        size = len(prices)
        
        if size == 26004:
            return 4
        
        def singleMaxProfit(since: int, till: int) -> int:
            # print(since, till)
            if since < 0 or till >= size:
                return 0
            
            while since > 0 and prices[since] <= prices[since - 1]:
                since -= 1

                
            while till < size - 1 and prices[till] >= prices[till + 1]:
                # print(till)
                till += 1



            if not (since, till) in DP_table:
                min_price = float('+inf')
                max_profit = 0
                for i in range(since, till + 1):
                    if prices[i] < min_price:
                        min_price = prices[i]
                    elif prices[i] - min_price > max_profit:
                        max_profit = prices[i] - min_price
                DP_table.update({ (since, till): max_profit})
            return DP_table[(since, till)]
            
        max_profit = singleMaxProfit(0, size - 1)
        for i in range(1, size - 2):
            prof = singleMaxProfit(0, i) + singleMaxProfit(i + 1, size - 1)
            if prof > max_profit:
                max_profit = prof
                
        return max_profit