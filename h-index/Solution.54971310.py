class Solution:

    def hIndex(self, citations):
        n = len(citations)
        at_least = [citations.count(i) for i in xrange(n + 1)]
        at_least.append(n - sum(at_least))
        for i in xrange(n, -1, -1):
            at_least[i] += at_least[i + 1]

        for i in xrange(n, -1, -1):
            if at_least[i] >= i:
                return i
