class Solution
{
public:

    int
    partition (
        vector<int>& nums,
        int start,
        int end
        )
    {
        int pivot = nums[end - 1];
        int left = start;
        int right = end - 1;

        while (true)
        {
            while (left < end && nums[left] < pivot)
            {
                ++left;
            }

            while (right > left && nums[right] >= pivot)
            {
                --right;
            }

            if (left >= right)
            {
                break;
            }

            swap(nums[left], nums[right]);
        }
        swap(nums[end - 1], nums[right]);

        return right;
    }

    int
    findKthLargest (
        vector<int>& nums,
        int k
        )
    {
        int start = 0;
        int end = nums.size();

        while (true)
        {
            int pivotInd = partition(nums, start, end);

            int position = nums.size() - pivotInd;
            if (position == k)
            {
                return nums[pivotInd];
            }
            else if (position < k)
            {
                end = pivotInd;
            }
            else
            {
                start = pivotInd + 1;
            }
        }
    }
};
