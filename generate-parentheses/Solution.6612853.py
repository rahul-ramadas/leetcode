class Solution:
    def generateParenthesis(self, n):
        if n == 0:
            return []

        solution = [['(', ')']]

        for i in xrange(2, n + 1):
            newSolution = []
            for s in solution:
                for ind in xrange(0, len(s) + 1):
                    newS = s[:]
                    newS[ind:ind] = ['(', ')']
                    newSolution.append(newS)
            uniqueSols = {''.join(s) for s in newSolution}
            solution = [list(s) for s in uniqueSols]

        solution = [''.join(s) for s in solution]
        return solution
