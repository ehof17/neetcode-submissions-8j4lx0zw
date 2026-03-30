from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        colDict = defaultdict(list)
        rowDict = defaultdict(list)
        sqDict = defaultdict(list)
        # i is index of row,
        for i, r in enumerate(board):
            # j is index of column, c is char
            for j, c in enumerate(r):
                if c == ".":
                    continue
                    
                sqIndex = (i // 3) * 3 + (j // 3)   
     
                if c in colDict[j] or c in rowDict[i] or c in sqDict[sqIndex]:
                    return False

                colDict[j].append(c)
                rowDict[i].append(c)
                sqDict[sqIndex].append(c)
        return True


        
        