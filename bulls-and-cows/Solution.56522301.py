class Solution:

    def getHint(self, secret, guess):
        secret = [ord(c) - ord("0") for c in secret]
        guess = [ord(c) - ord("0") for c in guess]
        secret_counts = [secret.count(i) for i in xrange(10)]
        guess_counts = [guess.count(i) for i in xrange(10)]
        bulls_count = [0] * 10

        for x, y in zip(secret, guess):
            if x == y:
                bulls_count[x] += 1

        cows_count = [min(secret_counts[i], guess_counts[i]) - bulls_count[i] for i in xrange(10)]

        return str(sum(bulls_count)) + "A" + str(sum(cows_count)) + "B"
