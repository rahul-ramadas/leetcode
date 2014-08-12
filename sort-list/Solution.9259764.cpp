class Solution {
public:

    ListNode* mergeSubLists(ListNode* head1, ListNode* head2, size_t halfLength, ListNode**& last)
    {
        size_t head1Len = 0;
        size_t head2Len = 0;
        ListNode* head = NULL;
        ListNode** prev = &head;
        
        while ((head1Len < halfLength) && (head2Len < halfLength) && (head2))
        {
            if (head1->val < head2->val)
            {
                *prev = head1;
                prev = &(head1->next);
                head1 = head1->next;
                ++head1Len;
            }
            else
            {
                *prev = head2;
                prev = &(head2->next);
                head2 = head2->next;
                ++head2Len;
            }
        }
        
        while (head1Len < halfLength)
        {
            *prev = head1;
            prev = &(head1->next);
            head1 = head1->next;
            ++head1Len;
        }
        
        while ((head2Len < halfLength) && (head2))
        {
            *prev = head2;
            prev = &(head2->next);
            head2 = head2->next;
            ++head2Len;
        }
        
        *prev = head2;
        last = prev;
        return head;
    }
    
    
    ListNode *sortList(ListNode *head) {
        
        for (size_t sortLen = 2; ; sortLen *= 2)
        {
            ListNode** prev = &head;
            
            bool merged = false;
            while (true)
            {
                size_t halfLength = sortLen / 2;
                ListNode* cur = *prev;
                
                for (size_t i = 0; cur && (i < halfLength); ++i, cur = cur->next);
                if (!cur)
                {
                    break;
                }
                
                merged = true;
                
                ListNode** last;
                *prev = mergeSubLists(*prev, cur, halfLength, last);
                prev = last;
            }
            
            if (!merged)
            {
                break;
            }
        }
        
        return head;
    }
};
