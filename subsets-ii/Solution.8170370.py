class Solution:

    def subsetsWithDup(self, num):
        num.sort()
        num_groups = [(k, sum(1 for i in g)) for k, g in itertools.groupby(num)]

        subsets = [[]]

        for num, count in num_groups:
            subset_length = len(subsets)
            for i in xrange(count):
                subsets.extend([s + [num] for s in subsets[-subset_length:]])

        return subsets
