class Solution:

    def zigzagLevelOrder(self, root):

        if root is None:
            return []

        current_level = [root]
        next_level = []
        levels = []

        while current_level:

            levels.append(current_level)

            for node in current_level:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)

            current_level = next_level[:]
            del next_level[:]

        for i in xrange(1, len(levels), 2):
            levels[i] = list(reversed(levels[i]))

        return [list(map(operator.attrgetter('val'), l)) for l in levels]
