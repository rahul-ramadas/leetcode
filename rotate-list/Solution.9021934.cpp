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
    ListNode *rotateRight(ListNode *head, int k) {
        
        if (k == 0 || head == NULL)
        {
            return head;
        }
        
        int length = 1;
        ListNode* node = head;
        while (node->next)
        {
            ++length;
            node = node->next;
        }
        
        k %= length;
        
        if (k == 0)
        {
            return head;
        }
        
        node->next = head;
        int count = length - k;
        node = head;
        while (--count)
        {
            node = node->next;
        }
        
        head = node->next;
        node->next = NULL;
        
        return head;
    }
};