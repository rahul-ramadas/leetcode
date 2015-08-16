class Solution:

    def find_min(self, num, low, high):
        while low < high:
            if num[low] < num[high]:
                return num[low]

            middle = (high + low) // 2
            if num[middle] > num[low]:
                low = middle + 1
            elif num[middle] < num[low]:
                high = middle
            else:
                return min(self.find_min(num, low, middle), self.find_min(num, middle + 1, high))

        return num[low]

    def findMin(self, num):
        if not num:
            return 0
        return self.find_min(num, 0, len(num) - 1)
