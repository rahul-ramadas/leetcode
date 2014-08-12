class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a list of strings
    def wordBreak(self, s, words):
        solutions = []

        for i in xrange(len(s) - 1, -1, -1):
            maxlen = len(s) - i
            for j in xrange(i + 1, len(s) + 1):
                word = s[i:j]
                if word not in words:
                    continue

                if len(word) == maxlen:
                    solutions.append([word])
                else:
                    for k in xrange(len(solutions)):
                        totallen = len(word) + sum(len(w) for w in solutions[k])
                        if totallen == maxlen:
                            solutions.append(solutions[k] + [word])

        for i in xrange(len(solutions) - 1, -1, -1):
            totallen = sum(len(w) for w in solutions[i])
            if totallen != len(s):
                del solutions[i]

        solutions = [' '.join(reversed(s)) for s in solutions]
        return solutions
