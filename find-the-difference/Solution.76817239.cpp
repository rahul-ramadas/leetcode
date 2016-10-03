class Solution {
public:
    char findTheDifference(string s, string t) {
        map<char, unsigned> letterCount;
        
        for (char c : s)
        {
            letterCount[c] += 1;
        }
        
        for (char c : t)
        {
            letterCount[c] += 1;
        }
        
        for (const auto& elem : letterCount)
        {
            if (elem.second % 2)
            {
                return elem.first;
            }
        }
        
        return 0;
    }
};
