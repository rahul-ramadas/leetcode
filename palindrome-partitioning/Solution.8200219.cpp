class Solution
{
public:
    bool isPalindrome(string::const_iterator begin, string::const_iterator end)
    {
        return equal(begin, end, reverse_iterator<string::const_iterator>(end));
    }

    void findPartitions(const string& s, string::const_iterator from, vector<pair<string::const_iterator, string::const_iterator>>& currentPartition, vector<vector<string>>& partitions)
    {
        if (from == s.cend())
        {
            vector<string> solution;
            for (auto& p : currentPartition)
            {
                solution.emplace_back(p.first, p.second);
            }

            partitions.push_back(std::move(solution));
            return;
        }

        for (auto i = from; i != s.cend();)
        {
            ++i;
            if (!isPalindrome(from, i))
            {
                continue;
            }

            currentPartition.push_back(make_pair(from, i));
            findPartitions(s, i, currentPartition, partitions);
            currentPartition.pop_back();
        }
    }

    vector<vector<string>> findPartitions(const string& s)
    {
        vector<vector<string>> partitions;
        vector<pair<string::const_iterator, string::const_iterator>> currentPartition;
        findPartitions(s, s.cbegin(), currentPartition, partitions);

        return partitions;
    }

    vector<vector<string>> partition(string s)
    {
        return findPartitions(s);
    }
};
