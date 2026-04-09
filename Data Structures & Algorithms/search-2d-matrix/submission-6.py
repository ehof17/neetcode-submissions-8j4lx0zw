class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # first, check if there is a row that starts smaller or equal and ends bigger or equal to targ

        L = 0
        R = len(matrix[0])-1

        top = 0
        bottom = len(matrix)-1
        mid = 0
        while top <= bottom:
            mid = (top+bottom)//2
            if matrix[mid][L] <= target <= matrix[mid][R]:
                break
            elif matrix[mid][L]> target:
                bottom = mid-1
            elif matrix[mid][R]<target:
                top = mid+1
        else:
            return False
      
        # value should be in mid
        matrix_row = matrix[mid]
        L2, R2 = 0, len(matrix_row)-1
        while L2 <= R2:
            mid2 = (L2+R2)//2
            if matrix_row[mid2]==target:
                return True
            elif matrix_row[mid2]>target:
                R2 = mid2-1
            elif matrix_row[mid2]<target:
                L2 = mid2+1

        return False

