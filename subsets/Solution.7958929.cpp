class Solution
{
public:

    vector<int> GetSubset(const vector<int>& S, const vector<bool>& Selection)
    {
        vector<int> set;
        for (size_t i = 0; i < Selection.size(); ++i)
        {
            if (Selection[i])
            {
                set.push_back(S[i]);
            }
        }

        return set;
    }

    bool NextSelection(vector<bool>& Selection)
    {
        size_t numToSelect = 0;
        size_t i;

        for (i = Selection.size(); i-- > 0; )
        {
            if (!Selection[i])
            {
                continue;
            }

            if (((i + 1) == Selection.size()) || (Selection[i + 1]))
            {
                ++numToSelect;
                continue;
            }

            Selection[i] = false;
            Selection[i + 1] = true;

            i += 2;
            break;
        }

        if (!numToSelect)
        {
            return true;
        }

        if (i >= Selection.size())
        {
            return false;
        }

        for (; i < Selection.size(); ++i)
        {
            if (numToSelect)
            {
                Selection[i] = true;
                --numToSelect;
            }
            else
            {
                Selection[i] = false;
            }
        }

        return true;
    }

    void AddAllCombinations(const vector<int>& S, size_t Length, vector<vector<int>>& Result)
    {
        vector<int> combination(Length, 0);
        vector<bool> selection(S.size(), false);
        for (size_t i = 0; i < Length; ++i)
        {
            selection[i] = true;
        }

        do
        {
            Result.push_back(GetSubset(S, selection));
        } while (NextSelection(selection));
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