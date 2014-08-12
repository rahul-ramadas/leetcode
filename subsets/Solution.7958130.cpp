class Solution
{
public:

    void BuildCombinationAndAdd(const vector<int>& S, size_t SmallestSelectIndex, size_t CurrentIndex, vector<int>& Combination, vector<vector<int>>& Result)
    {
        if (CurrentIndex == Combination.size())
        {
            Result.push_back(Combination);
            return;
        }

        size_t remaining = Combination.size() - CurrentIndex;
        for (size_t i = SmallestSelectIndex; i < (S.size() - remaining + 1); ++i)
        {
            Combination[CurrentIndex] = S[i];
            BuildCombinationAndAdd(S, i + 1, CurrentIndex + 1, Combination, Result);
        }
    }

    void AddAllCombinations(const vector<int>& S, size_t Length, vector<vector<int>>& Result)
    {
        vector<int> combination(Length, 0);
        BuildCombinationAndAdd(S, 0, 0, combination, Result);
    }

    vector<vector<int>> subsets(vector<int> &S)
    {
        sort(S.begin(), S.end());

        vector<vector<int>> result;
        result.push_back(vector<int>());

        for (size_t i = 1; i <= S.size(); ++i)
        {
            AddAllCombinations(S, i, result);
        }

        return result;
    }
};
