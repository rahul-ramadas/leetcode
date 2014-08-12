class Solution:
    def mergeTwoLists(self, l1, l2):
        if l1 is None:
            return l2
        elif l2 is None:
            return l1

        head = ListNode(0)
        current = head

        while l1 is not None and l2 is not None:
            if l1.val < l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next

        if l1 is None:
            current.next = l2
        else:
            current.next = l1

        return head.next
