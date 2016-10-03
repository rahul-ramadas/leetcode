class Solution {
public:
    int longestPalindrome(string s) {
        map<char, unsigned> letterCount;
        
        for (char c: s)
        {
            ++letterCount[c];
        }
        
        bool foundOdd = false;
        unsigned maxLength = 0;
        for (const auto& elem: letterCount)
        {
            if (elem.second % 2)
            {
                foundOdd = true;
                maxLength += elem.second - 1;
            }
            else
            {
                maxLength += elem.second;
            }
        }
        
        if (foundOdd)
        {
            maxLength += 1;
        }
        
        return static_cast<int>(maxLength);
    }
};
