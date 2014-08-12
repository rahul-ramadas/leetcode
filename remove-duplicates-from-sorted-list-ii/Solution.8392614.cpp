class Solution
{
public:
    ListNode *deleteDuplicates(ListNode *head)
    {
        if (!head)
        {
            return NULL;
        }

        ListNode** ptr = &head;
        int number;

        while (*ptr)
        {
            number = (*ptr)->val;

            if ((*ptr)->next == NULL)
            {
                break;
            }

            if ((*ptr)->next->val == number)
            {
                while (*ptr && ((*ptr)->val == number))
                {
                    *ptr = (*ptr)->next;
                }
            }
            else
            {
                ptr = &((*ptr)->next);
            }
        }

        return head;
    }
};
