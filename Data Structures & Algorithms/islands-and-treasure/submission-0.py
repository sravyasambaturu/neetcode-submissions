from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m, n = len(grid), len(grid[0])
        visited = set()
        q = deque()

        def addCell(i,j):
            if i < 0 or i >= m or j < 0 or j >= n or  grid[i][j] == -1 or (i,j) in visited:
                return
            q.append((i,j))
            visited.add((i,j))

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    q.append((i,j))
                    visited.add((i,j))

        dist = 0
        while q:
            for r in range(len(q)):
                i , j = q.popleft()
                grid[i][j] = dist
                addCell(i+1, j)
                addCell(i-1, j)
                addCell(i, j+1)
                addCell(i, j-1)
            dist += 1
