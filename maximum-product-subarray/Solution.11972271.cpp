class Solution {
public:

    int maxProduct(int A[], int n) {
        int bestProduct = numeric_limits<int>::min();
        int maxPositive = 1;
        int minNegative = 1;
        
        for (int i = 0; i < n; ++i)
        {
            if (A[i] > 0)
            {
                bestProduct = max(bestProduct, maxPositive * A[i]);
                maxPositive *= A[i];
                minNegative *= max(1, A[i]);
            }
            else if (A[i] == 0)
            {
                bestProduct = max(bestProduct, 0);
                maxPositive = 1;
                minNegative = 1;
            }
            else // A[i] < 0
            {
                bestProduct = max(bestProduct, minNegative * A[i]);
                int oldMaxPositive = maxPositive;
                maxPositive = max(1, minNegative * A[i]);
                minNegative = oldMaxPositive * A[i];
            }
        }
        
        return bestProduct;
    }
};
