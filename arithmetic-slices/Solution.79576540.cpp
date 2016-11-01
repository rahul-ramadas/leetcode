class Solution
{
public:

    int numberOfArithmeticSlices(vector<int>& A)
    {
        if (A.size() < 2)
        {
            return 0;
        }

        long long currDiff = numeric_limits<long long>::max();
        int startIndex = 0;
        int count = 0;

        for (int i = 1; i <= (int) A.size(); ++i)
        {
            long long diff;
            if (i == (int) A.size())
            {
                diff = numeric_limits<long long>::max();
            }
            else
            {
                diff = A[i] - A[i - 1];
            }

            if (diff == currDiff)
            {
                continue;
            }

            int n = i - startIndex;

            if (n >= 3)
            {
                count += (n * n - 3 * n + 2) / 2;
            }

            startIndex = i - 1;
            currDiff = diff;
        }

        return count;
    }
};
