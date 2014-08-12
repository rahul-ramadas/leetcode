class Solution
{
public:

    ListNode *mergeKLists(vector<ListNode *> &lists)
    {
        ListNode* head = NULL;
        ListNode** ptr = &head;
        auto comp = [](ListNode* lhs, ListNode* rhs)
        {
            return lhs->val > rhs->val;
        };

        priority_queue<ListNode*, vector<ListNode*>, decltype(comp)> pq(comp);

        for (auto node : lists)
        {
            if (node)
            {
                pq.push(node);
            }
        }

        while (!pq.empty())
        {
            ListNode* node = pq.top();
            pq.pop();

            *ptr = node;
            if (node->next)
            {
                pq.push(node->next);
            }
            (*ptr)->next = NULL;
            ptr = &((*ptr)->next);
        }

        return head;
    }
};
