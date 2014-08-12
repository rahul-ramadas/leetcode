class Solution {
public:

    typedef unordered_multimap<string, bool> WordMap;

    WordMap createMultiMap(const vector<string>& L)
    {
        WordMap usedWords;

        for (auto& s : L)
        {
            usedWords.insert(make_pair(s, false));
        }
        
        return usedWords;
    }

    bool updateMultiMap(WordMap& usedWords, const string& word, bool used)
    {
        bool wordExists;
        return updateMultiMap(usedWords, word, used, wordExists);
    }

    bool updateMultiMap(WordMap& usedWords, const string& word, bool used, bool& wordExists)
    {
        auto range = usedWords.equal_range(word);
        if (range.first == range.second)
        {
            wordExists = false;
            return false;
        }

        wordExists = true;

        auto it = range.first;
        for (; it != range.second; ++it)
        {
            if (it->second != used)
            {
                break;
            }
        }

        if (it == range.second)
        {
            return false;
        }

        usedWords.erase(it);
        usedWords.insert(make_pair(word, used));
        return true;
    }

    void removeUsedWords(const string& s, size_t start, size_t end, size_t wordLength, WordMap& usedWords)
    {
        for (size_t i = start; i < end; i += wordLength)
        {
            string word = s.substr(i, wordLength);
            updateMultiMap(usedWords, word, false);
        }
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
        
        auto usedWords = createMultiMap(L);
        
        for (size_t i = 0; i < wordLength; ++i)
        {
            if (i + sequenceLength > S.length())
            {
                break;
            }
            
            size_t start = i;
            size_t end = i;
            size_t foundWords = 0;
            
            while (end + wordLength <= S.length())
            {
                string word = S.substr(end, wordLength);
                bool wordExists;
                if (!updateMultiMap(usedWords, word, true, wordExists))
                {
                    if (!wordExists)
                    {
                        foundWords = 0;
                        removeUsedWords(S, start, end, wordLength, usedWords);
                        start = end + wordLength;
                        end = start;
                        if (start + sequenceLength > S.length())
                        {
                            break;
                        }
                        continue;
                    }
                    else
                    {
                        do
                        {
                            --foundWords;
                            removeUsedWords(S, start, start + wordLength, wordLength, usedWords);
                            start += wordLength;
                        } while (!updateMultiMap(usedWords, word, true));
                    }
                }
                
                ++foundWords;
                if (foundWords == numWords)
                {
                    result.push_back(static_cast<int>(start));
                    removeUsedWords(S, start, start + wordLength, wordLength, usedWords);
                    --foundWords;
                    start += wordLength;
                }
                
                end += wordLength;
            }
        }
        
        return result;
    }
};
