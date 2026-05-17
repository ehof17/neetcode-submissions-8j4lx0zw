class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS = len(board)
        COLS = len(board[0])
        directions = [[0,1], [0, -1], [1, 0], [-1, 0]]
        # # means safe
        # flip all remaining O cells
        def dfs(r, c):
            if min(r,c) < 0 or r >= ROWS or c >= COLS or board[r][c] != "O":
                return

            board[r][c] = "#"
            for d_r, d_c in directions:
                dfs(r+d_r, c+d_c)
       
        for r in range(ROWS):
            if board[r][0] == "O":
                dfs(r, 0)
            if board[r][COLS -1] == "O":
                dfs(r, COLS-1)
        for c in range(COLS):
            if board[0][c] == "O":
                dfs(0,c)
            if board[ROWS-1][c] == "O":
                dfs(ROWS-1, c)

        for R in range(ROWS):
            for C in range(COLS):
                if board[R][C]=="O":
                    board[R][C] = "X"
                if board[R][C] == "#":
                    board[R][C]="O"

    


