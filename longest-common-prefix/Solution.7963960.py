class Solution:

    def common_prefix(self, a, b):
        i = 0
        end = min(len(a), len(b))
        while i < end:
            if a[i] != b[i]:
                break
            i += 1

        return a[:i]

    def longestCommonPrefix(self, strs):
        if not strs:
            return ""

        longest = strs[0]

        for i in xrange(1, len(strs)):
            longest = self.common_prefix(longest, strs[i])
            if not longest:
                return ""

        return longest
