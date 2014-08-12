class Solution:
    def build_permutations(self, permutation, index, used_numbers, permutations):
        if index == len(permutation):
            permutations.append(permutation[:])
            return

        for k, v in used_numbers.copy().items():
            if v:
                continue

            used_numbers[k] = True
            permutation[index] = k
            self.build_permutations(permutation, index + 1, used_numbers, permutations)
            used_numbers[k] = False

    def permute(self, num):
        used_numbers = collections.OrderedDict({x: False for x in num})
        permutation = [0] * len(num)
        permutations = []
        self.build_permutations(permutation, 0, used_numbers, permutations)
        return permutations
