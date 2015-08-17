class Solution {
public:

    void findCombinations(vector<vector<int>>& Solutions, vector<int>& Current, int K, int N, int Next)
    {
        if (Current.size() == K)
        {
            int sum = std::accumulate(Current.cbegin(), Current.cend(), 0);
            if (sum == N)
            {
                Solutions.push_back(Current);
            }
            return;
        }
        
        for (int i = Next; i <= 9; ++i)
        {
            Current.push_back(i);
            findCombinations(Solutions, Current, K, N, i + 1);
            Current.pop_back();
        }
    }
    
    vector<vector<int>> combinationSum3(int k, int n) {
        vector<vector<int>> solutions;
        vector<int> current;
        findCombinations(solutions, current, k, n, 1);
        return solutions;
    }
};
