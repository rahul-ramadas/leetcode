class Solution
{
public:
    ListNode *reverseBetween(ListNode *head, int m, int n)
    {
        ListNode** newHead = &head;
        ListNode** newTail;
        ListNode* cur = head;

        for (int i = 1; i < m; ++i)
        {
            newHead = &((*newHead)->next);
            cur = cur->next;
        }

        ListNode* prev = NULL;
        ListNode* next = cur->next;
        newTail = &(cur->next);

        for (int i = m; i <= n; ++i)
        {
            cur->next = prev;
            prev = cur;
            cur = next;
            if (next)
            {
                next = next->next;
            }
        }

        *newTail = cur;
        *newHead = prev;

        return head;
    }
};
