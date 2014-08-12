class Solution:
    Values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    def romanToInt(self, s):
        prevDigit = 0
        currentValue = 0

        for digit in reversed(s):
            digitValue = self.Values[digit]
            if digitValue < prevDigit:
                currentValue -= digitValue
            else:
                currentValue += digitValue
            prevDigit = digitValue

        return currentValue