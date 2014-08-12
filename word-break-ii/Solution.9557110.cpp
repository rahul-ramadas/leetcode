class Solution {
public:

    void buildSolutions(vector<string>& solutions, const vector<vector<int>>& nextIndices, string& currentString, const string& s, size_t index)
    {
        if (index == s.length())
        {
            solutions.push_back(currentString);
            return;
        }

        for (auto nextInd : nextIndices[index])
        {
            string nextString;
            if (currentString.empty())
            {
                nextString = s.substr(index, nextInd - index);
            }
            else
            {
                nextString = currentString + " " + s.substr(index, nextInd - index);
            }

            buildSolutions(solutions, nextIndices, nextString, s, nextInd);
        }
    }

    vector<string> wordBreak(string s, unordered_set<string> &dict) {

        vector<vector<int>> nextIndices(s.length(), vector<int>());

        for (size_t i = s.length(); i-- > 0;)
        {
            for (size_t j = i + 1; j <= s.length(); ++j)
            {
                string word = s.substr(i, j - i);
                if (dict.find(word) == dict.cend())
                {
                    continue;
                }

                if (j == s.length() || !nextIndices[j].empty())
                {
                    nextIndices[i].push_back(static_cast<int>(j));
                }
            }
        }

        vector<string> solutions;
        string currentString;
        buildSolutions(solutions, nextIndices, currentString, s, 0);

        return solutions;
    }
};
