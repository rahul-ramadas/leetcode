class Solution:
    def searchMatrix(self, matrix, target):
        if not matrix:
            return False

        rows = len(matrix)
        cols = len(matrix[0])
        elems = rows * cols

        def get_element(n):
            row = n / cols
            col = n % cols
            return matrix[row][col]

        lower = 0
        upper = elems
        while lower < upper:
            middle = (upper + lower) / 2
            elem = get_element(middle)
            if elem == target:
                return True
            elif elem < target:
                lower = middle + 1
            elif elem > target:
                upper = middle

        return False
