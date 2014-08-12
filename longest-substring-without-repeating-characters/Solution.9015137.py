class Solution:

    def lengthOfLongestSubstring(self, s):
        begin = 0
        end = 0
        letter_index = {}
        max_len = 0

        for i in xrange(len(s)):
            c = s[i]
            if c not in letter_index or letter_index[c] < begin:
                letter_index[c] = i
                end += 1
                max_len = max(max_len, end - begin)
            else:
                begin = letter_index[c] + 1
                end += 1
                letter_index[c] = i

        return max_len
