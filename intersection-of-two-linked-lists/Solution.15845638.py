# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param two ListNodes
    # @return the intersected ListNode
    def getIntersectionNode(self, headA, headB):
        lengthA = self.getLength(headA)
        lengthB = self.getLength(headB)
        
        while lengthA > lengthB:
            headA = headA.next
            lengthA -= 1
            
        while lengthB > lengthA:
            headB = headB.next
            lengthB -= 1
            
        while headA is not None and headB is not None:
            if headA is headB:
                return headA
            headA = headA.next
            headB = headB.next
            
        return None
        
    def getLength(self, head):
        length = 0
        while head is not None:
            length += 1
            head = head.next
            
        return length
