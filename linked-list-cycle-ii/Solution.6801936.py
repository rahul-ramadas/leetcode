class Solution:
    def detectCycle(self, head):
        if head is None:
            return None

        tortoise = head
        hare = head

        while True:
            if hare.next is None or hare.next.next is None:
                return None

            hare = hare.next.next
            tortoise = tortoise.next

            if tortoise is hare:
                break

        tortoise = head

        while tortoise is not hare:
            tortoise = tortoise.next
            hare = hare.next

        return tortoise
