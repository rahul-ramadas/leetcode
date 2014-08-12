class Solution:
    def generate(self, numRows):
        if not numRows:
            return []

        triangle = [[1]]
        for i in range(1, numRows):
            newList = []
            for j in range(-1, i):
                a = 0 if j < 0 else triangle[i - 1][j]
                b = 0 if j == i - 1 else triangle[i - 1][j + 1]
                newList.append(a + b)
            triangle.append(newList)

        return triangle