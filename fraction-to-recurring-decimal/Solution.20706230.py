import math
import itertools


class Solution:

    def fractionToDecimal(self, numerator, denominator):
        sign = math.copysign(1, numerator / denominator)
        sign_str = "-" if sign == -1 else ""
        numerator = abs(numerator)
        denominator = abs(denominator)

        characteristic = numerator // denominator
        rem = numerator % denominator

        if rem == 0:
            return sign_str + str(characteristic)

        digits = []
        rems = dict()
        rems[rem] = 0

        repeat_index = None
        while rem != 0 and repeat_index is None:
            rem *= 10
            quot = rem // denominator
            digits.append(quot)
            rem = rem % denominator
            repeat_index = rems.get(rem)
            if repeat_index is None:
                rems[rem] = len(digits)

        if rem == 0:
            decimal_digits = "".join(itertools.imap(str, digits))
        else:
            chain = itertools.chain(itertools.islice(digits, repeat_index),
                                    "(",
                                    itertools.islice(digits, repeat_index, None),
                                    ")")
            decimal_digits = "".join(itertools.imap(str, chain))

        return sign_str + str(characteristic) + "." + decimal_digits
