class Solution:
    def singleNumber(self, A):
        ones = 0
        twos = 0
        for number in A:
            temp = number & twos
            twos ^= temp
            number ^= temp
            temp = number & ones
            twos |= temp
            ones ^= temp
            number ^= temp
            ones |= number
            number ^= ones
        return ones
