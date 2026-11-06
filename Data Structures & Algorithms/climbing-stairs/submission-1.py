class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {} 

        def solve(temp):

            if temp > n:
                return 0
            
            #Base condition
            if temp == n:
                return 1

            if temp in memo:
                return memo[temp]

            memo[temp] = solve(temp + 1) + solve(temp + 2)

            return memo[temp]
        
        return solve(0)