class Solution:
    def hasCycle(self, head):
        if head is None:
            return False

        slow = head
        fast = head.next

        while slow is not None and fast is not None:
            slow = slow.next
            fast = fast.next
            if slow is not None and fast is not None and slow is fast:
                return True

            if fast is not None:
                fast = fast.next

            if slow is not None and fast is not None and slow is fast:
                return True

        return False
