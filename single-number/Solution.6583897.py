class Solution:

    def singleNumber(self, A):
        extraNumber = reduce(lambda x, y: x ^ y, A)
        return extraNumber
