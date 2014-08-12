class Solution:
    def rotate(self, matrix):
        return [list(reversed(c)) for c in zip(*matrix)]
