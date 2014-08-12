class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of integers
    def spiralOrder(self, matrix):
        if not matrix:
            return []

        m = len(matrix)
        n = len(matrix[0])
        ints = [0] * (m * n)
        count = 0
        
        i = 0
        j = 0

        while m > 0 and n > 0:
            
            for c in xrange(n):
                ints[count] = matrix[i][j + c]
                count += 1
                
            j += n - 1
            if m == 1:
                break
            
            for c in xrange(1, m):
                ints[count] = matrix[i + c][j]
                count += 1
                
            i += m - 1
            if n == 1:
                break
            
            for c in xrange(1, n):
                ints[count] = matrix[i][j - c]
                count += 1
                
            j -= n - 1
            
            for c in xrange(1, m - 1):
                ints[count] = matrix[i - c][j]
                count += 1
                
            i -= m - 2
            j += 1
            
            m -= 2
            n -= 2
            
        return ints
