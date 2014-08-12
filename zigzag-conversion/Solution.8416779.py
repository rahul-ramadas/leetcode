class Solution:

    @staticmethod
    def gen_indices(string_length, rows, row_index):
        if row_index >= string_length:
            raise StopIteration

        i = row_index

        down = (rows - 1 - row_index) * 2
        up = row_index * 2

        yield i

        while True:

            if down:
                i += down
                if i >= string_length:
                    raise StopIteration

                yield i

            if up:
                i += up
                if i >= string_length:
                    raise StopIteration
                yield i

            if not down and not up:
                i += 1
                if i >= string_length:
                    raise StopIteration
                yield i

    def convert(self, s, nRows):

        string_length = len(s)
        return ''.join([
            ''.join([s[i] for i in self.gen_indices(string_length, nRows, r)])
            for r in xrange(nRows)
        ])
