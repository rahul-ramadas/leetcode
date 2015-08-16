class Solution:
    # @param {integer} n
    # @return {integer}
    def countPrimes(self, n):
        count = 0
        sieve = [False] * n
        
        for i in range(2, len(sieve)):
            if sieve[i]:
                continue
            
            count += 1
            
            j = i
            while i * j < len(sieve):
                sieve[i * j] = True
                j += 1
                
        return count
