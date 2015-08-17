class Solution:
    # @param {integer} num
    # @return {integer}
    def addDigits(self, num):
        if not num:
            return 0
            
        if num % 9 == 0:
            return 9
            
        return num % 9
