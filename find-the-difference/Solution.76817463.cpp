class Solution {
public:
    char findTheDifference(string s, string t) {
        char remaining = 0;
        
        for (char c : s)
        {
            remaining ^= c;
        }
        
        for (char c : t)
        {
            remaining ^= c;
        }
        
        return remaining;
    }
};
