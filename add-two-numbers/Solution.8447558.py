# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
        carry = 0
        
        head = ListNode(0)
        l3 = head
        
        while l1 is not None or l2 is not None:
            a = 0
            b = 0
            if l1 is not None:
                a = l1.val
                l1 = l1.next
            if l2 is not None:
                b = l2.val
                l2 = l2.next
            
            l3.next = ListNode(0)
            l3 = l3.next
                
            c = a + b + carry
            l3.val = c % 10
            carry = c / 10
            
        if carry:
            l3.next = ListNode(carry)
            
        return head.next
