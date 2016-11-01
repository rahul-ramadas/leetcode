class Solution {
public:
    int firstUniqChar(string s) {
        array<uint8_t, 26> letters{};
        for (char c : s)
        {
            letters[c - 'a'] = min(letters[c - 'a'] + 1, 2);
        }
        
        for (int i = 0; i < (int)s.length(); ++i)
        {
            if (letters[s[i] - 'a'] == 1)
            {
                return i;
            }
        }
        
        return -1;
    }
};
