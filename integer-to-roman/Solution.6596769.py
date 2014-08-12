class Solution:
    Numerals = [(1000, 'M'),
                (900, 'CM'),
                (500, 'D'),
                (400, 'CD'),
                (100, 'C'),
                (90, 'XC'),
                (50, 'L'),
                (40, 'XL'),
                (10, 'X'),
                (9, 'IX'),
                (5, 'V'),
                (4, 'IV'),
                (1, 'I')]

    def intToRoman(self, num):
        number = num
        numeral = ''
        while number:
            for v in self.Numerals:
                if v[0] <= number:
                    break

            number -= v[0]
            numeral += v[1]
        return numeral