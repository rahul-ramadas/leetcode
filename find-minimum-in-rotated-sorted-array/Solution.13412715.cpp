class Solution {
public:
    int findMin(vector<int> &num) {
        int low = 0;
        int high = num.size();

        int smallest = num[0];

        while (low < high)
        {
            if (num[low] < num[high - 1])
            {
                return min(num[low], smallest);
            }

            int middle = low + (high - low) / 2;
            smallest = min(smallest, num[middle]);

            if (num[middle] > num[low])
            {
                low = middle + 1;
            }
            else // if (num[middle] < num[low])
            {
                high = middle;
            }
        }

        return smallest;
    }
};
