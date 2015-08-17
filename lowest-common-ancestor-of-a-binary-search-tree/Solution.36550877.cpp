/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    TreeNode* findLca(TreeNode* node, TreeNode* p, TreeNode* q, bool& FoundP, bool& FoundQ)
    {
        if (node == nullptr)
        {
            return nullptr;
        }
        
        bool foundP = false;
        bool foundQ = false;
        
        TreeNode* lca;
        lca = findLca(node->left, p, q, foundP, foundQ);
        if (lca)
        {
            return lca;
        }
        
        FoundP |= foundP;
        FoundQ |= foundQ;
        
        foundP = false;
        foundQ = false;
        
        lca = findLca(node->right, p, q, foundP, foundQ);
        if (lca)
        {
            return lca;
        }
        
        FoundP |= foundP;
        FoundQ |= foundQ;
        
        if (node == p)
        {
            FoundP = true;
        }
        else if (node == q)
        {
            FoundQ = true;
        }
        
        if (FoundP && FoundQ)
        {
            return node;
        }
        
        return nullptr;
    }
    
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        bool foundP = false;
        bool foundQ = false;
        
        return findLca(root, p, q, foundP, foundQ);
    }
};
