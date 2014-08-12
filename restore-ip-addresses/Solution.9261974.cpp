class Solution {
public:

    void findIps(const string& s, size_t ind, int foundSegments, vector<size_t>& segLengths, vector<string>& results)
    {
        if (foundSegments == 4)
        {
            if (ind == s.length())
            {
                string ip;
                size_t curInd = 0;
                for (auto l : segLengths)
                {
                    if (ip.length())
                    {
                        ip += ".";
                    }
                    ip += s.substr(curInd, l);
                    curInd += l;
                }
                results.push_back(ip);
            }

            return;
        }
        
        for (size_t j = 1; (j <= 3) && ((ind + j) <= s.length()); ++j)
        {
            string seg = s.substr(ind, j);
            if (stoi(seg) > 255)
            {
                break;
            }
            
            segLengths[foundSegments] = j;
            findIps(s, ind + j, foundSegments + 1, segLengths, results);
            
            if (seg == "0")
            {
                break;
            }
        }
    }

    vector<string> restoreIpAddresses(string s) {
        vector<string> results;
        vector<size_t> segLengths(4, 0);
        findIps(s, 0, 0, segLengths, results);
        return results;
    }
};