class Solution:
    def next_permutation(self, permutation):
        if len(permutation) == 1:
            return False

        i = len(permutation) - 2
        while i >= 0 and permutation[i] > permutation[i + 1]:
            i -= 1

        if i < 0:
            permutation.reverse()
            return False

        j = len(permutation) - 1
        while permutation[j] < permutation[i]:
            j -= 1

        permutation[i], permutation[j] = permutation[j], permutation[i]
        permutation[i + 1:] = permutation[-1:i:-1]
        return True

    def permute(self, num):
        permutations = []
        if not num:
            return permutations

        permutation = sorted(num)
        permutations.append(permutation[:])

        while self.next_permutation(permutation):
            permutations.append(permutation[:])

        return permutations
