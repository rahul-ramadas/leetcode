class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int len = nums.size();
        vector<int> solution(len, 0);
        solution[0] = 1;
        for (int i = 1; i < len; ++i)
        {
            solution[i] = solution[i - 1] * nums[i - 1];
        }
        
        int rem = 1;
        for (int i = len - 1; i >= 0; --i)
        {
            solution[i] *= rem;
            rem *= nums[i];
        }
        
        return solution;
    }
};
