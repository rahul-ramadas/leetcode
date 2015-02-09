class Solution:

    def largestNumber(self, num):
        num_str = map(str, num)
        num_str.sort(cmp=lambda str1, str2: -1 if str1 + str2 > str2 + str1 else 1)
        if len(num_str) >= 2 and num_str[0] == num_str[1] == "0":
            return "0"
        return "".join(num_str)
