class Solution:

    def connect(self, root):
        if root is None:
            return

        level_head = root
        root.parent = None

        def get_next_node(node):
            parent = node.parent
            if parent is None:
                return None

            if parent.left is node:
                if parent.right is not None:
                    return parent.right

            while parent.next is not None:
                parent = parent.next
                if parent.left is not None:
                    return parent.left
                elif parent.right is not None:
                    return parent.right

            return None

        def get_next_level(this_level_head):
            while this_level_head is not None:
                if this_level_head.left is not None:
                    return this_level_head.left
                elif this_level_head.right is not None:
                    return this_level_head.right
                this_level_head = this_level_head.next

        while level_head is not None:
            node = level_head
            while node is not None:
                if node.left is not None:
                    node.left.parent = node
                if node.right is not None:
                    node.right.parent = node

                node.next = get_next_node(node)
                node = node.next

            level_head = get_next_level(level_head)
