class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort(reverse=True)
        memo = {}

        def dfs(i, amount):
            if amount == 0:
                return 0

            if i == len(coins):
                return float("inf")

            if (i, amount) in memo:
                return memo[(i, amount)]

            res = dfs(i + 1, amount)

            if coins[i] <= amount:
                res = min(res, 1 + dfs(i, amount - coins[i]))
            
            memo[(i, amount)] = res
            

            return res
        
        ans = dfs(0, amount)

        return ans if ans != float("inf") else -1