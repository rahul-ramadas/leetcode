class Solution {
public:
    
    void getLetterCounts(const string& T, size_t (&counts)[256])
    {
        for (auto c : T)
        {
            ++counts[c];
        }
    }

    string minWindow(string S, string T) {
        size_t counts[256] = {};
        getLetterCounts(T, counts);
        size_t tempCounts[256] = {};
        size_t window = S.length() + 1;
        string windowString;

        size_t start = 0;
        size_t end = 0;
        size_t found = 0;
        
        while (end < S.length())
        {
            char c = S[end];

            if (!counts[c])
            {
                if (found)
                {
                    ++end;
                }
                else
                {
                    ++start;
                    ++end;
                }
            }
            else
            {
                if (tempCounts[c] < counts[c])
                {
                    ++found;
                }
                
                ++tempCounts[c];
                ++end;
            }
            
            c = S[start];
            while ((start < end) && ((tempCounts[c] > counts[c]) || (!counts[c])))
            {
                if (counts[c])
                {
                    --tempCounts[c];
                }
                
                ++start;
                c = S[start];
            }
            
            if (found == T.length())
            {
                if (window > end - start)
                {
                    window = end - start;
                    windowString = S.substr(start, end - start);
                }
            }
        }
        
        if (window == S.length() + 1)
        {
            return "";
        }
        return windowString;
    }
};
