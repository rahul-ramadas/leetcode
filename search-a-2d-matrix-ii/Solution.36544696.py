class Solution:
    # @param {integer[][]} matrix
    # @param {integer} target
    # @return {boolean}
    def searchMatrix(self, matrix, target):
        i = len(matrix) - 1
        j = 0
        
        while True:
            
            if matrix[i][j] == target:
                return True
                
            if matrix[i][j] < target:
                j += 1
            elif matrix[i][j] > target:
                i -= 1
                
            if i < 0 or j >= len(matrix[i]):
                return False
