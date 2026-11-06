class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        visited = {}
        
        def solve(i, j):
            if i >= m or j >= n:
                return 0

            if i == m - 1 and j == n - 1:
                return 1

            if (i, j) in visited:
                return visited[(i, j)]
            

            visited[(i, j)] = solve(i + 1, j) + solve(i, j + 1)

            return visited[(i, j)]
        
        return solve(0, 0)