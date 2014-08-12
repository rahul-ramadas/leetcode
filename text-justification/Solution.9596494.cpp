class Solution {
public:
    vector<string> fullJustify(vector<string> &words, int L) {
        size_t start = 0;
        size_t end = 0;
        vector<string> result;
        
        while (start < words.size())
        {
            size_t currentLen = words[end++].length();
            while((end < words.size()) && ((currentLen + 1 + words[end].length()) <= L))
            {
                currentLen += 1 + words[end].length();
                ++end;
            };
            
            size_t numWords = end - start;
            size_t freeSpaces = L - currentLen + numWords - 1;
            
            string line;
            
            if ((numWords == 1) || (end == words.size()))
            {
                line = words[start];
                for (size_t i = start + 1; i < end; ++i)
                {
                    line += ' ' + words[i];
                }
                line += string(L - currentLen, ' ');
            }
            else
            {
                line = words[start];
                for (size_t i = start + 1; i < end; ++i)
                {
                    size_t spaces = (freeSpaces + end - i - 1) / (end - i);
                    line += string(spaces, ' ');
                    line += words[i];
                    freeSpaces -= spaces;
                }
            }
            
            result.emplace_back(std::move(line));
            start = end;
        }
        
        return result;
    }
};
