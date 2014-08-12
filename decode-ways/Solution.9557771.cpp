class Solution {
public:
    int numDecodings(string s) {
        if (s.empty())
        {
            return 0;
        }
        
        int a = (s.back() == '0') ? 0 : 1;
        
        if (s.length() == 1)
        {
            return a;
        }
        
        int b = 1;
        
        for (int i = s.length() - 2; i >= 0; --i)
        {
            int c = 0;
            if (s[i] != '0')
            {
                c += a;
            }
            
            int num = stoi(s.substr(i, 2));
            if (num >= 10 && num <= 26)
            {
                c += b;
            }
            
            b = a;
            a = c;
        }
        
        return a;
    }
};
