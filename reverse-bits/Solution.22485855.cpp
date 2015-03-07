class Solution
{
public:

    Solution()
    {
        for (uint32_t i = 0; i <= 255; ++i)
        {
            m_ReverseMap[i] = reverseBits8(static_cast<uint8_t>(i));
        }
    }

    uint32_t reverseBits(uint32_t n)
    {
        uint32_t reversed = 0;

        for (int i = 0; i < 4; ++i)
        {
            uint8_t byte = static_cast<uint8_t>(0xFF & n);
            n >>= 8;
            reversed <<= 8;
            reversed |= m_ReverseMap[byte];
        }

        return reversed;
    }

private:

    static uint8_t reverseBits8(uint8_t n)
    {
        uint8_t reversed = 0;
        for (int i = 0; i < 8; ++i)
        {
            reversed <<= 1;
            reversed |= (n & 0x1);
            n >>= 1;
        }

        return reversed;
    }

    array<uint8_t, 256> m_ReverseMap;
};
