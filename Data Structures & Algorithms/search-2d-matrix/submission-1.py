class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix[0])
        n = len(matrix)
        low = 0 
        high = (n * m) - 1
        while low <= high:
            mid = (low + high) // 2
            row = mid // m
            col =  mid % m
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                low = mid + 1
            else:
                high = mid - 1
        return False



# Let's say the binary search picks a midpoint index of mid = 6. 
# Remember, m = 4.row = 6 // 4 → 1 (4 goes into 6 exactly 1 time).col = 6 % 4 → 2 
# (the remainder of 6 divided by 4 is 2).Result: 1D index 6 maps exactly to Row 1, Column 2.
# m = len(matrix[0]) calculates the total number of columns in the matrix.