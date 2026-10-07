class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        lr, rr = 0, len(matrix) - 1
        mRow = 0

        while lr <= rr:
            mRow = (rr+lr) //2

            if  matrix[mRow][0]< target and matrix[mRow][-1]< target:
                lr = mRow + 1
            elif  matrix[mRow][0]> target and matrix[mRow][-1]> target:
                rr = mRow-1
            elif  matrix[mRow][0]<= target and matrix[mRow][-1]>= target:
                break
        else:
            return False
            

        lc, rc = 0, len(matrix[0]) -1
        mCol = 0
        while lc <= rc:
            mCol = (rc+lc) //2
            if matrix[mRow][mCol] < target:
                lc = mCol+1
            elif matrix[mRow][mCol] > target:
                rc = mCol-1
            elif matrix[mRow][mCol] == target:
                return True
        else:
            return False


        