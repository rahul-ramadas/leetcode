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
    ListNode* reverseLinkedList(ListNode* head)
    {
        ListNode* node = head;
        ListNode* prev = nullptr;
        
        while (node)
        {
            ListNode* next = node->next;
            node->next = prev;
            prev = node;
            node = next;
        }
        
        return prev;
    }
    
    bool isPalindrome(ListNode* head) {
        
        ListNode* slow = head;
        ListNode* fast = head;
        
        while (fast)
        {
            slow = slow->next;
            fast = fast->next;
            if (!fast)
            {
                break;
            }
            fast = fast->next;
        }
        
        ListNode* backHead = reverseLinkedList(slow);
        
        ListNode* front = head;
        ListNode* back = backHead;
        
        while (back && front->val == back->val)
        {
            front = front->next;
            back = back->next;
        }
        
        bool result;
        if (back)
        {
            result = false;
        }
        else
        {
            result = true;
        }
        
        reverseLinkedList(backHead);
        
        return result;
    }
};
