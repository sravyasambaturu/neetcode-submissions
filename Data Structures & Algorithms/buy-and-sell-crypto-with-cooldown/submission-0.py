class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dicti = {}
        def solve(i, buying):
            if i >= len(prices):
                return 0
            
            if (i, buying) in dicti:
                return dicti[(i, buying)]

            if buying:
                buy = solve(i + 1, not buying) - prices[i]
                cooldown = solve(i + 1, buying)
                dicti[(i, buying)] = max(buy, cooldown)
                
            else:
                sell = solve(i + 2, not buying) + prices[i]
                cooldown = solve(i + 1, buying)
                dicti[(i, buying)] = max(sell, cooldown)
            
            return dicti[(i, buying)]
         
        return solve(0, True)