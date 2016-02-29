class Solution:

    def singleNumber(self, nums):
        xor_all = reduce(operator.xor, nums)

        # Get a bit-mask with just the right-most bit set. We do with by first computing a number
        # with the right-most bit cleared, then XOR it with the original number.
        rightmost_bit = (xor_all & (xor_all - 1)) ^ (xor_all)

        xor_all_with_bit_set = reduce(operator.xor, (n for n in nums if n & rightmost_bit))
        xor_all_with_bit_clear = reduce(operator.xor, (n for n in nums if not n & rightmost_bit))

        return [xor_all_with_bit_set, xor_all_with_bit_clear]
