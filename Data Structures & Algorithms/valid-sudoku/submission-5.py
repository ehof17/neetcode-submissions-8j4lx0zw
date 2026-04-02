class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # all rows to be valid
        # all columns to be valid
        # all cubes to be valid
        rows = [set() for _ in range(len(board))]
        cols = [set() for _ in range(len(board))]
        squares = [set() for _ in range(len(board))]
        for r, row in enumerate(board):
            for c, val in enumerate(row):
                if val == ".":
                    continue 
                row_sq = r // 3
                col_sq = c // 3
                square_id = row_sq * 3 + col_sq
                # 2 and 2 != 3 and 1
                if val in rows[r]:
                    return False
                rows[r].add(val)
                if val in cols[c]:
                    return False
                cols[c].add(val)
                if val in squares[square_id]:
                    return False
                squares[square_id].add(val)

        return True
                
