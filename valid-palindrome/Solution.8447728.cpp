class Solution {
public:
    bool isPalindrome(string s) {

        auto forward = s.cbegin();
        auto backward = s.cend() - 1;
        
        while (forward < backward)
        {
            while (forward < backward && !isalnum(*forward))
            {
                ++forward;
            }
            
            if (forward >= backward)
            {
                break;
            }
            
            while (backward > forward && !isalnum(*backward))
            {
                --backward;
            }
            
            if (backward <= forward)
            {
                break;
            }
            
            if (tolower(*forward) != tolower(*backward))
            {
                return false;
            }
            
            ++forward;
            --backward;
        }

        return true;
    }
};