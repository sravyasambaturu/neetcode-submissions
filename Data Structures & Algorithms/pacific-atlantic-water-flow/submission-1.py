class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])

        def reach(starts):
            seen = set(starts)
            stack = list(starts)

            while stack:
                r, c = stack.pop()
                for dr, dc in ((0,1),(0,-1),(1,0),(-1,0)):
                    nr, nc = r+dr, c+dc
                    if 0 <= nr < rows  and 0 <= nc < cols and (nr,nc) not in seen and heights[nr][nc] >= heights[r][c]:
                        seen.add((nr, nc))
                        stack.append((nr,nc))            
            return seen

        pacific = reach([(0,c) for c in range(cols)] + [(r,0) for r in range(rows)]) 
        atlantic = reach([(rows-1, c) for c in range(cols)]+[(r, cols-1) for r in range(rows)])
        return [[r, c] for r, c in pacific & atlantic] 
