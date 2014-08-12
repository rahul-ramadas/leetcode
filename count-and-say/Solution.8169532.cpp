class Solution
{
public:

    string countAndSay(int n)
    {
        string sequence = "1";

        for (int i = 2; i <= n; ++i)
        {
            int j = 0;

            stringstream sout;

            while (j < sequence.length())
            {
                int count = 1;
                char c = sequence[j++];
                while (j < sequence.length() && sequence[j] == c)
                {
                    ++j;
                    ++count;
                }

                sout << count << c;
            }

            sequence = sout.str();
        }

        return sequence;
    }
};
