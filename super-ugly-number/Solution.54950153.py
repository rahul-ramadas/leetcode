class Solution:

    def nthSuperUglyNumber(self, n, primes):
        indices = [0] * len(primes)
        uglies = [0] * n

        uglies[0] = 1

        for i in xrange(1, n):
            min_ugly = min((uglies[indices[j]] * primes[j] for j in xrange(len(primes))))
            for j in xrange(len(primes)):
                if uglies[indices[j]] * primes[j] == min_ugly:
                    indices[j] += 1
            uglies[i] = min_ugly

        return uglies[n - 1]
