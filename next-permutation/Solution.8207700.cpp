class Solution
{
public:

    void nextPermutation(vector<int>& num)
    {
        if (num.size() <= 1)
        {
            return;
        }

        size_t index = num.size() - 1;

        while ((index > 0) && (num[index - 1] >= num[index]))
        {
            --index;
        }

        if (index == 0)
        {
            sort(num.begin(), num.end());
            return;
        }

        --index;

        size_t index2 = num.size() - 1;
        while (num[index2] <= num[index])
        {
            --index2;
        }

        swap(num[index], num[index2]);
        sort(num.begin() + index + 1, num.end());
    }
};
