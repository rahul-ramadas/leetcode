class Solution:

    def shortestPalindrome(self, s):
        fake_string = s + "#" + s[::-1]
        lps = longest_proper_prefix_suffix(fake_string)
        longest_prefix_length = lps[len(fake_string)]
        print(longest_prefix_length)
        num_chars_to_add = len(s) - longest_prefix_length
        str_to_add = s[:-num_chars_to_add - 1:-1]
        result = str_to_add + s
        return result


def longest_proper_prefix_suffix(pattern):
    """Construct table of longest proper prefix that is also
    a suffix for each length of the pattern
    """

    lps = [0] * (len(pattern) + 1)
    lps[0] = -1
    lps[1] = 0

    cur_prefix_len = 0
    pattern_sublen = 2
    while pattern_sublen <= len(pattern):
        index = pattern_sublen - 1
        if pattern[index] == pattern[cur_prefix_len]:
            cur_prefix_len += 1
            lps[pattern_sublen] = cur_prefix_len
            pattern_sublen += 1
        elif cur_prefix_len:
            cur_prefix_len = lps[cur_prefix_len]
        else:
            lps[pattern_sublen] = 0
            pattern_sublen += 1

    return lps
