class Solution
{
public:

    string addBinary(string a, string b)
    {
        int carry = 0;

        auto aiter = a.crbegin();
        auto aend = a.crend();
        auto biter = b.crbegin();
        auto bend = b.crend();

        string result;

        while ((aiter != aend) || (biter != bend) || carry)
        {
            int a = 0;
            int b = 0;
            if (aiter != aend)
            {
                a = *aiter - '0';
                ++aiter;
            }

            if (biter != bend)
            {
                b = *biter - '0';
                ++biter;
            }

            int val = carry + a + b;
            carry = val / 2;
            val %= 2;

            result = string(1, '0' + val) + result;
        }

        return result;
    }
};
