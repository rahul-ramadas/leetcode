class Solution {

private:

    bool matchAndAdvance(const char*& s, const char*& p, bool& tooLong)
    {
        const char* ts = s;
        const char* tp = p;
        tooLong = false;
        while (*tp)
        {
            if (*tp == '*')
            {
                s = ts;
                p = tp;
                return true;
            }

            if (!*ts)
            {
                tooLong = true;
                return false;
            }

            if ((*tp != '?') && (*ts != *tp))
            {
                return false;
            }

            ++ts;
            ++tp;
        }

        if (!*ts && !*tp)
        {
            s = ts;
            p = tp;
            return true;
        }

        return false;
    }

public:
    bool isMatch(const char *s, const char *p) {
        // s is string
        // p is pattern

        if (s == NULL)
        {
            s = "";
        }

        if (p == NULL)
        {
            p = "";
        }

        if (!*s && !*p)
        {
            return true;
        }

        if (!*p)
        {
            return false;
        }

        if (*p == '*')
        {
            do
            {
                ++p;
            } while (*p == '*');

            while (*s)
            {
                bool tooLong;
                if (matchAndAdvance(s, p, tooLong))
                {
                    return isMatch(s, p);
                }

                if (tooLong)
                {
                    return false;
                }

                ++s;
            }

            return !*p;
        }
        else
        {
            bool tooLong;
            if (!matchAndAdvance(s, p, tooLong))
            {
                return false;
            }
            return isMatch(s, p);
        }
    }
};
