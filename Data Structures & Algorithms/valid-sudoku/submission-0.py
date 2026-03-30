from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowMap = defaultdict(list)
        colMap = defaultdict(list)
        sqMap = defaultdict(list)
        for r, rows in enumerate(board):
            for c, val in enumerate(rows):
                sqidx = (r//3) *3 + (c//3)
                if val != '.':
                    if val in rowMap[r]:
                        print(f"fail cux we in row")
                        return False
                    if val in colMap[c]:
                        print(f"fail cuz we in col")
                        return False
                    if val in sqMap[sqidx]:
                        print(f"fail cuz we in sq")
                        return False
                    rowMap[r].append(val)
                    colMap[c].append(val)
                    sqMap[sqidx].append(val)
        return True


        
        