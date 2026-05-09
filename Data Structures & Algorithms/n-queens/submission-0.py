class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        if n == 1:
            return [["Q"]]
        # so we know we need a row with a queen in each thing
        # and then is the backtracking just the shuffling of the rows?

        # different row, different column
        # different diagonal
        #
        # For the first row, we have n choices
        # then the next row, we have n-1 choices
        # then the next row, we have n-2 choices

        # place thing
        # for everything that is valid 

        # keep the previous queen columns

        prevCols = set()
        posDiag = set()
        negDiag = set()
        # diagonals increase column by 1 and row by 1 as well
        # (r-c) = 0 negative diagonal
        # (r+c) = 3 positive diagonal
        row = 0
        res =[]
        board = [["."] * n for i in range(n)]

        def backtrack(r):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            for c in range(n):
                curNeg = r-c
                curPos = r+c
                if c in prevCols or curPos in posDiag or curNeg in negDiag:
                    continue
                
                prevCols.add(c)
                posDiag.add(curPos)
                negDiag.add(curNeg)
                board[r][c] = "Q"

                backtrack(r+1)

                prevCols.remove(c)
                posDiag.remove(curPos)
                negDiag.remove(curNeg)
                board[r][c] = "."
        backtrack(0)
        return res

