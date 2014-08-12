class Solution:

    def longestConsecutive(self, num):
        range_length = collections.defaultdict(int)
        max_length = 0

        for n in num:
            if range_length[n] != 0:
                continue

            range_length[n] = 1
            left_length = range_length[n - 1]
            right_length = range_length[n + 1]
            new_length = left_length + right_length + 1
            range_length[n - left_length] = range_length[n + right_length] = new_length
            max_length = max(max_length, new_length)

        return max_length
