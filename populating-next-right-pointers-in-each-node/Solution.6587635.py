class Solution:
    def connect(self, root):
        if root is None:
            return

        root.parent = None
        processingLevel = 2
        currentLevel = 1
        currentNode = root
        prevNode = None

        while True:
            while currentLevel < processingLevel and currentNode.left is not None:
                currentNode.left.parent = currentNode
                currentNode = currentNode.left
                currentLevel += 1

            if currentLevel < processingLevel:
                break

            if prevNode is not None:
                prevNode.next = currentNode

            prevNode = currentNode
            currentNode = currentNode.parent
            currentNode.right.parent = currentNode
            currentNode = currentNode.right
            prevNode.next = currentNode
            prevNode = currentNode

            while currentNode.parent is not None and currentNode.parent.right is currentNode:
                currentNode = currentNode.parent
                currentLevel -= 1

            if currentNode.parent is None:
                processingLevel += 1
                prevNode = None
                continue

            currentNode = currentNode.parent
            currentNode.right.parent = currentNode
            currentNode = currentNode.right