class Solution:

    def subsets(self, S):
        result = [[]]
        S = sorted(S)
        for l in range(1, len(S) + 1):
            result.extend([list(c) for c in itertools.combinations(S, l)])

        return result
