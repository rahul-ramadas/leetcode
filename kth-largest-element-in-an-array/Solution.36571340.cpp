class Solution
{
public:

    int
    findKthLargest (
        vector<int>& nums,
        int k
        )
    {
        if (nums.size() == 1)
        {
            return nums[0];
        }

        auto start = nums.begin();
        auto end = nums.end();

        while (true)
        {
            int pivot = *(end - 1);
            auto pred = [pivot](const int& val) { return val < pivot; };

            auto pivotIt = std::partition(start, end - 1, pred);

            if (pivotIt != (end - 1))
            {
                swap(*pivotIt, *(end - 1));
            }

            int position = nums.cend() - pivotIt;
            if (position == k)
            {
                return pivot;
            }
            else if (position < k)
            {
                end = pivotIt;
            }
            else
            {
                start = pivotIt + 1;
            }
        }
    }
};
