class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # every row, every col, and every grid needs to be valid
        #gridIndex
        rowSets = {i:set() for i in range(9)}
        colSets = {i:set() for i in range(9)}
        gridSets = {
            (0,0):set(),
            (0,1):set(),
            (0,2):set(),
            (1,0):set(),
            (1,1):set(),
            (1,2):set(),
            (2,0):set(),
            (2,1):set(),
            (2,2):set()
        }


        for r, row in enumerate(board):
            for c, val in enumerate(row):
                if val != '.':
                    gridIndex = (r//3, c//3)
                    # 0 its in 1rd row
                    # 0 it can be 0, 1, 2

                    if val in rowSets[r]:
                        return False

                    rowSets[r].add(val)
                    
                    if val in colSets[c]:
                        return False
                    
                    colSets[c].add(val)

                    if val in gridSets[gridIndex]:
                        return False
                    
                    gridSets[gridIndex].add(val)

        return True






        
        