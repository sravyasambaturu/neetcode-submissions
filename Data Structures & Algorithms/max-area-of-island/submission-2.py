class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0]) if grid else 0

        def dfs(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] != 1:
                return 0
            grid[r][c] = 0 #mark visited
            return 1 + dfs(r, c+1) + dfs(r, c-1) + dfs(r+1, c) + dfs(r-1, c)
                
        return max((dfs(r, c) for r in range(rows) for c in range(cols)), default=0)


# class Solution:
#     def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
#         rows, cols = len(grid), len(grid[0]) if grid else 0
#         max_area = 0

#         def dfs(r, c):
#             if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] != 1:
#                 return 0
            
#             grid[r][c] = 0 # Mark as visited so we don't count it again
            
#             # Sum up 1 (current cell) + all 4 neighboring directions
#             return 1 + dfs(r, c+1) + dfs(r, c-1) + dfs(r+1, c) + dfs(r-1, c)
                
#         # Run DFS only when we encounter a piece of land ('1')
#         for r in range(rows):
#             for c in range(cols):
#                 if grid[r][c] == 1:
#                     max_area = max(max_area, dfs(r, c))
                    
#         return max_area
