class Solution:

    def hIndex(self, citations):
        n = len(citations)
        at_least = [0] * (n + 2)
        for c in citations:
            at_least[min(c, n + 1)] += 1
        for i in xrange(n, -1, -1):
            at_least[i] += at_least[i + 1]

        for i in xrange(n, -1, -1):
            if at_least[i] >= i:
                return i
