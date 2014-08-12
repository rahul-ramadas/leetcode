class Solution
{
public:

    int minDistance(string word1, string word2)
    {
        vector<vector<int>> dp(word1.length() + 1, vector<int>(word2.length() + 1, 0));

        for (size_t i = 0; i < dp[0].size(); ++i)
        {
            dp[0][i] = i;
        }

        for (size_t i = 0; i < dp.size(); ++i)
        {
            dp[i][0] = i;
        }

        for (size_t i = 1; i <= word1.length(); ++i)
        {
            for (size_t j = 1; j <= word2.length(); ++j)
            {
                int del = dp[i - 1][j] + 1;
                int add = dp[i][j - 1] + 1;
                int rep = dp[i - 1][j - 1] + ((word1[i - 1] == word2[j - 1]) ? 0 : 1);

                dp[i][j] = min(del, min(add, rep));
            }
        }

        return dp[word1.length()][word2.length()];
    }
};
