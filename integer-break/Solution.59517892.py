class Solution:

    def integerBreak(self, n):
        if n == 2:
            return 1
        if n == 3:
            return 2

        rem = n % 3
        product = 1

        if rem == 1:
            product = 4
            n -= 4
        elif rem == 2:
            product = 6
            n -= 5

        product *= 3 ** (n / 3)
        return product
