class Solution {
public:
    int divide(int Dividend, int Divisor) {
        long long dividend = llabs(Dividend);
        long long divisor = llabs(Divisor);
        vector<pair<long long, long long>> multiples;
        multiples.push_back(make_pair(1, divisor));
        while (true)
        {
            auto& lastMultiple = multiples.back();
            long long nextMultiple = lastMultiple.second + lastMultiple.second;
            if (nextMultiple > INT_MAX)
            {
                break;
            }
            
            multiples.push_back(make_pair(lastMultiple.first + lastMultiple.first, nextMultiple));
        }
        
        long long quotient = 0;
        for (auto it = multiples.crbegin(); it != multiples.crend(); ++it)
        {
            auto& multiple = *it;
            
            while (dividend - multiple.second >= 0)
            {
                quotient += multiple.first;
                dividend -= multiple.second;
            }
        }
        
        if (((Dividend > 0) && (Divisor > 0)) || ((Dividend < 0) && (Divisor < 0)))
        {
            return quotient;
        }
        else
        {
            return quotient - quotient - quotient;
        }
    }
};
