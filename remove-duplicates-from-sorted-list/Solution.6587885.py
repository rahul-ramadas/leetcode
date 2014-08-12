# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        if head is None:
            return None
            
        lastNode = head
        node = head.next
        
        while node is not None:
            if node.val != lastNode.val:
                lastNode.next = node
                lastNode = node
            node = node.next
        lastNode.next = None
        
        return head
