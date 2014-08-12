class Solution
{
public:

    TreeNode* sortedListToBST(ListNode*& head, size_t begin, size_t end)
    {
        if (begin >= end)
        {
            return NULL;
        }

        size_t mid = begin + (end - begin) / 2;
        TreeNode* left = sortedListToBST(head, begin, mid);
        TreeNode* root = new TreeNode(head->val);
        root->left = left;
        head = head->next;
        root->right = sortedListToBST(head, mid + 1, end);
        return root;
    }

    TreeNode* sortedListToBST(ListNode* head)
    {
        size_t n = 0;
        ListNode* node = head;
        while (node != NULL)
        {
            ++n;
            node = node->next;
        }

        return sortedListToBST(head, 0, n);
    }
};
