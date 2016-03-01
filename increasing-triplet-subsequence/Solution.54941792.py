class Solution:

    def increasingTriplet(self, nums):
        max_len = 0
        c1 = 0
        c2 = 0

        def find_len(x):
            if max_len == 2 and c2 < x:
                return 2
            elif max_len >= 1 and c1 < x:
                return 1
            return 0

        for n in nums:
            prev_len = find_len(n)
            new_len = prev_len + 1
            if new_len == 1:
                c1 = n
            elif new_len == 2:
                c2 = n
            max_len = max(max_len, new_len)
            if max_len == 3:
                return True

        return False
