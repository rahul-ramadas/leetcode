class Solution {
public:
    bool isMatch(const char *s, const char *p) {
        // s is string
        // p is regex

        size_t slen = strlen(s);
        size_t plen = strlen(p);
        vector<bool> canMatch(slen + 1, false);
        
        canMatch[slen] = true;
        
        for (size_t i = plen; i-- > 0;)
        {
            if (p[i] == '*')
            {
                continue;
            }
            
            bool isRepeated;
            if (((i + 1) != plen) && (p[i + 1] == '*'))
            {
                isRepeated = true;
            }
            else
            {
                isRepeated = false;
            }
            
            for (size_t j = 0; j <= slen; ++j)
            {
                if (j == slen)
                {
                    canMatch[j] = isRepeated && canMatch[j];
                    continue;
                }

                if (!isRepeated)
                {
                    if (p[i] == '.')
                    {
                        canMatch[j] = canMatch[j + 1];
                    }
                    else
                    {
                        canMatch[j] = (p[i] == s[j]) && canMatch[j + 1];
                    }
                }
                else
                {
                    for (size_t k = j; k <= slen && !canMatch[j]; ++k)
                    {
                        if ((k > j) && (p[i] != '.'))
                        {
                            if (p[i] != s[k - 1])
                            {
                                break;
                            }
                        }
                        
                        canMatch[j] = canMatch[k];
                    }
                }
            }
        }
        
        return canMatch[0];
    }
};