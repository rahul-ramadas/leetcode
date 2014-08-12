class Solution {
public:
    int longestValidParentheses(string s) {
        if (s.empty())
        {
            return 0;
        }
        
        int maxLen = 0;
        int lastUnmatched = -1;
        stack<int> matching;
        
        for (int i = 0; i < s.length(); ++i)
        {
            if (s[i] == '(')
            {
                matching.push(i);
            }
            else // s[i] == ')'
            {
                if (matching.empty())
                {
                    lastUnmatched = i;
                }
                else
                {
                    matching.pop();
                    if (matching.empty())
                    {
                        maxLen = max(maxLen, i - lastUnmatched);
                    }
                    else
                    {
                        maxLen = max(maxLen, i - matching.top());
                    }
                }
            }
        }
        
        return maxLen;
    }
};
