class Solution {
public:
    int trap(int A[], int n) {
        vector<int> tallestToLeft(n, 0);
        vector<int> tallestToRight(n, 0);
        
        for (int i = 1; i < n; ++i)
        {
            tallestToLeft[i] = max(tallestToLeft[i - 1], A[i - 1]);
        }
        
        for (int i = n - 2; i >= 0; --i)
        {
            tallestToRight[i] = max(tallestToRight[i + 1], A[i + 1]);
        }
        
        int totalVolume = 0;
        for (int i = 0; i < n; ++i)
        {
            totalVolume += max(0, min(tallestToLeft[i], tallestToRight[i]) - A[i]);
        }
        
        return totalVolume;
    }
};