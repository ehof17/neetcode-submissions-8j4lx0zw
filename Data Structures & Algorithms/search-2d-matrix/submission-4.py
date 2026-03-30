class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS = len(matrix)
        COLS = len(matrix[0])
        # find the row it is in
        top, bot = 0, ROWS-1
        while top <= bot:
            row = (top+bot) // 2
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bot = row - 1
            else:
                break
        if not (top <= bot):
            return False
        row = (top + bot) // 2
        L, R = 0, COLS - 1
        while L <= R:
            m = (L+R)//2
            if matrix[row][m] < target:
                L = m + 1
            elif matrix[row][m] > target:
                R = m - 1
            else: 
                return True
        if matrix[row][m] == target:
            return True

        return False
        



        