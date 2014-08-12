class Solution {
public:
    int minCut(string s) {
        if (s.empty())
        {
            return 0;
        }

        size_t n = s.length();
        vector<vector<bool>> isPalindrome(n, vector<bool>(n, false));

        for (size_t i = 0; i < n - 1; ++i)
        {
            isPalindrome[i][i] = true;
            isPalindrome[i][i + 1] = (s[i] == s[i + 1]);
        }
        isPalindrome[n - 1][n - 1] = true;

        for (size_t len = 3; len <= n; ++len)
        {
            for (size_t i = 0; i <= (n - len); ++i)
            {
                isPalindrome[i][i + len - 1] = ((s[i] == s[i + len - 1]) && isPalindrome[i + 1][i + len - 2]);
            }
        }

        vector<int> minCuts(n, static_cast<int>(n));
        for (size_t i = n; i-- > 0;)
        {
            for (size_t j = i; j < n; ++j)
            {
                if (!isPalindrome[i][j])
                {
                    continue;
                }

                if (j == n - 1)
                {
                    minCuts[i] = 0;
                }
                else
                {
                    minCuts[i] = min(minCuts[i], 1 + minCuts[j + 1]);
                }
            }
        }

        return minCuts[0];
    }
};
