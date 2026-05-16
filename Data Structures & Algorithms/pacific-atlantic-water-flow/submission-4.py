from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # top right and bottom left will always be in both

        #
        # check everyrhing that 
        ROWS = len(heights)
        COLS = len(heights[0])
        pacific = set()
        atlantic = set()
        directions = [(0,1), (0,-1), (1,0), (-1,0)]

        def bfs(starts):
            q = deque(starts)
            visited = set(starts)
            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc
                    if (
                        0 <= nr < ROWS and
                        0 <= nc < COLS and
                        (nr,nc) not in visited and
                        heights[nr][nc]>=heights[r][c]
                    ):
                        visited.add((nr,nc))
                        q.append((nr,nc))
            return visited
        pacific_start = [(0, c) for c in range(COLS)] + [(r, 0) for r in range(ROWS)]
        atlantic_start = [(r, COLS-1) for r in range(ROWS)] + [(ROWS-1, c) for c in range(COLS)]
        pacific = bfs(pacific_start)
        atlantic = bfs(atlantic_start)
        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in atlantic and (r, c) in pacific:
                    res.append((r,c))

        return res
       