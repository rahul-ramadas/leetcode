class Codec:

    def serialize(self, root):
        if root is None:
            return ""

        level = [root]
        serialization = [root]

        while level:
            next_level = []
            for node in level:
                if node is None:
                    continue

                next_level.append(node.left)
                next_level.append(node.right)

            serialization.extend(next_level)
            level = next_level

        while serialization[-1] is None:
            del serialization[-1]

        serialization = " ".join(str(i.val) if i is not None else "null" for i in serialization)
        return serialization

    def deserialize(self, data):
        if not data:
            return None

        data = [int(i) if i != "null" else None for i in data.split()]
        root = TreeNode(data[0])
        previous_level = [root]
        index = 1

        def construct_node(data_element):
            if data_element is None:
                return None
            return TreeNode(data_element)

        while previous_level:
            next_level = []
            for node in previous_level:
                if index < len(data):
                    node.left = construct_node(data[index])
                    index += 1
                    if node.left is not None:
                        next_level.append(node.left)
                if index < len(data):
                    node.right = construct_node(data[index])
                    index += 1
                    if node.right is not None:
                        next_level.append(node.right)
            previous_level = next_level

        return root
