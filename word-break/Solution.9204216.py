class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a boolean
    def wordBreak(self, s, dict):
        words = set(dict)
        can_segment = [False] * (len(s) + 1)
        can_segment[0] = True
        
        for i in xrange(1, len(s) + 1):
            for j in xrange(1, i + 1):
                if not can_segment[i - j]:
                    continue
                
                begin = len(s) - i
                end = begin + j
                word = s[begin:end]
                if word not in words:
                    continue
                
                can_segment[i] = True
                break
                
        return can_segment[len(s)]
