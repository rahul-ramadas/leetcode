class Solution:

    def is_interleave_cached(original_func):
        def new_func(self, s1, i, s2, j, s3, k):
            res = self.cache.get((i, j, k), None)
            if res is not None:
                return res
            res = original_func(self, s1, i, s2, j, s3, k)
            self.cache[(i, j, k)] = res
            return res
        return new_func

    @is_interleave_cached
    def is_interleave(self, s1, i, s2, j, s3, k):
        if k == len(s3):
            if i != len(s1) or j != len(s2):
                return False
            return True

        if i != len(s1) and s1[i] == s3[k]:
            result = self.is_interleave(s1, i + 1, s2, j, s3, k + 1)
            if result:
                return True

        if j != len(s2) and s2[j] == s3[k]:
            result = self.is_interleave(s1, i, s2, j + 1, s3, k + 1)
            if result:
                return True

        return False

    def isInterleave(self, s1, s2, s3):
        if len(s1) + len(s2) != len(s3):
            return False
            
        dp = [[False]*(len(s2) + 1) for _ in xrange(len(s1) + 1)]
        dp[len(s1)][len(s2)] = True
        
        for i in xrange(len(s1), -1, -1):
            for j in xrange(len(s2), -1, -1):
                if i == len(s1) and j == len(s2):
                    continue
                
                k = len(s3) - ((len(s1) - i) + (len(s2) - j))
                
                if i != len(s1) and s1[i] == s3[k]:
                    if dp[i + 1][j]:
                        dp[i][j] = True
                        
                if j != len(s2) and s2[j] == s3[k]:
                    if dp[i][j + 1]:
                        dp[i][j] = True
                        
        return dp[0][0]
