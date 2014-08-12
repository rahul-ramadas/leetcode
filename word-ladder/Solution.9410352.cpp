class Solution {
public:

    int ladderLength(string start, string end, unordered_set<string> &dict) {

        dict.insert(end);
        unordered_map<string, string> previous;
        previous[start] = string();
        queue<string> process;
        process.push(start);
        auto firstword = dict.find(start);
        if (firstword != dict.end())
        {
            dict.erase(firstword);
        }
        
        while (!process.empty())
        {
            auto word = process.front();
            process.pop();
            
            if (word == end)
            {
                int count = 0;
                while (!word.empty())
                {
                    ++count;
                    word = previous[word];
                }
                
                return count;
            }
            
            string nextword = word;
            for (size_t i = 0; i < nextword.length(); ++i)
            {
                for (int j = 1; j <= 26; ++j)
                {
                    nextword[i] = ((nextword[i] - 'a' + 1) % 26) + 'a';
                    if (j == 26)
                    {
                        break;
                    }
                    
                    auto it = dict.find(nextword);
                    if (it == dict.end())
                    {
                        continue;
                    }
                    
                    previous[*it] = word;
                    process.push(*it);
                    dict.erase(it);
                }
            }
        }
        
        return 0;
    }
};
