class Solution:

    def isValidSerialization(self, preorder):
        preorder = preorder.split(",")
        return self.is_valid_serialization(preorder)

    def is_valid_serialization(self, preorder):
        edge_count = 1
        for node in preorder:
            if edge_count == 0:
                return False
            edge_count -= 1
            if node != "#":
                edge_count += 2

        if edge_count != 0:
            return False
        return True
