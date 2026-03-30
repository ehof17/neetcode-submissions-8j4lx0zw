class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = []
        fresh = 0
        time = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    fresh+=1
                if grid[r][c] == 2:
                    q.append((r,c))

        directions = [[0,1], [0,-1], [1,0], [-1,0]] 

        while fresh > 0 and q:
            lenq = len(q)
            for i in range(lenq):
                (R,C) = q.pop(0)
                for d_r, d_c in directions:
                    n_r = d_r + R
                    n_c = d_c + C
                    if n_r in range(len(grid)) and n_c in range(len(grid[0])) and grid[n_r][n_c] == 1:
                        grid[n_r][n_c] = 2
                        
                        q.append((n_r, n_c))
                        fresh-=1
                        
            time+=1

        return time if fresh == 0 else -1