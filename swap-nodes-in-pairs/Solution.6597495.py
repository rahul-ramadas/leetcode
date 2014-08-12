class Solution:
    def swapPairs(self, head):
        if head is None:
            return None

        prev = None
        one = head
        two = head.next
        if two is not None:
            head = two

        while one is not None and two is not None:
            last = two.next
            one.next = last
            two.next = one
            if prev is not None:
                prev.next = two
            prev = one
            one = last
            if last is not None:
                two = last.next

        return head
