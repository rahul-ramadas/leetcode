class Solution:
    def next_permutation(self, permutation):
        pass

    def permute(self, num):
        permutations = []
        permutation = sorted(num)

        for p in itertools.permutations(permutation):
            permutations.append(list(p))

        return permutations
