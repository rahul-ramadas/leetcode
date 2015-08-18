class Solution:

    def countDigitOne(self, n):
        place = 1
        count = 0
        while n - place >= 0:
            temp = n - place
            count += (temp // (place * 10)) * place
            temp %= (place * 10)
            count += min(place, temp + 1)
            place *= 10

        return count
