class Solution(object):

    def isValidSerialization(self, preorder):
        preorder = preorder.split(",")
        length = self.valid_serialization_length(preorder, 0, len(preorder))
        if length == len(preorder):
            return True
        else:
            return False

    def valid_serialization_length(self, preorder, begin, end):
        if preorder[begin] == "#":
            return 1

        if end - begin < 3:
            return 0

        left_length = self.valid_serialization_length(preorder, begin + 1, end)
        if left_length == 0:
            return 0

        right_length = self.valid_serialization_length(preorder, begin + 1 + left_length, end)
        if right_length == 0:
            return 0

        return 1 + left_length + right_length
