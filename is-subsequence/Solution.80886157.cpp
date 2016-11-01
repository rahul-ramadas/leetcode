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
        int lo = 0;
        int hi = (int)Indices.size();
        
        while (hi > lo)
        {
            int mid = lo + ((hi - lo) / 2);
            int num = Indices[mid];
            
            if (num <= LastInd)
            {
                lo = mid + 1;
            }
            else
            {
                hi = mid;
            }
        }
        
        if (lo == (int)Indices.size())
        {
            return -1;
        }
        
        return Indices[lo];
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
