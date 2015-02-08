class Solution:

    def titleToNumber(self, s):
        number = 0

        for c in s:
            number = number * 26 + (ord(c) - ord("A") + 1)

        return number
