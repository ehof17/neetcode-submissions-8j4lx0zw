from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        current = []
        ROWS = len(grid)
        COLS = len(grid[0])
        infected_cnt = 0
        total_fruits = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]==2:
                    infected_cnt+=1
                    total_fruits+=1
                    current.append((r,c))
                    q.append([r,c])
                if grid[r][c]==1:
                    total_fruits+=1

        def process(r,c):
            nonlocal infected_cnt
            if min(r, c) < 0 or r >= ROWS or c >= COLS or grid[r][c] != 1:
                return
            grid[r][c]=2
            q.append([r,c])
            infected_cnt+=1
        time = 0
        # for x in rn
        while q:
            for i in range(len(q)):
                r,c = q.popleft()
                process(r+1, c)
                process(r-1, c)
                process(r, c-1)
                process(r, c+1)
            time+=1
        

        if total_fruits == infected_cnt: return max(0, time - 1)
        return -1
        # time+=1

         