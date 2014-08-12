class Solution {
public:
    int lengthOfLastWord(const char *s) {
        size_t len = strlen(s);
        int endIndex = len - 1;
        for (; endIndex >= 0 && s[endIndex] == ' '; --endIndex);
        int res = 0;
        for (; endIndex >= 0 && s[endIndex] != ' '; --endIndex, ++res);
        return res;
    }
};
