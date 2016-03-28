class Solution:

    def countBits(self, num):
        if num == 0:
            return [0]

        result = [0] * (num + 1)

        last_power_of_two = 1
        copy_from = 0
        for i in xrange(1, num + 1):
            result[i] = 1 + result[copy_from]
            copy_from += 1
            if copy_from == last_power_of_two:
                last_power_of_two = i + 1
                copy_from = 0

        return result
