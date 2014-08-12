class Solution
{
public:

    bool isScramble(string s1, string s2)
    {
        if (s1.length() != s2.length())
        {
            return false;
        }

        if (s1.empty())
        {
            return true;
        }

        size_t len = s1.length();
        vector<vector<vector<bool>>> dp(len, vector<vector<bool>>(len, vector<bool>(len + 1, false)));

        for (size_t i = 0; i < len; ++i)
        {
            for (size_t j = 0; j < len; ++j)
            {
                dp[i][j][1] = (s1[i] == s2[j]);
            }
        }

        for (size_t subLength = 2; subLength <= len; ++subLength)
        {
            for (size_t i = 0; i <= (len - subLength); ++i)
            {
                for (size_t j = 0; j <= (len - subLength); ++j)
                {
                    for (size_t offset = 0; (offset < (subLength - 1)) && !dp[i][j][subLength]; ++offset)
                    {
                        size_t len1 = offset + 1;
                        size_t len2 = subLength - len1;

                        dp[i][j][subLength] = (dp[i][j][len1] && dp[i + len1][j + len1][len2]) ||
                            (dp[i][j + len2][len1] && dp[i + len1][j][len2]);
                    }
                }
            }
        }

        return dp[0][0][len];
    }
};
