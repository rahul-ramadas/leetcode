class Solution:

    def removeNthFromEnd(self, head, n):
        hare = head
        for _ in xrange(n - 1):
            hare = hare.next

        if hare.next is None:
            head = head.next
            return head

        hare = hare.next
        tortoise = head
        while hare.next is not None:
            hare = hare.next
            tortoise = tortoise.next

        tortoise.next = tortoise.next.next
        return head
