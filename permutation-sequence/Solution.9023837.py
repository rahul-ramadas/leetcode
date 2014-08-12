class Solution:

    def getPermutation(self, n, k):
        count = math.factorial(n)
        k -= 1
        digits = [str(i) for i in xrange(1, n + 1)]
        permutation = []

        for i in xrange(n):
            count /= n - i
            index = k / count
            permutation += digits[index]
            del digits[index]
            k %= count

        return ''.join(permutation)
