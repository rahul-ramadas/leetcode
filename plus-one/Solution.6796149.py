class Solution:
    def plusOne(self, digits):
        carry = 1
        for i, e in reversed(list(enumerate(digits))):
            if not carry:
                break
            newE = (e + 1)
            digits[i] = newE % 10
            carry = newE / 10

        if carry:
            digits.insert(0, carry)

        return digits