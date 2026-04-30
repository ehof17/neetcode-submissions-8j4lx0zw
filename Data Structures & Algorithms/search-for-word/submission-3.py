class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # check up, down, left, right
        ROWS = len(board)
        COLS = len(board[0])
        char_to_find = word[0]

        def helper(i, r, c):
            if i == len(word):
                return True
            if c >= COLS or r >= ROWS or c < 0 or r < 0 or board[r][c]!=word[i]:
                return False

            temp = board[r][c]
            board[r][c] = "#"
            val = (
                helper(i+1,r,c+1) or
                helper(i+1,r+1,c) or
                helper(i+1,r-1,c) or
                helper(i+1,r,c-1)
                )
            board[r][c]=temp
            return val
                
            
        for row in range(ROWS):
            for col in range(COLS):
                
                if helper(0, row, col):
                    return True
        return False