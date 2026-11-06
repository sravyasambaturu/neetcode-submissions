class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows, cols = len(matrix), len(matrix[0])
        rowZero = False

        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    #mark the column 
                    matrix[0][c] = 0
                    if r > 0:
                        #if we find in other rows we mark the rows to be zero
                        matrix[r][0] = 0
                    else:
                        #if there are zeros in first row we flag them using True 
                        rowZero = True

        #we will make the ones we found zeros 
        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0

        
        #we tackle first column 
        if matrix[0][0] == 0:
            for r in range(rows):
                matrix[r][0] = 0

        #we tackle first row
        if rowZero:
            for c in range(cols):
                matrix[0][c] = 0