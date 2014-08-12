class Solution
{
public:

    vector<pair<int, int>> getNumGroups(vector<int> num)
    {
        sort(num.begin(), num.end());

        vector<pair<int, int>> numGroups;

        for (auto i : num)
        {
            if (numGroups.empty() || (numGroups.back().first != i))
            {
                numGroups.push_back(make_pair(i, 1));
            }
            else
            {
                ++numGroups.back().second;
            }
        }

        return numGroups;
    }

    void findSolutions(vector<pair<int, int>> numGroups, size_t index, vector<int>& solution, int currentSum, int target, vector<vector<int>>& solutions)
    {
        if (currentSum == target)
        {
            solutions.push_back(solution);
            return;
        }

        if (currentSum > target)
        {
            return;
        }

        if (index == numGroups.size())
        {
            return;
        }

        for (size_t i = index; i < numGroups.size(); ++i)
        {
            for (int j = 1; j <= numGroups[i].second; ++j)
            {
                for (int k = 1; k <= j; ++k)
                {
                    solution.push_back(numGroups[i].first);
                }

                findSolutions(numGroups, i + 1, solution, currentSum + numGroups[i].first * j, target, solutions);

                solution.erase(solution.end() - j, solution.end());
            }
        }
    }

    vector<vector<int>> combinationSum2(vector<int> &num, int target)
    {
        auto numGroups = getNumGroups(num);

        vector<vector<int>> solutions;
        vector<int> solution;

        findSolutions(numGroups, 0, solution, 0, target, solutions);
        return solutions;
    }
};
