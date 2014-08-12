class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permuteUnique(self, num):
        return map(list, list(set(itertools.permutations(num))))
