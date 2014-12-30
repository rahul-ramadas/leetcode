class Solution:

    def getElement(self, num, index):
        if index < 0 or index >= len(num):
            return float('-inf')
        return num[index]

    def findPeakElement(self, num):

        lower_bound = 0
        upper_bound = len(num)

        while True:

            middle_index = (upper_bound + lower_bound) // 2

            middle = self.getElement(num, middle_index)
            left = self.getElement(num, middle_index - 1)
            right = self.getElement(num, middle_index + 1)

            if left < middle > right:
                return middle_index
            elif left < middle < right:
                lower_bound = middle_index + 1
            elif left > middle > right:
                upper_bound = middle_index
            elif left > middle < right:
                upper_bound = middle_index
