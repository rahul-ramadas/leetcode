class Solution
{
public:

    void insertSortedList(ListNode*& head, ListNode* node)
    {
        ListNode* current = head;
        ListNode** prevPtr = &head;

        while (current && (current->val < node->val))
        {
            prevPtr = &(current->next);
            current = current->next;
        }

        *prevPtr = node;
        node->next = current;
    }

    ListNode *insertionSortList(ListNode *head)
    {
        ListNode* sortedHead = NULL;

        while (head)
        {
            ListNode* node = head;
            head = head->next;
            node->next = NULL;

            insertSortedList(sortedHead, node);
        }

        return sortedHead;
    }
};
