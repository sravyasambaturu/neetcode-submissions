from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        q = deque()
        time, fresh = 0, 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    q.append((i,j))
            
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        while q and fresh > 0:
            for _ in range(len(q)):
                i,j = q.popleft()
                for di, dj in directions:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == 1:
                        grid[ni][nj] = 2
                        fresh -= 1
                        q.append((ni, nj))
                        
            time += 1

        return time if fresh == 0 else -1
                        
    

        