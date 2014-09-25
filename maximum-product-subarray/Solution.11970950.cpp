class Solution {
public:

    int getProduct(int A[], int i, int j)
    {
        if (i == j)
        {
            return numeric_limits<int>::min();
        }

        return accumulate(A + i, A + j, 1, multiplies<int>());
    }

    int maxProduct(int A[], int n) {
        int bestProduct = numeric_limits<int>::min();

        int segmentStart = 0;
        while (segmentStart < n)
        {
            int firstNegative = -1;
            int lastNegative = -1;
            int countNegatives = 0;

            int i;
            for (i = segmentStart; (i < n) && (A[i] != 0); ++i)
            {
                if (A[i] < 0)
                {
                    ++countNegatives;
                    if (firstNegative == -1)
                    {
                        firstNegative = i;
                    }

                    lastNegative = i;
                }
            }

            int product;

            if (countNegatives % 2 == 0)
            {
                product = getProduct(A, segmentStart, i);
            }
            else
            {
                if (i - segmentStart == 1)
                {
                    product = A[segmentStart];
                }
                else
                {
                    int firstProduct = getProduct(A, segmentStart, lastNegative);
                    int secondProduct = getProduct(A, firstNegative + 1, i);

                    product = max(firstProduct, secondProduct);
                }
            }

            bestProduct = max(bestProduct, product);

            if (i < n)
            {
                bestProduct = max(0, bestProduct);
                ++i;
            }

            segmentStart = i;
        }

        return bestProduct;
    }
};
