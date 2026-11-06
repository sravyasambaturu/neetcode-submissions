class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n = len(s)
        m = len(p)

        memo = {}
        
        def solve(i, j):
            if j == m:
                return i == n
            
            if (i, j) in memo:
                return memo[(i, j)]

            match = i < n and (s[i] == p[j] or p[j] == '.')


            if (j + 1) < m and p[j + 1] == "*":
                bully = solve(i, j + 2) or (match and solve(i + 1, j))
                memo[(i,j)] = bully
                return bully
                
            
            if match:
                bully = solve(i + 1, j + 1)
                memo[(i,j)] = bully
                return bully
            
            memo[(i,j)] = False
            return memo[(i,j)]
        
        return solve(0, 0)