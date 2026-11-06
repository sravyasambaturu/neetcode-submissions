class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dicti = {}
        def solve(i, value):
            if value == amount:
                return 1 

            if i >= len(coins) or value > amount:
                return 0

            if (i, value) in dicti:
                return dicti[(i, value)]
            
            res = solve(i, value + coins[i]) + solve(i + 1, value)

            dicti[(i, value)] = res

            return res
        
        return solve(0, 0)
        