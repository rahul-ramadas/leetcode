class Solution(object):
    def isUgly(self, num):
        if not num:
            return False

        for factor in (2, 3, 5):
            while num % factor == 0:
                num /= factor
                
        return num == 1
