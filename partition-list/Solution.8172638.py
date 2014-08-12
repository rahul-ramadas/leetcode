class Solution:

    def partition(self, head, x):
        left_head = ListNode(0)
        left = left_head
        right_head = ListNode(0)
        right = right_head

        node = head
        while node is not None:
            if node.val < x:
                left.next = node
                left = left.next
            else:
                right.next = node
                right = right.next

            temp = node
            node = node.next
            temp.next = None

        left.next = right_head.next
        return left_head.next
