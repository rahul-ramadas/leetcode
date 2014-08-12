class Solution {
public:
    vector<vector<int>> fourSum(vector<int>& num, int target)
    {
        sort(num.begin(), num.end());
        vector<vector<int>> solutions;
        size_t i = 0;
        while (i < num.size())
        {
            size_t j = i + 1;
            
            while (j < num.size())
            {
                size_t k = j + 1;
                size_t l = num.size() - 1;
                int remaining_sum = target - num[i] - num[j];
                
                while (k < l)
                {
                    int trial_sum = num[k] + num[l];
                    if (trial_sum > remaining_sum)
                    {
                        --l;
                    }
                    else if (trial_sum < remaining_sum)
                    {
                        ++k;
                    }
                    else
                    {
                        solutions.emplace_back(vector<int>{num[i], num[j], num[k], num[l]});
                        ++k;
                        while ((k < l) && (num[k] == num[k - 1]))
                        {
                            ++k;
                        }
                    }
                }
                
                ++j;
                while ((j < num.size()) && (num[j] == num[j - 1]))
                {
                    ++j;
                }
            }
            
            ++i;
            while ((i < num.size()) && (num[i] == num[i - 1]))
            {
                ++i;
            }
        }
        
        return solutions;
    }
};
