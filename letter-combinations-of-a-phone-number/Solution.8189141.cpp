class Solution
{
public:

    vector<string> letterCombinations(string digits)
    {
        vector<string> letterMap{ "", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz" };
        vector<string> solutions;

        buildSolutions(digits, letterMap, solutions);
        return solutions;
    }

private:

    void buildSolutions(const string& digits, size_t index, string& currentSolution, const vector<string>& letterMap, vector<string>& solutions)
    {
        if (index == digits.length())
        {
            solutions.push_back(currentSolution);
            return;
        }

        for (auto c : letterMap[digits[index] - '0'])
        {
            currentSolution += c;
            buildSolutions(digits, index + 1, currentSolution, letterMap, solutions);
            currentSolution.pop_back();
        }
    }

    void buildSolutions(const string& digits, const vector<string>& letterMap, vector<string>& solutions)
    {
        string currentSolution;
        buildSolutions(digits, 0, currentSolution, letterMap, solutions);
    }
};
