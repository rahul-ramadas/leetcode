# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return head
        
        odd_head = head
        even_head = head.next
        cur_odd = odd_head
        cur_even = even_head
        
        while cur_even is not None and cur_even.next is not None:
            next_odd = cur_even.next
            cur_even.next = cur_even.next.next
            cur_odd.next = next_odd
            cur_odd = cur_odd.next
            cur_even = cur_even.next
            
        cur_odd.next = even_head
        return odd_head
