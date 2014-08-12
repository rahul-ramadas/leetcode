class Solution:

    def isPalindrome(self, x):
        if x < 0:
            return False

        least_digit_mask = 1
        most_digit_mask = 1
        while x / most_digit_mask:
            most_digit_mask *= 10
        most_digit_mask /= 10

        while ((most_digit_mask > least_digit_mask) and
               (((x / most_digit_mask) % 10) == ((x / least_digit_mask) % 10))):
            most_digit_mask /= 10
            least_digit_mask *= 10

        if most_digit_mask > least_digit_mask:
            return False
        else:
            return True
