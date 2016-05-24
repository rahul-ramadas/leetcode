class Solution(object):
    def isPowerOfFour(self, num):
        if num == 0:
            return False
        if (num & (num - 1)):
            return False
        if (num & 0xAAAAAAAA):
            return False
        return True
