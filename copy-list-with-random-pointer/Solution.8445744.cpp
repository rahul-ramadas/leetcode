class Solution
{
public:

    RandomListNode *copyRandomList(RandomListNode *head)
    {
        if (!head)
        {
            return NULL;
        }

        RandomListNode* ptr = head;

        while (ptr)
        {
            RandomListNode* next = ptr->next;
            ptr->next = new RandomListNode(ptr->label);
            ptr->next->next = next;
            ptr = next;
        }

        ptr = head;
        while (ptr)
        {
            if (ptr->random)
            {
                ptr->next->random = ptr->random->next;
            }
            ptr = ptr->next->next;
        }

        ptr = head;
        RandomListNode* newHead = ptr->next;
        while (ptr)
        {
            RandomListNode* next = ptr->next->next;
            if (next)
            {
                ptr->next->next = next->next;
            }
            ptr->next = next;
            ptr = next;
        }

        return newHead;
    }
};
