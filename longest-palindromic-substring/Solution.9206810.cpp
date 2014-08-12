class Solution {
public:
    string longestPalindrome(string s) {
        static bool dp[1000][1001] = {};
        for (size_t i = 0; i < s.length(); ++i)
        {
            dp[i][0] = true;
            dp[i][1] = true;
        }
        
        size_t longest_len = 1;
        size_t longest_ind = 0;
        for (size_t len = 2; len <= s.length(); ++len)
        {
            for (size_t i = 0; i <= (s.length() - len); ++i)
            {
                if (s[i] == s[i + len - 1])
                {
                    dp[i][len] = dp[i + 1][len - 2];
                    if (dp[i][len])
                    {
                        longest_len = len;
                        longest_ind = i;
                    }
                }
                else
                {
                    dp[i][len] = false;
                }
            }
        }
        
        return s.substr(longest_ind, longest_len);
    }
};