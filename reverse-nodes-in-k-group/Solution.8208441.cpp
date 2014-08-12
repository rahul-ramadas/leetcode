/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
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
    
    int listLength(ListNode* head)
    {
        int length = 0;
        
        while (head)
        {
            ++length;
            head = head->next;
        }
        
        return length;
    }
    
    ListNode *reverseKGroup(ListNode *head, int k) {
        int length = listLength(head);

        for (int start = 1, end = k; end <= length; start += k, end += k)
        {
            head = reverseBetween(head, start, end);
        }
        
        return head;
    }
};