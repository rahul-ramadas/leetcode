class Solution:

    def subsets(self, S):
        result = [[]]
        S = sorted(S)
        for n in S:
            for i in xrange(len(result)):
                ss = result[i][:] + [n]
                result.append(ss)

        return result
