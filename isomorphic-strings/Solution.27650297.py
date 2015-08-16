class Solution:
    # @param {string} s
    # @param {string} t
    # @return {boolean}
    def isIsomorphic(self, s, t):
        mapping = dict()
        mapped = set()
        
        for a, b in zip(s, t):
            if a in mapping:
                if mapping[a] != b:
                    return False
            elif b in mapped:
                return False
            else:
                mapping[a] = b
                mapped.add(b)
                
        return True
