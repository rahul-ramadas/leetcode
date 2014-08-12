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

    ListNode* getFirstHalfEnd(ListNode* head)
    {
        ListNode* slow = head;
        ListNode* fast = head;
        
        while (true)
        {
            fast = fast->next;
            if (!fast)
            {
                break;
            }
            
            fast = fast->next;
            if (!fast)
            {
                break;
            }
            
            slow = slow->next;
        }
        
        return slow;
    }
    
    void reverseList(ListNode*& head)
    {
        ListNode* cur = head;
        ListNode* prev = NULL;
        
        while (cur)
        {
            ListNode* next = cur->next;
            cur->next = prev;
            prev = cur;
            cur = next;
        }
        
        head = prev;
    }
    
    void reorderList(ListNode *head) {
        
        if (!head)
        {
            return;
        }
        
        ListNode* firstHalfEnd = getFirstHalfEnd(head);
        reverseList(firstHalfEnd->next);
        
        ListNode* firstHalf = head;
        ListNode* secondHalf = firstHalfEnd->next;
        firstHalfEnd->next = NULL;
        ListNode** prev = &head;
        
        while (firstHalf)
        {
            *prev = firstHalf;
            firstHalf = firstHalf->next;
            (*prev)->next = secondHalf;
            if (secondHalf)
            {
                prev = &(secondHalf->next);
                secondHalf = secondHalf->next;
            }
        }
    }
};
