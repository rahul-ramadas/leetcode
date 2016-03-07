class Solution:

    def removeInvalidParentheses(self, s):
        if self.is_valid_parens(s):
            return [s]

        search_set = set()
        search_set.add(s)
        solution = set()

        while not solution:
            search_set2 = set()
            for str in search_set:
                for i in xrange(len(str)):
                    if str[i] != "(" and str[i] != ")":
                        continue
                    trial = str[:i] + str[i + 1:]
                    if self.is_valid_parens(trial):
                        solution.add(trial)
                    if not solution:
                        search_set2.add(trial)
            search_set = search_set2

        return list(solution)

    def is_valid_parens(self, s):
        count = 0
        for c in s:
            if c == "(":
                count += 1
            elif c == ")":
                if count == 0:
                    return False
                count -= 1

        if count != 0:
            return False
        return True
