class Solution {
public:
    bool isValid(string s) {
        stack<char> bracketStack;
        
        for (auto c : s)
        {
            if (c == '(' || c == '[' || c == '{')
            {
                bracketStack.push(c);
                continue;
            }
            
            if (bracketStack.empty())
            {
                return false;
            }
            
            auto popped = bracketStack.top();
            bracketStack.pop();
            
            if (((c == ')') && (popped != '(')) ||
                ((c == ']') && (popped != '[')) ||
                ((c == '}') && (popped != '{')))
            {
                return false;
            }
        }
        
        return bracketStack.empty();
    }
};