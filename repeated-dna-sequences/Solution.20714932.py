import collections
import itertools


class Solution:

    def findRepeatedDnaSequences(self, s):
        if len(s) < 10:
            return []

        seq = collections.deque(itertools.islice(s, 0, 9), 10)
        result = []

        seq_dict = dict()
        for c in itertools.islice(s, 9, None):
            seq.append(c)
            seq_str = "".join(seq)
            count = seq_dict.get(seq_str, None)
            if count is None:
                seq_dict[seq_str] = 1
            elif count == 1:
                seq_dict[seq_str] = 2
                result.append(seq_str)

        return result
