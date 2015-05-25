class Solution {
public:

    int rob(const vector<int>& nums, size_t start, size_t end)
    {
        int a = 0;
        int b = 0;
        
        for (size_t i = start; i < end; ++i)
        {
            int c = max(a + nums[i], b);
            a = b;
            b = c;
        }
        
        return max(a, b);
    }
    
    int rob(vector<int>& nums) {
        if (nums.empty())
        {
            return 0;
        }
        
        if (nums.size() == 1)
        {
            return nums[0];
        }
        
        int sol1 = rob(nums, 0, nums.size() - 1);
        int sol2 = rob(nums, 1, nums.size());
        
        return max(sol1, sol2);
    }
};
