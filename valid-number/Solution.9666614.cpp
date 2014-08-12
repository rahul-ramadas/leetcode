class Solution
{
private:

public:
    bool isNumber(const char* s)
    {
        char* end;
        while (*s == ' ')
        {
            ++s;
        }

        if (!*s)
        {
            return false;
        }

        double value = strtod(s, &end);

        while (*end == ' ')
        {
            ++end;
        }

        return !*end;
    }
};
