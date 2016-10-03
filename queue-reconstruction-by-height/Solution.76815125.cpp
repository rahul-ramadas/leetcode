class Solution
{
public:

    vector<pair<int, int>> reconstructQueue(vector<pair<int, int>>& people)
    {
        auto sortedPeople = people;

        std::sort(sortedPeople.begin(), sortedPeople.end(),
            [](const pair<int, int>& lhs, const pair<int, int>& rhs)
            {
                if (lhs.first != rhs.first)
                {
                    return (lhs.first > rhs.first);
                }

                return (lhs.second < rhs.second);
            });

        vector<pair<int, int>> solution;

        for (const auto& person : sortedPeople)
        {
            solution.insert(solution.begin() + person.second, person);
        }

        return solution;
    }
};
