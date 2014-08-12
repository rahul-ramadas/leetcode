class Solution {
public:

    unordered_map<string, size_t> createMap(const vector<string>& L)
    {
        unordered_map<string, size_t> countWords;

        for (auto& s : L)
        {
            ++countWords[s];
        }

        return countWords;
    }

    vector<int> findSubstring(string S, vector<string> &L) {
        vector<int> result;

        if (L.empty())
        {
            return result;
        }
        
        size_t wordLength = L[0].length();
        size_t numWords = L.size();
        size_t sequenceLength = wordLength * numWords;
        
        if (S.length() < sequenceLength)
        {
            return result;
        }
        
        auto countWords = createMap(L);
        
        for (size_t i = 0; i < wordLength; ++i)
        {
            if (i + sequenceLength > S.length())
            {
                break;
            }
            
            size_t start = i;
            size_t end = i;
            size_t foundWords = 0;
            unordered_map<string, size_t> tempCountWords;
            
            while (end + wordLength <= S.length())
            {
                string word = S.substr(end, wordLength);
                auto it = countWords.find(word);

                if (it == countWords.end())
                {
                    foundWords = 0;
                    tempCountWords.clear();
                    start = end + wordLength;
                    end = start;
                    if (start + sequenceLength > S.length())
                    {
                        break;
                    }
                }
                else if (it->second > tempCountWords[word])
                {
                    ++tempCountWords[word];
                    ++foundWords;
                    end += wordLength;
                }
                else
                {
                    string removeWord;
                    do
                    {
                        removeWord = S.substr(start, wordLength);
                        --tempCountWords[removeWord];
                        --foundWords;
                        start += wordLength;
                    } while (removeWord != word);
                    
                    ++tempCountWords[word];
                    ++foundWords;
                    end += wordLength;
                }
                
                if (foundWords == numWords)
                {
                    result.push_back(static_cast<int>(start));
                    string removeWord = S.substr(start, wordLength);
                    --tempCountWords[removeWord];
                    --foundWords;
                    start += wordLength;
                }
            }
        }
        
        return result;
    }
};
