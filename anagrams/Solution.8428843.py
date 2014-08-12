class Solution:

    def anagrams(self, strs):
        key = lambda s: ''.join(sorted(s))

        strs = sorted(strs, key=key)
        strs = itertools.groupby(strs, key=key)
        result = []
        for k, g in strs:
            l = list(g)
            if len(l) == 1:
                continue
            result.extend(l)
        return result
