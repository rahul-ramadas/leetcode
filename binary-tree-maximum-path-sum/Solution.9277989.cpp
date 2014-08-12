/**
 * Definition for binary tree
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:

    int findMaxPathToChild(TreeNode* root, int& maxPathSum)
    {
        if (!root)
        {
            return 0;
        }
        
        int leftMax = findMaxPathToChild(root->left, maxPathSum);
        int rightMax = findMaxPathToChild(root->right, maxPathSum);
        
        maxPathSum = max(maxPathSum, root->val);
        maxPathSum = max(maxPathSum, root->val + leftMax);
        maxPathSum = max(maxPathSum, root->val + rightMax);
        maxPathSum = max(maxPathSum, leftMax + rightMax + root->val);
        
        int childMax = root->val;
        childMax = max(childMax, root->val + leftMax);
        childMax = max(childMax, root->val + rightMax);
        
        return childMax;
    }

    int maxPathSum(TreeNode *root) {
        if (!root)
        {
            return 0;
        }
        
        int maxPath = root->val;
        findMaxPathToChild(root, maxPath);
        return maxPath;
    }
};