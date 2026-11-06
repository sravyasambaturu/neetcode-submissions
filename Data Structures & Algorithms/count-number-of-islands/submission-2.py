class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        rows, cols = len(grid), len(grid[0])
        islands = 0

        def dfs(r, c):
            # Base cases: out of bounds or water ('0')
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == "0":
                return

            # Mark as visited by "sinking" the land
            grid[r][c] = "0"

            # Explore all 4 orthogonal directions
            dfs(r + 1, c)  # Down
            dfs(r - 1, c)  # Up
            dfs(r, c + 1)  # Right
            dfs(r, c - 1)  # Left

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    islands += 1
                    dfs(r, c)  # Sink the entire connected island

        return islands