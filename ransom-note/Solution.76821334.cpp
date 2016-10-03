class Solution {
public:
    bool canConstruct(string ransomNote, string magazine) {
        if (magazine.length() < ransomNote.length())
        {
            return false;
        }
        
        array<unsigned, 26> letterCount{};
        
        for (char c: magazine)
        {
            ++letterCount[c - 'a'];
        }
        
        for (char c: ransomNote)
        {
            if (letterCount[c - 'a'] == 0)
            {
                return false;
            }
            
            --letterCount[c - 'a'];
        }
        
        return true;
    }
};
