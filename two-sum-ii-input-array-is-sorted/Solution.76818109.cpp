class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        if (numbers.size() < 2)
        {
            return {{0, 0}};
        }
        
        size_t index1 = 0;
        size_t index2 = numbers.size() - 1;
        
        do
        {
            unsigned long long currentSum = (unsigned long long)numbers[index1] + numbers[index2];
            
            if (currentSum == target)
            {
                break;
            }
            
            if (currentSum > target)
            {
                --index2;
            }
            else
            {
                ++index1;
            }
        } while (true);
        
        return {{index1 + 1, index2 + 1}};
    }
};
