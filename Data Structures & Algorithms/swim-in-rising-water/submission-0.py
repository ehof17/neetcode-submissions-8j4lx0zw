import heapq
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        adj = {}
        # adjacent is to left or to right
        ROWS = len(grid)
        COLS = len(grid[0])

        def r_c_to_index(r,c):
            # each row is 1 col len
            # row 2 column 1 is the third val
            index = (r * COLS) + c
            return index
            
        def index_to_rc(ind):
            row   = ind // ROWS
            column = ind % ROWS
            return row, column


        for i in range(ROWS*COLS):
            adj[i] = []
        
        for i in range(len(adj)):
            r,c = index_to_rc(i)
            if r >= 1:            # up
                adj[i].append((grid[r-1][c], r_c_to_index(r-1, c)))
            if r < ROWS - 1:      # down
                adj[i].append((grid[r+1][c], r_c_to_index(r+1, c)))
            if c >= 1:            # left
                adj[i].append((grid[r][c-1], r_c_to_index(r, c-1)))
            if c < COLS - 1:      # right
                adj[i].append((grid[r][c+1], r_c_to_index(r, c+1)))
      
        minHeap = [(0,0)]
        res = {}
        target = r_c_to_index(ROWS-1,COLS-1)
        seen = set()
        pq = [(grid[0][0], 0)]          # (time so far, index)

        while pq:
            t, idx = heapq.heappop(pq)
            if idx == target:
                return t

            r, c = divmod(idx, COLS)
            for nr, nc in ((r-1,c), (r+1,c), (r,c-1), (r,c+1)):
                if 0 <= nr < ROWS and 0 <= nc < COLS:
                    nidx = r_c_to_index(nr, nc)
                    if nidx not in seen:
                        seen.add(nidx)
                        heapq.heappush(pq, (max(t, grid[nr][nc]), nidx))
            
