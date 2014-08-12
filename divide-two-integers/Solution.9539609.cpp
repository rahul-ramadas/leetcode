class Solution {
public:
    int divide(int Dividend, int Divisor) {
        long long dividend = llabs(Dividend);
        long long divisor = llabs(Divisor);
        long long multiple = divisor;
        long long factor = 1;

        while (multiple <= INT_MAX + 1ll)
        {
            multiple <<= 1;
            factor <<= 1;
        }

        multiple >>= 1;
        factor >>= 1;

        long long quotient = 0;
        while (factor)
        {
            while (dividend - multiple >= 0)
            {
                quotient += factor;
                dividend -= multiple;
            }

            multiple >>= 1;
            factor >>= 1;
        }

        if (((Dividend > 0) && (Divisor > 0)) || ((Dividend < 0) && (Divisor < 0)))
        {
            return (int)quotient;
        }
        else
        {
            return 0 - (int)quotient;
        }
    }
};
