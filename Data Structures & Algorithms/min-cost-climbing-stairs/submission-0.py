class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}

        def solve(i):

            #Base cond
            if i >= len(cost):
                return 0

            if i in memo:
                return memo[i]

            #choices
            temp_left = solve(i + 1)

            temp_right = solve(i + 2)

            memo[i] = cost[i] + min(temp_left, temp_right)

            return memo[i]
        

        res = min(solve(0), solve(1))
        return res