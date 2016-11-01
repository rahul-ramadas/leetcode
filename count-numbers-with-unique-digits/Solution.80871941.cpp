class Solution {
public:
    int countNumbersWithUniqueDigits(int n) {
        if (n == 0)
        {
            return 1;
        }
        
        if (n == 1)
        {
            return 10;
        }
        
        int count = 10;
        for (int digits = 2; digits <= min(n, 10); ++digits)
        {
            int posibs = 9;
            int countWithDigits = 1;
            for (int i = 0; i < digits; ++i)
            {
                countWithDigits *= posibs;
                if (i != 0)
                {
                    --posibs;
                }
            }
            
            count += countWithDigits;
        }
        
        return count;
    }
};
