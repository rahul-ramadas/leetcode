class Solution {
public:
    array<vector<int>, 26> GetIndicesArray(const string& T)
    {
        array<vector<int>, 26> indicesArr{};
        for (int i = 0; i < (int)T.length(); ++i)
        {
            indicesArr[T[i] - 'a'].push_back(i);
        }
        
        return indicesArr;
    }
    
    int FindNextInd(const vector<int>& Indices, int LastInd)
    {
        auto it = std::upper_bound(Indices.cbegin(), Indices.end(), LastInd);
        if (it == Indices.cend())
        {
            return -1;
        }
        
        return *it;
    }
    
    bool isSubsequence(string s, string t) {
        auto indicesArr = GetIndicesArray(t);
        int lastInd = -1;
        
        for (char c : s)
        {
            auto& indices = indicesArr[c - 'a'];
            lastInd = FindNextInd(indices, lastInd);
            if (lastInd == -1)
            {
                return false;
            }
        }
        
        return true;
    }
};
