class Solution:

    def longestPalindrome(self, s):
        n = len(s)
        p = [0] * (2*n + 1)

        def get(i):
            if i % 2 == 0:
                return ""
            return s[i / 2]

        c = 0
        r = 0

        for i in xrange(1, len(p)):
            id = 2*c - i

            if id < 0:
                t = 0
            else:
                t = p[id]

            if i + t < r:
                p[i] = t
                continue

            p[i] = max(0, r - i)
            k = i + p[i] + 1
            kd = 2*i - k
            while k < len(p) and kd >= 0 and get(kd) == get(k):
                k += 1
                kd -= 1
                p[i] += 1

            c = i
            r = k - 1

        index, max_val = max(enumerate(p), key=operator.itemgetter(1))

        start_pos = (index - max_val + 1) / 2
        return s[start_pos:start_pos + max_val]
