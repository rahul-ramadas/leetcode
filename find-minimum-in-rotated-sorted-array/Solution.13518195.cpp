class Solution {
public:
    int findMin(vector<int> &num) {
        int low = 0;
        int high = num.size() - 1;
        
        while (low < high)
        {
            if (num[low] < num[high])
            {
                return num[low];
            }
            
            int middle = low + (high - low) / 2;
            
            if (num[middle] >= num[low])
            {
                low = middle + 1;
            }
            else // if (num[middle] < num[low])
            {
                high = middle;
            }
        }
        
        return num[low];
    }
};
