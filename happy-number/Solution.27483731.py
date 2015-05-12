class Solution:
    def split_digits(self, n):
        if n == 0:
            yield 0
            return
            
        while n != 0:
            yield n % 10
            n /= 10
            
    def next_happy(self, n):
        return sum(i * i for i in self.split_digits(n))
        
    # @param {integer} n
    # @return {boolean}
    def isHappy(self, n):
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = self.next_happy(n)
            
        if n == 1:
            return True
        return False
