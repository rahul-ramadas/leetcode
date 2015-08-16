class Solution:
    # @param m, an integer
    # @param n, an integer
    # @return an integer
    def rangeBitwiseAnd(self, m, n):
        result = 0
        count = n - m + 1
        for b in range(n.bit_length()):
            if self.is_bit_set(m, b) and \
               self.is_bit_set(n, b) and \
               count <= 2 ** b:
                   result |= 2 ** b
                   
        return result
        
    def is_bit_set(self, n, b):
        return (n & (2 ** b)) != 0
