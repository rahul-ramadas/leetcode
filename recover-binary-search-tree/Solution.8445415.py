class Solution:

    def recoverTree(self, root):
        firstWrong = None
        secondWrong = None

        node = root

        # Find smallest number

        while node.left is not None:

            rightMost = node.left
            while rightMost.right is not None:
                rightMost = rightMost.right
            rightMost.right = node

            node = node.left

        prev = node

        while node:

            if node.left is not None:
                rightMost = node.left
                while rightMost.right is not None and rightMost.right is not node:
                    rightMost = rightMost.right

                if rightMost.right is None:
                    rightMost.right = node
                    node = node.left
                else:
                    rightMost.right = None
                    if node.val < prev.val:
                        if firstWrong is None:
                            firstWrong = prev
                            secondWrong = node
                        else:
                            secondWrong = node
                    else:
                        prev = node
                    node = node.right
            else:
                if node.val < prev.val:
                    if firstWrong is None:
                        firstWrong = prev
                        secondWrong = node
                    else:
                        secondWrong = node
                else:
                    prev = node
                node = node.right

        firstWrong.val, secondWrong.val = secondWrong.val, firstWrong.val

        return root
