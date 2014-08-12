class Solution {
public:
    char *strStr(char *haystack, char *needle) {
        
        if (!haystack || !needle)
        {
            return NULL;
        }
        
        if (!*needle)
        {
            return haystack;
        }
        
        char* end = haystack;
        char* ptr;
        for (ptr = needle; *ptr && *end; ++ptr, ++end);
        if (*ptr)
        {
            return NULL;
        }
        
        --end;

        for (char* start = haystack; *end; ++start, ++end)
        {
            char* ptrn = needle;
            for (char* ptrh = start; *ptrn && (*ptrh == *ptrn); ++ptrh, ++ptrn);
            if (!*ptrn)
            {
                return start;
            }
        }
        
        return NULL;
    }
};