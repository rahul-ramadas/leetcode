class Solution:

    def has_leading_zeros(self, num):
        if len(num) > 1 and num[0] == "0":
            return True
        return False

    def check_is_additive(self, num, start_index, prev_num, expected_next_num):

        if start_index == len(num):
            return True

        expected_next_num_str = str(expected_next_num)
        if not num.startswith(expected_next_num_str, start_index):
            return False

        start_index += len(expected_next_num_str)

        return self.check_is_additive(num, start_index, expected_next_num, prev_num + expected_next_num)

    def isAdditiveNumber(self, num):
        for first_len in xrange(1, len(num) + 1):
            first_num_str = num[:first_len]
            if self.has_leading_zeros(first_num_str):
                continue
            first_num = int(first_num_str)

            remaining_len = len(num) - first_len
            for second_len in xrange(1, remaining_len + 1):
                second_num_str = num[first_len:first_len + second_len]
                if self.has_leading_zeros(second_num_str):
                    continue
                second_num = int(second_num_str)

                if first_len + second_len == len(num):
                    continue

                if self.check_is_additive(num, first_len + second_len, second_num, first_num + second_num):
                    return True

        return False
