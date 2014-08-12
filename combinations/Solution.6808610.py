class Solution:
    def combine(self, n, k):
        return [list(elem) for elem in itertools.combinations(xrange(1, n + 1), k)]
