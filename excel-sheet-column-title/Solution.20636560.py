class Solution:

    def convertToTitle(self, num):
        letters = []

        while num:
            num -= 1
            letters.append(string.ascii_uppercase[num % 26])
            num //= 26

        return ''.join(reversed(letters))
