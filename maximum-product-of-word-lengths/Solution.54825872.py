class Solution:

    def maxProduct(self, words):
        def convert_word_to_num(word):
            return reduce(lambda x, y: x | y, (1 << (ord(c) - ord("a")) for c in word), 0)

        word_nums = [convert_word_to_num(word) for word in words]

        max_len = 0
        for i in xrange(len(words)):
            for j in xrange(i + 1, len(words)):
                if (word_nums[i] & word_nums[j]):
                    continue

                max_len = max(max_len, len(words[i]) * len(words[j]))

        return max_len
