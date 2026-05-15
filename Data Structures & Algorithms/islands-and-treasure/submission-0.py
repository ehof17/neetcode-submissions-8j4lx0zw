from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # if -1: pop
        # if 0: everything near it is 1 away
        # check again for 1s, everything adjacent will be 2
        # check again for 2s, everything adjacent will be 3
        ROWS = len(grid)
        COLS = len(grid[0])
        visit = set()
        q = deque()

        def addRoom(r,c):
            if r == ROWS or r < 0 or c == COLS or c < 0 or (r, c) in visit or grid[r][c]==-1:
                return
            visit.add((r,c))
            q.append([r,c])

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]==0:
                    visit.add((r,c))
                    q.append([r,c])
        dist = 0
        while q:
            for i in range(len(q)):
                val = q.popleft()
                r, c = val
                grid[r][c] = dist
                addRoom(r+1, c)
                addRoom(r-1, c)
                addRoom(r, c-1)
                addRoom(r, c+1)
            dist+=1


       

       

        