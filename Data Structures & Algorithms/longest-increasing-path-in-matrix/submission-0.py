class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])

        visited = {}

        def solve(i, j, prev_val):

            if i >= rows or i < 0 or j >= cols or j < 0 or matrix[i][j] <= prev_val:
                return 0
            
            if (i, j) in visited:
                return visited[(i, j)]

            
            
            else:
                #top
                top = 1 + solve(i-1, j, matrix[i][j])

                #bottom
                bottom = 1 + solve(i + 1, j, matrix[i][j])
          

                #left
                left = 1 + solve(i, j - 1, matrix[i][j])

                #right
                right = 1 + solve(i, j + 1, matrix[i][j])

                res = max(top, bottom, left, right)

                visited[(i, j)] = res

                return res

        
        max_len = -float("inf")
        for i in range(rows):
            for j in range(cols):
                max_len = max(max_len, solve(i, j, -1))
        
        return max_len
        