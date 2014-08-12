class Solution
{
public:

    bool isAnagram(const string& s1, size_t s1begin, size_t s1end, const string& s2, size_t s2begin, size_t s2end)
    {
        array<int, 26> s1map{};
        array<int, 26> s2map{};

        for (size_t i = s1begin; i != s1end; ++i)
        {
            ++s1map[s1[i] - 'a'];
        }

        for (size_t i = s2begin; i != s2end; ++i)
        {
            ++s2map[s2[i] - 'a'];
        }

        return equal(s1map.cbegin(), s1map.cend(), s2map.cbegin());
    }

    bool isScramble(const string& s1, size_t s1begin, size_t s1end, const string& s2, size_t s2begin, size_t s2end)
    {
        if ((s1end - s1begin) != (s2end - s2begin))
        {
            return false;
        }

        if (!(s1end - s1begin))
        {
            return true;
        }

        if (!isAnagram(s1, s1begin, s1end, s2, s2begin, s2end))
        {
            return false;
        }

        if (equal(s1.cbegin() + s1begin, s1.cbegin() + s1end, s2.cbegin() + s2begin))
        {
            return true;
        }

        size_t len = s1end - s1begin;

        for (size_t offset = 1; offset < len; ++offset)
        {
            size_t s11begin = s1begin;
            size_t s11end = s11begin + offset;
            size_t s12begin = s11end;
            size_t s12end = s1end;

            size_t s21begin = s2begin;
            size_t s21end = s21begin + offset;
            size_t s22begin = s21end;
            size_t s22end = s2end;
            size_t s23begin = s2begin;
            size_t s23end = s23begin + (len - offset);
            size_t s24begin = s23end;
            size_t s24end = s2end;

            if ((isScramble(s1, s11begin, s11end, s2, s21begin, s21end) &&
                 isScramble(s1, s12begin, s12end, s2, s22begin, s22end)) ||
                (isScramble(s1, s11begin, s11end, s2, s24begin, s24end) &&
                 isScramble(s1, s12begin, s12end, s2, s23begin, s23end)))
            {
                return true;
            }
        }

        return false;
    }

    bool isScramble(string s1, string s2)
    {
        return isScramble(s1, 0, s1.length(), s2, 0, s2.length());
    }
};
