class Solution:
    def reverse(self, x):
        isNegative = False
        if x < 0:
            isNegative = True
            x *= -1

        reversedNumber = int(str(x)[-1::-1])
        if isNegative:
            reversedNumber *= -1

        return reversedNumber
