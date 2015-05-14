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
    ListNode* removeElements(ListNode* head, int val) {
        ListNode** next = &head;
        ListNode* cur = head;
        
        while (cur)
        {
            if (cur->val == val)
            {
                *next = cur->next;
                cur = cur->next;
            }
            else
            {
                next = &cur->next;
                cur = cur->next;
            }
        }
        
        return head;
    }
};
