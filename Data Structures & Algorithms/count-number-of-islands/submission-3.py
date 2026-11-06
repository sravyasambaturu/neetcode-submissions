class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0]) if grid else 0
        count = 0

        def sink(r, c):
            stack = [(r,c)]
            grid[r][c] = "0"
            while stack:
                x, y = stack.pop()
                for dx, dy in ((1,0), (0, -1), (0, 1), (-1,0)):
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == "1":
                        grid[nx][ny] = "0" 
                        stack.append((nx, ny))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    count += 1
                    sink(r,c)
        return count


        